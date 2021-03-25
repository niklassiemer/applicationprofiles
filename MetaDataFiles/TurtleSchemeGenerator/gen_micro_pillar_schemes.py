from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import SFBFields, FieldList


class MicroPillarBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Location")
        self.add(label="Instrument used", name="instrument")
        self.add(label="Tip used", name="tip")


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Relative Humidity", unit='%', qudt='PERCENT_RH')
        self.add(label="Environmental protection during specimen testing", name="TestingEnv")
        self.add(label="Environmental gas")
        self.add(label="Test duration")
        self.add(label="Test date", field_type="date")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")
        self.add(label="Pillar Orientation", long=True)


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Type of test")
        self.add(label="Tip ID")
        self.add(label="Diamond area function")
        self.add(label="Date of Calibration", field_type="date")
        self.add(label="Frame stiffness", unit='N/m')
        self.add(label="Target load", unit="mN")
        self.add(label="Target depth", unit="nm")
        self.add(label="Target strain rate", unit='/s')
        self.add(label="Target loading rate", unit='mN/s')
        self.add(label="Continuous stiffness measurement", field_type='bool')
        self.add(label="Drift correction enabled", field_type="bool")
        self.add(label="Sample temperature", unit="\u00b0C")
        self.add(label="Tip temperature", unit="\u00b0C")


class MicroPillar(Grey, Green, Yellow, MicroPillarBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


micro_pillar = Scheme("Micropillar")
micro_pillar.fields = MicroPillarBasic()
micro_pillar.write("micropillar.ttl")

micro_pillar.fields = Grey()
micro_pillar.write('micropillar_grey.ttl')

micro_pillar.fields = Yellow()
micro_pillar.write('micropillar_yellow.ttl')

micro_pillar.fields = Green()
micro_pillar.write('micropillar_green.ttl')


micro_pillar.fields = MicroPillar()
micro_pillar.write('micropillar_full.ttl')
