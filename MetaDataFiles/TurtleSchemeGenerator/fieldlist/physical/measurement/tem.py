from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


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


class TEM(Experiment, Green):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
