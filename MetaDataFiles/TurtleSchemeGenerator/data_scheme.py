# -*- coding: utf-8 -*-
"""Meta Data Schemes """


class DropdownList:
    def __init__(
        self,
        label,
        options,
        name=None,
        title=None,
    ):
        self.label = label
        if title is None:
            self.title = self.label
        else:
            self.title = title

        if name is None:
            self.name = "".join(label.split(" "))
        else:
            self.name = name
        if isinstance(options, str):
            self.options = list(options)
        else:
            self.options = options

    def ttl_preamble(self):
        result = '@base <'
        result += self.name + '>.\n\n'
        result += """@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix xml: <http://www.w3.org/XML/1998/namespace>.
@prefix dcterms: <http://purl.org/dc/terms/>.
@prefix skos: <http://www.w3.org/2004/02/skos/core#>.

        """
        return result

    def write(self, filename, encoding='utf8'):
        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.ttl_preamble())
            f.write(self.ttl_str())

    def copy(self):
        return DropdownList(
            label=self.label,
            options=self.options,
            name=self.name,
            title=self.title
        )

    def ttl_str(self):
        result = "<" + self.name + "> "
        result += """
  dcterms:license <http://spdx.org/licenses/MIT> ;
  dcterms:publisher <https://itc.rwth-aachen.de/> ;
  dcterms:rights "Copyright © 2020 IT Center, RWTH Aachen University" ;
  dcterms:title  """
        result += '"' + self.title + '"@en ;\n'
        result += '  rdfs:label '
        result += '"' + self.label + '"@de ,\n'
        result += '"' + self.label + '"@en .\n'

        for idx, option in enumerate(self.options):
            result += "<" + self.name + "#" + str(idx) + "> a "
            result += "<" + self.name + "#" + str(idx) + ">;\n"
            result += '  rdfs:label '
            result += '"' + option + '"@de ,\n'
            result += '"' + option + '"@en ;\n'
            result += '  rdfs:subClassOf '
            result += "<" + self.name + ">.\n"

        return result


class MetaDataField:
    def __init__(
            self,
            label,
            name=None,
            field_type=None,
            required=False,
            unit=None,
            long=False
    ):
        self.label = label
        if name is None:
            name_list = label.split(" ")
            name_list = [name.capitalize() for name in name_list]
            self.name = "".join(name_list)
            self.name = self.name[0].lower() + self.name[1:]
            if '/' in self.name or '(' in self.name or ')' in self.name:
                raise ValueError('Label contains special character and name cannot be derived: specify name= ')
        else:
            self.name = name
        self.long = long
        self.unit = unit
        self._single_type = True

        if field_type is None or field_type == "string":
            self.field_type = 'xsd:string'
        elif field_type == "date":
            self.field_type = 'xsd:date'
        elif field_type == 'bool' or field_type == 'boolean':
            self.field_type = 'xsd:boolean'
        elif field_type == "class" or field_type == "list":
            self._single_type = False
            self.field_type = field_type
            self._class_name = ""
        elif isinstance(field_type, DropdownList):
            self._single_type = False
            self.field_type = field_type.copy()
            self._class_name = field_type.name
        else:
            self.field_type = field_type

        self.required = required
        self.sh_path = "sfb1394:" + self.name

    def ttl_str(self, schema_name, order_number):
        result = ''
        result += 'coscineSfb1394' + schema_name + ':' + self.name + ' \n'
        result += '  sh:path ' + self.sh_path + ' ;\n'
        result += '  sh:order ' + str(order_number) + ' ;\n'

        if self.required:
            result += ' sh:minCount 1 ;\n'

        if self.long:
            result += ' dash:singleLine false ;\n'

        if self._single_type:
            result += '  sh:datatype ' + self.field_type + ' ;\n'
        else:
            result += '  sh:maxCount 1 ;\n'

        if self.unit is None:
            label = self.label
        else:
            label = self.label + ' [' + self.unit + ']'
            # TODO: add unit ontology

        result += '  sh:name "' + label + '"@en, "' + label + '"@de ;\n'

        if self._single_type:
            result += '. \n'
        else:
            result += '  sh:class <' + self._class_name + '> . \n'
        return result

    def copy(self):
        return MetaDataField(
            label=self.label,
            name=self.name,
            field_type=self.field_type,
            required=self.required,
            unit=self.unit,
            long=self.long
        )


class FieldList:
    def __init__(self):
        self._fields = []

    @staticmethod
    def enforce_type(obj, class_):
        if not isinstance(obj, class_):
            raise TypeError(f'Expected a {class_.__name__} but got {type(obj)}')

    def append(self, item):
        self.enforce_type(item, MetaDataField)
        self._fields.append(item)

    def add(self, label, **field_kwargs):
        self._fields.append(MetaDataField(label, **field_kwargs))

    def __getitem__(self, item):
        return self._fields.__getitem__(item)

    def __next__(self):
        return self._fields.__next__()

    def __add__(self, other):
        self.enforce_type(other, FieldList)
        new_list = FieldList()
        new_list._fields = self._fields + other._fields
        return new_list

    def __iadd__(self, other):
        self.enforce_type(other, FieldList)
        self._fields += other._fields
        return self

    def __len__(self):
        return self._fields.__len__()

    def copy(self):
        new_list = FieldList()
        new_list._fields = [field.copy() for field in self._fields]
        return new_list


