from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import SFBFields, FieldList

micro = "\u03bc"
deg = "\u00b0"


class EPMABasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Instrument used", name="instrument")
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Acquisition mode", field_type="class")
        self.add(label="Elements included/Peak ID", name='elementsIncluded')


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Count rate", unit='cps', qudt='NUM-PER-SEC')
        self.add(label="Spot size")
        self.add(label="Measurement time/date", name="measurementTime")
        self.add(label="Background method")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Standard used")
        self.add(label="Magnification")
        self.add(label="Dwell time", unit='s')
        self.add(label="Working distance", unit='mm')
        self.add(label="Tilt", unit=deg)


class EPMA(Grey, Green, EPMABasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


EPMA_scheme = Scheme("EPMA")
EPMA_scheme.fields = EPMABasic()
EPMA_scheme.write()

EPMA_scheme.fields = Green()
EPMA_scheme.write('EPMA_green.ttl')

EPMA_scheme.fields = Grey()
EPMA_scheme.write("EPMA_grey.ttl")

EPMA_scheme.fields = EPMA()
EPMA_scheme.write('EPMA_full.ttl')
