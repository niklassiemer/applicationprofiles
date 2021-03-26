from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class SIETBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")
        self.add(label="Ion selective electrode solution")
        self.add(label="Ion selective membrane")
        self.add(label="Reference solution")


class SIET(SIETBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()