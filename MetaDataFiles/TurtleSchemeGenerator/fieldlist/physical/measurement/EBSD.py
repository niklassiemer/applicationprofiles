from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement


class EBSD(SpotMeasurement):
    def __init__(self):
        super().__init__()
        self.add(label="Corrosion", field_type="bool")
        self.add(label='Detector ID(s)', name="detectorID")

        # green
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

        # grey
        self.add(label="Pillar Orientation", long=True)

        self.sort_fields_by_order_priority()
