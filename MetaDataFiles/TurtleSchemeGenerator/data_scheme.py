# -*- coding: utf-8 -*-
"""Meta Data Schemes """


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
            self.name = "".join(label.split(" "))
            if '/' in self.name:
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

        result += '  sh:name "' + label + '"@en, "' + label + '"@de ;\n'

        if self._single_type:
            result += '. \n'
        else:
            result += '  sh:class <> . \n'
        return result


class MetaDataSchemes:
    def __init__(self, name):
        self.name = name
        self.base = "@base <https://purl.org/coscine/ap/sfb1394/" + self.name + "/> .\n"

        self.preamble = '''
@prefix dash: <http://datashapes.org/dash#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

@prefix csmd: <http://www.purl.org/net/CSMD/4.0#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

@prefix sfb1394: <http://purl.org/coscine/terms/sfb1394#> .
'''
        self.fields = []

    def gen_scheme(self):
        if len(self.fields) == 0:
            raise TypeError("No Field specified")
        result = ""
        result += self.gen_preamble()
        result += self.gen_page()
        result += self.gen_nodes()
        return result

    def gen_preamble(self):
        result = ""
        result += self.base
        result += self.preamble
        result += "@prefix coscineSfb1394" + self.name +\
                  ": <https://purl.org/coscine/ap/sfb1394/" + self.name + "#> .\n"
        return result

    def add_field(self, *args, **kwargs):
        self.fields.append(MetaDataField(*args, **kwargs))

    def gen_page(self):
        result = ""
        result += "<https://purl.org/coscine/ap/sfb1394/" + self.name + "/>"
        result += """
  dcterms:license <http://spdx.org/licenses/MIT> ;
  dcterms:publisher <https://itc.rwth-aachen.de/> ;
  dcterms:rights "Copyright © 2020 IT Center, RWTH Aachen University" ;
  dcterms:title  """
        result += '"SFB1394 ' + self.name + '"@en ;\n\n'
        result += '  a sh:NodeShape ;\n'
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
        for i, field in enumerate(self.fields):
            result += '\n'
            result += field.ttl_str(schema_name=self.name, order_number=i)
        return result

    def write(self, filename, encoding='utf8'):
        with open(filename, 'w', encoding=encoding) as f:
            f.write(self.gen_scheme())
