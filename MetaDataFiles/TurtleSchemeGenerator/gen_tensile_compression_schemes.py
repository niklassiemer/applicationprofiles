from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import SFBFields, FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg


class TensileCompressionBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Location")
        self.add(label="Instrument used", name="instrument")
        self.add(label="Type of loading", field_type="class")


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Relative Humidity", unit='%', qudt="PERCENT_RH")
        self.add(label="Temperature", unit="\u00b0C")
        self.add(label="Test date", field_type="date")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label='Specimen dimensions', unit='mm', long=True)
        self.add(label='Temperature of deformation', unit=deg+'C')
        self.add(label='Strain rate', unit='/s')
        self.add(label='Software used for data analysis')


class TensileCompression(Grey, Green, Yellow, TensileCompressionBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = TensileCompressionBasic()
tensile_compression.write("tensile_compression.ttl")

tensile_compression.fields = Green()
tensile_compression.write("tensile_compression_green.ttl")

tensile_compression.fields = Grey()
tensile_compression.write("tensile_compression_grey.ttl")

tensile_compression.fields = Yellow()
tensile_compression.write("tensile_compression_yellow.ttl")

tensile_compression.fields = TensileCompression()
tensile_compression.write('tensile_compression_full.ttl')
