from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class EPMABasic(Experiment):
    def __init__(self):
        super().__init__()
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
