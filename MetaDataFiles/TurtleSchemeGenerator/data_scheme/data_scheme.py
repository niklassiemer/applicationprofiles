# -*- coding: utf-8 -*-
"""Meta Data Schemes """
import os.path

from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import _gen_unit_relation
import pandas as pd


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
            self._name = "".join(label.split(" "))
        else:
            self._name = name
        if isinstance(options, str):
            self.options = list(options)
        else:
            self.options = options
        self.base = ""

    @property
    def name(self):
        if self.base == "":
            return self._name
        else:
            return self.base + '/' + self._name

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
        new = DropdownList(
            label=self.label,
            options=self.options,
            name=self.name,
            title=self.title
        )
        new.base = self.base
        return new

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
            long=False,
            example_input="",
            comment="",
            order_priority=None,
            qudt=None,
            sh_path=None,
            other_ttl_relations=None
    ):
        """
        Single Field of a meta data scheme
        Params:
            label(str): Displayed label
            name(str): Internal name - required if the label contains special characters, i.e  '/', '(', ')'
            field_type(str/obj/None): 'string', 'bool', field_type_object; 'string' is default
            required(bool): if True this Field is required; False is default
            unit(str/None): unit of the quantity; e.g. 'm/s'
            qudt(str/None): qudt unit name of the unit; e.g. 'M-PER-SEC'
            long(bool): If True this fiels may contain more than one line/ value
            sh_path(str/None): value for the 'sh:path' property; default is 'sfb1394:' + name
            order_priority(int/None): Priority for the order of fields:
                fields with smaller positive numbers are displayed first.
                fields without priority (0 or None) are displayed second.
                fields with negative priority are displayed last; -1 is lowest possible priority
            other_ttl_relations{dict/None): other ontology relations; e.g. {"qudt:Unit": "unit:M-PER-SEC"}
        """
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
        if other_ttl_relations is None:
            self.ttl_relations = {}
        else:
            self.ttl_relations = other_ttl_relations

        self.comment = comment
        self.example_input = example_input
        self.order_priority = order_priority
        self._order_number = None

        self.long = long
        if qudt is not None:
            self.ttl_relations[_gen_unit_relation(qudt, qudt=True)[0]] = _gen_unit_relation(qudt, qudt=True)[1]
        self.unit = unit
        if unit is not None and "qudt:Unit" not in self.ttl_relations:
            try:
                self.ttl_relations[_gen_unit_relation(self.unit)[0]] = _gen_unit_relation(self.unit)[1]
            except KeyError:
                raise ValueError(f"Unit '{unit}' is not linked to qudt ontology.")
        self._single_type = True

        if field_type == 'class' or field_type == 'list':
            self._single_type = False
            self.field_type = field_type
        elif isinstance(field_type, DropdownList):
            self._single_type = False
            self.field_type = field_type.copy()
        elif isinstance(field_type, list):
            self._single_type = False
            self.field_type = DropdownList(label=self.label, options=field_type)
        else:
            self.field_type = field_type

        self.required = required
        if sh_path is None and "sh:path" not in self.ttl_relations.keys():
            self.ttl_relations["sh:path"] = "sfb1394:" + self.name
        elif sh_path is not None:
            self.ttl_relations["sh:path"] = sh_path

    @property
    def ttl_field_type(self):
        if self.field_type is None or self.field_type == "string":
            return 'xsd:string'
        elif self.field_type == "date":
            return 'xsd:date'
        elif self.field_type == 'bool' or self.field_type == 'boolean':
            return 'xsd:boolean'
        else:
            return ''

    @property
    def txt_field_type(self):
        if self.field_type is None or self.field_type == "string":
            return 'string'
        elif self.field_type == "date":
            return 'date'
        elif self.field_type == 'bool' or self.field_type == 'boolean':
            return 'boolean'
        elif isinstance(self.field_type, DropdownList):
            return 'choice: ' + str(self.field_type.options)
        elif self.field_type == 'class' or self.field_type == 'list':
            return 'undefined list'
        else:
            return self.field_type

    @property
    def _class_name(self):
        if isinstance(self.field_type, str):
            return self.field_type
        elif isinstance(self.field_type, DropdownList):
            return self.field_type.name
        else:
            raise AttributeError

    @property
    def ttl_term_str(self):
        result = ''
        if not self.ttl_relations["sh:path"] == "sfb1394:" + self.name:
            return result

        if self.unit is None:
            label = self.label
        else:
            label = self.label + ' [' + self.unit + ']'

        result += self.ttl_relations["sh:path"] + ' \n'
        result += '  rdfs:label "' + label + '"@en, "' + label + '"@de ;\n'
        result += '. \n\n'
        return result

    def ttl_str(self, schema_name, order_number=None):
        _order_number = order_number if order_number is not None else self._order_number
        result = ''
        result += 'coscineSfb1394' + schema_name + ':' + self.name + ' \n'
        result += '  sh:path ' + self.ttl_relations["sh:path"] + ' ;\n'
        result += '  sh:order ' + str(_order_number) + ' ;\n'

        if self.required:
            result += ' sh:minCount 1 ;\n'

        if self.long:
            result += ' dash:singleLine false ;\n'

        if self._single_type:
            result += '  sh:datatype ' + self.ttl_field_type + ' ;\n'
        else:
            result += '  sh:maxCount 1 ;\n'

        result += '  sh:name "' + self.label_w_unit + '"@en, "' + self.label_w_unit + '"@de ;\n'

        for key, value in self.ttl_relations.items():
            if not (key == 'qudt:Unit' and value == 'unit:None'):
                result += '  ' + key + ' ' + value + ' ;\n'

        if self._single_type:
            result += '. \n'
        else:
            result += '  sh:class <' + self._class_name + '> . \n'
        return result

    @property
    def label_w_unit(self):
        if self.unit is None:
            label = self.label
        else:
            label = self.label + ' [' + self.unit + ']'
        return label

    @property
    def txt(self):
        indent = '   '
        result = self.label_w_unit
        if self.required:
            result += '*'
        result = result.ljust(40)
        result += ': '
        if len(self.example_input) > 0:
            result += indent + '"' + self.example_input + '" '
        result += indent + '(' + self.txt_field_type + ')' + indent
        if len(self.comment) > 0:
            result += '#' + indent + self.comment + ' '
        return result + '\n'

    @property
    def list(self):
        return [self.label_w_unit, self.required, self.example_input, self.txt_field_type, self.comment]

    def copy(self):
        return MetaDataField(
            label=self.label,
            name=self.name,
            field_type=self.field_type,
            required=self.required,
            unit=self.unit,
            long=self.long,
            comment=self.comment,
            example_input=self.example_input,
            qudt=None,  # stored in self.ttl_relations
            sh_path=None,  # stored in self.ttl_relations
            order_priority=self.order_priority,
            other_ttl_relations=self.ttl_relations
        )

    def __lt__(self, other):
        self_order_prio = self.order_priority if self.order_priority is not None else 0
        other_order_prio = other.order_priority if other.order_priority is not None else 0

        # Same sign and none is zero: normal comparison
        if self_order_prio * other_order_prio > 0:
            return self_order_prio < other_order_prio

        # Different signs or at least one is zero:
        # positive number < 0 < negative number thus:
        return self_order_prio > other_order_prio

    def __gt__(self, other):
        self_order_prio = self.order_priority if self.order_priority is not None else 0
        other_order_prio = other.order_priority if other.order_priority is not None else 0

        # Same sign and none is zero: normal comparison
        if self_order_prio * other_order_prio > 0:
            return self_order_prio > other_order_prio

        # Different signs or at least one is zero:
        # positive number < 0 < negative number thus:
        return self_order_prio < other_order_prio


