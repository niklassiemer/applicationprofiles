from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

micro = "\u03bc"
deg = "\u00b0"


class SEMBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Location")
        self.add(label="Instrument used", name="instrument")
        self.add(label="Detector used", name="detector")


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Temperature", unit=deg+'C'),
        self.add(label="Relative Humidity", unit='%', qudt="PERCENT_RH"),
        self.add(label="Environmental protection during specimen transfer", name="TestingEnv"),
        self.add(label="Environmental gas"),


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Current", unit="mA")
        self.add(label="Magnification")
        self.add(label="Image width", unit=micro + "m")
        self.add(label="Image size", unit="px(width) x px(height)", qudt="NUM")
        self.add(label="Acquisition mode", field_type="class")
        self.add(label="Storage Tilt", unit=deg)


class SEM(Grey, Green, Yellow, SEMBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


SEM_scheme = Scheme("SEM")
SEM_scheme.fields = SEMBasic()
SEM_scheme.write("SEM.ttl")

SEM_scheme.fields = Green()
SEM_scheme.write('SEM_green.ttl')

SEM_scheme.fields = Grey()
SEM_scheme.write('SEM_grey.ttl')

SEM_scheme.fields = Yellow()
SEM_scheme.write('SEM_yellow.ttl')

SEM_scheme.fields = SEM()
SEM_scheme.write('SEM_full.ttl')
