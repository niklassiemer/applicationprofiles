from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class IcpMsBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label="Analyzed elements")
        self.add(label="Isotope")
        self.add(label="Measurement modus")
        self.add(label='Sweeps')
        self.add(label="Replicates")
        self.add(label="Instrument used")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class IcpMS(Yellow, IcpMsBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()