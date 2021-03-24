from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field
from data_scheme import SFBFields, FieldList

micro = "\u03bc"
deg = "\u00b0"


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


ICP_MS = Scheme("ICP_MS")
ICP_MS.fields = IcpMsBasic()
ICP_MS.write()

ICP_MS.fields = Yellow()
ICP_MS.write("ICP_MS_yellow.ttl")

ICP_MS.fields = IcpMS()
ICP_MS.write("ICP_MS_full.ttl")

