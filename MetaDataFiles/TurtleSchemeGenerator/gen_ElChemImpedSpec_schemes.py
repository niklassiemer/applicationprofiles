from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

micro = "\u03bc"
deg = "\u00b0"


class ElChemImpedSpecBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label="Mode")
        self.add(label="Alternating Current", unit='mA')
        self.add(label="Alternating Voltage", unit='mV')
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt="MilliV")
        self.add(label="Counter electrode")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Potentiostat")
        self.add(label="Time OCP", unit='s')
        self.add(label="Frequency Start", unit='Hz')
        self.add(label="Frequency End", unit='Hz')


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Time of measurement", unit='min')


class ElChemImpedSpec(Grey, Green, Yellow, ElChemImpedSpecBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


ElChemImpedSpec_scheme = Scheme("ElChemImpedSpec")
ElChemImpedSpec_scheme.fields = ElChemImpedSpecBasic()
ElChemImpedSpec_scheme.write()

ElChemImpedSpec_scheme.fields = Yellow()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_yellow.ttl")

ElChemImpedSpec_scheme.fields = Green()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_green.ttl")

ElChemImpedSpec_scheme.fields = Grey()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_grey.ttl")

ElChemImpedSpec_scheme.fields = ElChemImpedSpec()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_full.ttl")