class FieldList:
    def __init__(self, field_list=None):
        """
        List of meta data fields
        Params:
            field_list(list/None): list containing only MetaDataFields.
        """
        if field_list is not None:
            for item in field_list:
                self.enforce_type(item, MetaDataField)
            self._fields = field_list.copy()
        else:
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

    def sort_fields_by_order_priority(self):
        """Sorts the fields in the FieldList by their order_parameter"""
        self._fields.sort()

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

    def to_txt(self):
        result = ''
        for field in self._fields:
            result += field.txt
        return result

    def to_list(self):
        result = []
        for field in self._fields:
            result.append(field.list)
        return result

    def to_pandas(self):
        return pd.DataFrame(self.to_list(), columns=['name', 'required', 'example_input', 'type', 'comment'])

    def write(self, filename, encoding='utf8'):
        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.to_txt())


class MetaDataSchemes:
    def __init__(self, name, extends=None):
        """

        Args:
            name (str): Name of the meta data scheme
            extends (str/:class:`MetaDataSchemes`/None): name or class of a parent meta data scheme

            if extends is a string it adds the
                'rdfs:subClassOf the_provided_string'
            as parent class definition, i.e. the string has to point to the actual location of the parent
            meta data scheme. TODO: verify this is working; it might crash the order parameter...
            if extends is a MetaDataScheme the current scheme is appended to this parent scheme.
        """
        self._path_and_name = name
        if '/' in name:
            self.name = name.split('/')[-1]
        else:
            self.name = name

        self.order_fields_by_priority = False
        self.parent_class = None
        self.parent_class_name = None
        if isinstance(extends, str):
            self.parent_class_name = extends
        elif isinstance(extends, MetaDataSchemes):
            self.parent_class = extends
            self.parent_class_name = extends.class_name
        elif extends is not None:
            raise TypeError(f'Expected a MetaDataSchemes or str but got {type(extends)}')
        self._fields = FieldList()
        self.preamble_prefixes = {
            "dash": "<http://datashapes.org/dash#>",
            "rdf": "<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
            "sh": "<http://www.w3.org/ns/shacl#>",
            "xsd": "<http://www.w3.org/2001/XMLSchema#>",
            "rdfs": "<http://www.w3.org/2000/01/rdf-schema#>",
            "qudt": "<http://qudt.org/schema/qudt/>",
            "unit": "<http://qudt.org/vocab/unit/>",
            "csmd": "<http://www.purl.org/net/CSMD/4.0#>",
            "dcterms": "<http://purl.org/dc/terms/>",
            "sfb1394": "<http://purl.org/coscine/terms/sfb1394#>"
        }

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, field_list):
        if isinstance(field_list, list):
            self._fields = FieldList(field_list)
        else:
            self._fields = field_list

    @property
    def n_fields(self):
        result = len(self.fields)
        if self.parent_class is not None:
            result += self.parent_class.n_fields
        return result

    @property
    def property_prefix(self):
        result = "@prefix coscineSfb1394" + self.name
        result += ": <https://purl.org/coscine/ap/sfb1394/" + self._path_and_name + "#> .\n"
        return result

    @property
    def class_name(self):
        return "<https://purl.org/coscine/ap/sfb1394/" + self._path_and_name + "/>"

    def gen_scheme(self):
        if len(self.fields) == 0:
            raise TypeError("No Field specified")
        if self.order_fields_by_priority:
            self._order_all_fields()
        result = ""
        result += self.gen_preamble()
        result += self.ttl_str(target_class=True, ordered_fields=self.order_fields_by_priority)
        result += " # Shape URL https://purl.org/coscine/ap/sfb1394/" + self._path_and_name + "/"
        return result

    def ttl_str(self, target_class=True, ordered_fields=False):
        result = ""
        result += self.property_prefix
        result += self.gen_required_fields(ordered_fields=ordered_fields)
        result += "\n # " + self.name + ' \n'
        result += self.gen_page(target_class=target_class)
        result += self.gen_nodes(ordered_fields=ordered_fields)
        return result

    def gen_preamble(self):
        result = ""
        result += "@base " + self.class_name + " .\n\n"
        for key, value in self.preamble_prefixes.items():
            result += "@prefix " + key + ": " + value + " .\n"
        return result

    @property
    def full_field_list(self):
        full_list = FieldList()
        if self.parent_class is not None:
            full_list += self.parent_class.full_field_list
        full_list += self.fields
        return full_list

    def _order_all_fields(self):
        full_list = self.full_field_list
        full_list.sort_fields_by_order_priority()
        for i, field in enumerate(full_list):
            field._order_number = i

    def gen_required_fields(self, ordered_fields=False):
        result = ""
        if self.parent_class is not None:
            result += self.parent_class.ttl_str(target_class=False, ordered_fields=ordered_fields)
        for field in self.fields:
            if hasattr(field.field_type, 'ttl_str'):
                field.field_type.base = "https://purl.org/coscine/ap/sfb1394/" + self._path_and_name
                result += field.field_type.ttl_str()
        return result

    def gen_page(self, target_class=True):
        result = ""
        result += self.class_name
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
            result += '  sh:targetClass <https://purl.org/coscine/ap/sfb1394/' + self._path_and_name + '/> ;'
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

    def gen_nodes(self, ordered_fields=False):
        result = ""
        if ordered_fields:
            for field in self.fields:
                result += '\n'
                result += field.ttl_str(schema_name=self.name)
            return result

        if self.parent_class is not None:
            offset = self.parent_class.n_fields
        else:
            offset = 0
        for i, field in enumerate(self.fields):
            result += '\n'
            result += field.ttl_str(schema_name=self.name, order_number=i + offset)
        return result

    @staticmethod
    def _parse_extension(implicit_extension, explicit_extension):
        if explicit_extension is not None and len(explicit_extension) > 0 and explicit_extension[0] != '.':
            explicit_extension = '.' + explicit_extension

        if (
                implicit_extension is not None
                and explicit_extension is not None
                and implicit_extension != ''
                and explicit_extension != implicit_extension
        ):
            raise ValueError(f'Implicit ({implicit_extension}) and explicit ({explicit_extension}) extensions were '
                             f'both provided and do not match!')

        return explicit_extension or implicit_extension or '.ttl'

    def write(self, filename=None, encoding='utf8', file_extension=None):
        """write the whole schema to a file.

        Args:
            filename(str): name of the file written; defaults to schema name + file_extension
                           if given with file extension, the corresponding file_extension is used.
            encoding(str): encoding used to write the file; defaults to 'utf8'
            file_extension(str/None): extension of the file to write. Possible extensions are:
                '.ttl' (default): write a turtle schema
                '.txt': write a plain text list
        """

        if filename is not None:
            _filename, _ext = os.path.splitext(filename)
        else:
            _filename = self.name
            _ext = ""

        _ext = self._parse_extension(_ext, file_extension)
        _filename = _filename + _ext

        if _ext == '.ttl':
            with open(_filename, 'w', encoding=encoding) as f:
                f.write(self.gen_scheme())
        elif _ext == '.txt':
            self.fields.write(_filename, encoding=encoding)
        else:
            raise ValueError(f"File extension {_ext} is not known.")
