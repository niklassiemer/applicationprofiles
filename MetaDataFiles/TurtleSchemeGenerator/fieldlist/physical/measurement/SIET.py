from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class SIET(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")
        self.add(label="Ion selective electrode solution")
        self.add(label="Ion selective membrane")
        self.add(label="Reference solution")
        self.sort_fields_by_order_priority()
