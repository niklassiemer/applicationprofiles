from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class EPMA(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Acquisition mode", field_type=["Point scan", "Line scan", "Mapping"])
        self.add(label="Elements included/Peak ID", name='peakID')

        # grey
        self.add(label="Count rate", unit='cps', qudt='NUM-PER-SEC')
        self.add(label="Spot size")
        self.add(label="Background method")

        # green
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Standard used")
        self.add(label="Magnification")
        self.add(label="Dwell time", unit='s')
        self.add(label="Working distance", unit='mm')
        self.add(label="Tilt", unit=deg)

        self.sort_fields_by_order_priority()
