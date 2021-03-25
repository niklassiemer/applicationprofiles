from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

micro = "\u03bc"
deg = "\u00b0"


class SIETBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")
        self.add(label="Ion selective electrode solution")
        self.add(label="Ion selective membrane")
        self.add(label="Reference solution")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class SIET(Yellow, SIETBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


SIET_scheme = Scheme("SIET")
SIET_scheme.fields = SIETBasic()
SIET_scheme.write()

SIET_scheme.fields = Yellow()
SIET_scheme.write("SIET_yellow.ttl")

SIET_scheme.fields = SIET()
SIET_scheme.write("SIET_full.ttl")

