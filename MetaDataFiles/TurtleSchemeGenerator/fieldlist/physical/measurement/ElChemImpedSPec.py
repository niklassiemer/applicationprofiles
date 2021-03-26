from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import ElChemImpedSpecYellow


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


class ElChemImpedSpec(Grey, Green, ElChemImpedSpecYellow, ElChemImpedSpecBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()