from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class SVET(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")
        self.add(label="Vibrating electrode")
        self.add(label="Tip length", unit=micro + 'm')
        self.add(label="Vibrating electrode frequency", unit='Hz')
        self.add(label="Vibrating electrode amplitude", unit='nm')
        self.add(label="Working distance", unit=micro + 'm')
        self.sort_fields_by_order_priority()
