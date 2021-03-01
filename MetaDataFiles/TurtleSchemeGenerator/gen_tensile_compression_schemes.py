from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Location"),
    Field(label="Instrument used", name="instrument"),
    Field(label="Type of loading", field_type="class"),
    Field(label="Comments", long=True),
    ]

grey = []
grey.append(Field(label="Relative Humidity", unit='%'))
grey.append(Field(label="Temperature", unit="\u00b0C"))
grey.append(Field(label="Test date", field_type="date"))

yellow = []
yellow.append(Field(label="Preparation routine", long=True))
yellow.append(Field(label="Preparation Date", field_type="date", long=True))
yellow.append(Field(label="Sample storage"))

green = [
    Field(label='Specimen dimensions', unit='mm', long=True),
    Field(label='Temperature of deformation', unit=deg+'C'),
    Field(label='Strain rate', unit='/s'),
    Field(label='Software used for data analysis')
]

tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = blue
tensile_compression.write("tensile_compression.ttl")

tensile_compression.fields = green
tensile_compression.write("tensile_compression_green.ttl")

tensile_compression.fields = grey
tensile_compression.write("tensile_compression_grey.ttl")

tensile_compression.fields = yellow
tensile_compression.write("tensile_compression_yellow.ttl")

tensile_compression.fields = blue + green + grey + yellow
tensile_compression.write('tensile_compression_full.ttl')
