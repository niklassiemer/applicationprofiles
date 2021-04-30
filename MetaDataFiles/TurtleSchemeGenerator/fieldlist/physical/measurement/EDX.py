from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement


class EDX(SpotMeasurement):
    def __init__(self):
        super().__init__()
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Magnification")
        self.add(label="Dwell time", unit='s')
        self.add(label="Tilt", unit=deg)
        self.add(label="Acquisition mode", field_type=["Point scan", "Line scan", "Mapping"])

        # grey
        self.add(label="Count rate", unit='cps', qudt='NUM-PER-SEC')
        self.add(label="Spot size")
        self.add(label="Working distance", unit='mm')
        self.add(label="Elements included/Peak ID", name='elementsIncluded')
        self.add(label="Background method")

        # green
        self.add(label="Standard used")

        self.sort_fields_by_order_priority()