class SFBFields(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="ID", required=True)  # Database ID for the object, be it sample, experiment, sim...
        self.add(label="Operator", required=True)
        self.add(label="Affiliation")
        self.add(label="DOIs", long=True)  # To associate publications produced using this object
        self.add(label="Comments", long=True)


class MetaDataSchemes:
    def __init__(self, name, extends=None):
        """

        Args:
            name (str): Name of the meta data scheme
            extends (str/:class:`MetaDataSchemes`/None): name or class of a parent meta data scheme

            if extends is a string it adds the
                rdfs:subClassOf the_provided_string
            as parent class definition, i.e. the string has to point to the actual location of the parent
            meta data scheme. TODO: verify this is working; it might crash the order parameter...
            if extends is a MetaDataScheme the current scheme is appended to this parent scheme.
        """
        self.name = name
        self.parent_class = None
        self.parent_class_name = None
        if isinstance(extends, str):
            self.parent_class_name = extends
        elif isinstance(extends, MetaDataSchemes):
            self.parent_class = extends
            self.parent_class_name = extends.class_name
        elif extends is not None:
            raise TypeError(f'Expected a MetaDataSchemes or str but got {type(extends)}')
        self.fields = FieldList()
        # Define strings for the ttl schema
        self.preamble_prefixes = '''
@prefix dash: <http://datashapes.org/dash#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

@prefix csmd: <http://www.purl.org/net/CSMD/4.0#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

@prefix sfb1394: <http://purl.org/coscine/terms/sfb1394#> .
'''

    @property
    def n_fields(self):
        result = len(self.fields)
        if self.parent_class is not None:
            result += self.parent_class.n_fields
        return result

    @property
    def property_prefix(self):
        result = "@prefix coscineSfb1394" + self.name
        result += ": <https://purl.org/coscine/ap/sfb1394/" + self.name + "#> .\n"
        return result

    @property
    def class_name(self):
        return "<https://purl.org/coscine/ap/sfb1394/" + self.name + "/>"

    def gen_scheme(self):
        if len(self.fields) == 0:
            raise TypeError("No Field specified")
        result = ""
        result += self.gen_preamble()
        result += self.ttl_str(target_class=True)
        result += " # Shape URL https://purl.org/coscine/ap/sfb1394/" + self.name + "/"
        return result

    def ttl_str(self, target_class=True):
        result = ""
        result += self.property_prefix
        result += self.gen_required_fields()
        result += self.gen_page(target_class=target_class)
        result += self.gen_nodes()
        return result

    def gen_preamble(self):
        result = ""
        result += "@base " + self.class_name + " .\n"
        result += self.preamble_prefixes
        return result

    def gen_required_fields(self):
        result = ""
        if self.parent_class is not None:
            result += "\n # " + self.parent_class.name + ' \n'
            result += self.parent_class.ttl_str(target_class=False)
        for field in self.fields:
            if hasattr(field.field_type, 'ttl_str'):
                result += field.field_type.ttl_str()
        return result

    def gen_page(self, target_class=True):
        result = ""
        result += "<https://purl.org/coscine/ap/sfb1394/" + self.name + "/>"
        result += """
  dcterms:license <http://spdx.org/licenses/MIT> ;
  dcterms:publisher <https://itc.rwth-aachen.de/> ;
  dcterms:rights "Copyright © 2020 IT Center, RWTH Aachen University" ;
  dcterms:title  """
        result += '"SFB1394 ' + self.name + '"@en ;\n\n'
        result += '  a sh:NodeShape ;\n'
        if self.parent_class_name is not None:
            result += '  rdfs:subClassOf ' + self.parent_class_name + ' ;\n'
        if target_class:
            result += '  sh:targetClass <https://purl.org/coscine/ap/sfb1394/' + self.name + '/> ;'
        result += '''
  sh:closed true ;

  sh:property [
    sh:path rdf:type ;
  ] ;

'''
        for field in self.fields[0:-1]:
            result += '  sh:property coscineSfb1394' + self.name + ':' + field.name + ' ;\n'
        field = self.fields[-1]
        result += '  sh:property coscineSfb1394' + self.name + ':' + field.name + ' .\n'
        return result

    def gen_nodes(self):
        result = ""
        if self.parent_class is not None:
            offset = self.parent_class.n_fields
        else:
            offset = 0
        for i, field in enumerate(self.fields):
            result += '\n'
            result += field.ttl_str(schema_name=self.name, order_number=i + offset)
        return result

    def write(self, filename=None, encoding='utf8'):
        if filename is None:
            filename = self.name + '.ttl'
        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.gen_scheme())
