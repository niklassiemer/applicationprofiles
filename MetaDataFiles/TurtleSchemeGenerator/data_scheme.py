"""Meta Data Schemes """


class MetaDataField:
    def __init__(self, label, name=None, ftype=None, required=False, long=False):
        self.label = label
        if name is None:
            self.name = "".join(label.split(" "))
        else:
            self.name = name
        self.long = long
        if ftype is None:
            self.ftype = 'xsd:string'
        else:
            self.ftype = ftype
        self.required = required
        self.sh_path = "sfb1394:" + self.name


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
        self._properties = []

    def gen_scheme(self):
        if len(self._properties) == 0:
            print("No Field specified")
            return
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

    def add_field(self, label, name=None, ftype=None, required=False, long=False):
        self._properties.append(MetaDataField(label=label, name=name, ftype=ftype, required=required, long=long))

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
        for field in self._properties[0:-1]:
            result += '  sh:property coscineSfb1394' + self.name + ':' + field.name + ' ;\n'
        field = self._properties[-1]
        result += '  sh:property coscineSfb1394' + self.name + ':' + field.name + ' .\n'
        return result

    def gen_nodes(self):
        result = ""
        for i, field in enumerate(self._properties):
            result += '\n'
            result += 'coscineSfb1394' + self.name + ':' + field.name + ' \n'
            result += '  sh:path ' + field.sh_path + ' ;\n'
            result += '  sh:order ' + str(i) + ' ;\n'
            if field.required:
                result += ' sh:minCount 1 ;\n'
            if field.long:
                result += ' dash:singleLine false ;\n'
            result += '  sh:datatype ' + field.ftype + ' ;\n'
            result += '  sh:name "' + field.label + '"@en, "' + field.label + '"@de ;\n'
            result += '. \n'
        return result
