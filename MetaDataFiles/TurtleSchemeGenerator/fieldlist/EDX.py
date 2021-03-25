from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class EDXBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Instrument used", name="instrument")
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Measurement position")
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Magnification")
        self.add(label="Dwell time", unit='s')
        self.add(label="Tilt", unit=deg)
        self.add(label="Acquisition mode", field_type=["Point scan", "Line scan", "Mapping"])


class EDXGrey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Count rate", unit='cps', qudt='NUM-PER-SEC')
        self.add(label="Spot size")
        self.add(label="Working distance", unit='mm')
        self.add(label="Elements included/Peak ID", name='elementsIncluded')
        self.add(label="Background method")


class EDXGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Measurement time/date", name="measurementTime")
        self.add(label="Standard used")


class EDX(EDXGrey, EDXGreen, EDXBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()