from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class XRDBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Instrument used", name="instrument")
        self.add(label="Specimen type", field_type='class')
        self.add(label="Specimen ID")
        self.add(label="Radiation source")
        self.add(label="Detector")
        self.add(label="Current", unit='mA')
        self.add(label="Voltage", unit='kV')
        self.add(label="Measurement position")
        self.add(label="Scan Mode", field_type='class')
        self.add(label="Incidence angle Omega", unit=deg)


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Filter")
        self.add(label="Mask size", unit='mm')
        self.add(label="Scan axis", field_type='class')
        self.add(label="Diffraction angle 2Theta", name='diffractionAngle', unit=deg)
        self.add(label="Rotation angle phi", unit=deg)
        self.add(label="Rotation angle chi", unit=deg)
        self.add(label="Number of frames")
        self.add(label="Measurement time", unit='s')
        self.add(label="Start 2Theta", unit=deg)
        # TODO: check if there is a End 2Theta missing in the docx.
        # self.add(label="End 2Theta", unit=deg)
        self.add(label="Start Theta", unit=deg)
        self.add(label="End Theta", unit=deg)
        self.add(label="Fixed 2Theta position", unit=deg)
        self.add(label="Step size", unit=deg)
        self.add(label="Time per step", unit='s')


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Preparation routine")
        self.add(label='Pre-treatment', field_type='class')
        self.add(label="Sample storage")
        self.add(label="Immersion Experiment ID")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Measurement time/date", name="measurementTime")


class XRD(Grey, Green, Yellow, XRDBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()