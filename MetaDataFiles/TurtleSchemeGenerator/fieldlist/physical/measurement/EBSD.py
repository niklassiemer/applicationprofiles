from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class EBSDBasic(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Sample location", example_input="Longitudanal cross-section; from top surface")
        self.add(label="Corrosion", field_type="bool")
        self.add(label='Detector ID(s)', name="detectorID")
        self.add(label='Location on sample', example_input="5mm in X and 4 mm in Y from lower left corner")
        # self.add(label='Any data set to be linked with this experiment', long=True,
        #         comment="e.g. EBSD_scheme map etc.")


class EBSDGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Current", unit="nA")
        self.add(label="Magnification")
        self.add(label="Step size", unit=micro+"m")
        self.add(label="Raster size", unit=micro+"m(width) x "+micro+"m(height)")
        self.add(label="Acquisition mode", field_type=['Line scan', 'Zig-zag scan'])
        self.add(label="No. of points")
        self.add(label="Working distance", unit='mm')
        self.add(label="Tilt angle", unit=deg)
        self.add(label="Software used for data analysis")


class EBSDGrey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Pillar Orientation", long=True)


class EBSD(EBSDGrey, EBSDGreen, EBSDBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
