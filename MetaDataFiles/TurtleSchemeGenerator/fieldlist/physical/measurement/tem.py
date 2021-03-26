from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class TEMBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Pre-treatment"),


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Pre-Preparation routine", long=True)
        self.add(label="Immersion Experiment ID", long=True)
        self.add(label="TEM preparation routine")
        self.add(label="TEM preparation date", field_type="date")
        self.add(label="Operator for sample preparation")
        self.add(label="Sample storage location")
        self.add(label="Sample storage conditions")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Microscope")
        self.add(label="Experiment Date", field_type='date')
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Magnification / Camera length", name='magnefication', unit='mm')
        self.add(label="Electron dose", unit='e/nm'+squared, qudt="E-PER-NanoM2")
        self.add(label="Dwell time", unit="ms")
        self.add(label="Data dimension")
        self.add(label="1st dimension unit")
        self.add(label="1st dimension pixels")
        self.add(label="1st dimension unit scaling")
        self.add(label="1st dimension starting pixel")
        self.add(label="2nd dimension unit")
        self.add(label="2nd dimension pixels")
        self.add(label="2nd dimension unit scaling")
        self.add(label="2nd dimension starting pixel")


class TEM(Green, Yellow, TEMBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()