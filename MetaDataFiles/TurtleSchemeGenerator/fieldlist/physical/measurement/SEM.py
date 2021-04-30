from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg, micro
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement


class SEMBasic(SpotMeasurement):
    def __init__(self):
        super().__init__()
        self.add(label="Detector ID(s)", name="detectorID")

        # green
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Current", unit="mA")
        self.add(label="Magnification")
        self.add(label="Image width", unit=micro + "m")
        self.add(label="Image size", unit="px(width) x px(height)", qudt="NUM")
        self.add(label="Acquisition mode", field_type=['Line scan', 'Zig-zag scan'])
        self.add(label="Storage Tilt", unit=deg)  # Does this belong in `physical.preparation.Storage`?

        self.sort_fields_by_order_priority()
