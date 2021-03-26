from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class EBSDBasic(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Corrosion", field_type="bool")
        self.add(label='Detectors used')
        self.add(label='Location on sample')
        self.add(label='Any data set to be linked with this experiment', long=True,
                 comment="e.g. EBSD_scheme map etc.")


class EBSDGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Current", unit="nA")
        self.add(label="Magnification")
        self.add(label="Step size", unit=micro+"m")
        self.add(label="Raster size", unit=micro+"m(width) x "+micro+"m(height)")
        self.add(label="Acquisition mode", field_type="class")
        self.add(label="No. of points")
        self.add(label="Working distance", unit='mm')
        self.add(label="Tilt angle", unit=deg)
        self.add(label="Software used for data analysis")


class EBSDGrey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Temperature", unit=deg+'C')
        self.add(label="Relative Humidity", unit='%',
                 other_ttl_relations={"qudt:Unit": "unit:PERCENT_RH"})
        self.add(label="Environmental protection during specimen testing", name="TestingEnv")
        self.add(label="Environmental gas")
        self.add(label="Pillar Orientation", long=True)


class EBSD(EBSDGrey, EBSDGreen, EBSDBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
