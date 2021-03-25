from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import SFBFields, FieldList

micro = "\u03bc"
deg = "\u00b0"


class CalphadDBBasic(SFBFields):
    def __init__(self):
        super().__init__()
        # This will not be unique:
        self.add(label="Database filename")
        self.add(label="Elements included")
        self.add(label="Element data")
        self.add(label="Date", field_type='date')
        self.add(label="Licence")
        self.add(label="Software used to test")
        # TODO: What is the purpose?
        self.add(label="References")


class CalphadDBGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Phases and models")


class CalphadDBGrey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Crystal structure", long=True)
        self.add(label="Compounds", long=True)


class CalphadDB(CalphadDBGrey, CalphadDBGreen, CalphadDBBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()

CALPHAD_DB = Scheme("Calphad_db")
CALPHAD_DB.fields = CalphadDBBasic()
CALPHAD_DB.write()

CALPHAD_DB.fields = CalphadDBGreen()
CALPHAD_DB.write("Calphad_db_green.ttl")

CALPHAD_DB.fields = CalphadDBGrey()
CALPHAD_DB.write("Calphad_db_grey.ttl")

CALPHAD_DB.fields = CalphadDB()
CALPHAD_DB.write("Calphad_db_full.ttl")

