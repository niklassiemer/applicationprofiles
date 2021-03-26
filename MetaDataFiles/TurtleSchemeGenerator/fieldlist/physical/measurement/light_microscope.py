from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class LightMicroscope(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Position sample"),
        self.add(label="Filter"),
        self.add(label="Magnification"),
        self.add(label="Scale", unit=micro+'m/px', qudt='MicroM-PER-NUM')
        self.sort_fields_by_order_priority()