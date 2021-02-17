from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

SEM_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Location"),
    Field(label="Instrument used", name="instrument"),
    Field(label="Detector used", name="detector"),
    Field(label="Comments", long=True),
]

SEM_grey = [
    Field(label="Temperature", unit=deg+'C'),
    Field(label="Relative Humidity", unit='%'),
    Field(label="Environmental protection during specimen transfer", name="TestingEnv"),
    Field(label="Environmental gas"),
]

SEM_yellow = [
    Field(label="Preparation routine", long=True),
    Field(label="Preparation Date", field_type="date", long=True),
    Field(label="Sample storage"),
]

SEM_green = [
    Field(label="Accelerating voltage", unit="kV"),
    Field(label="Current", unit="mA"),
    Field(label="Magnification"),
    Field(label="Image width", unit=micro + "m"),
    Field(label="Image size", unit="px(width) x px(height)"),
    Field(label="Acquisition mode", field_type="class"),
    Field(label="Storage Tilt", unit=deg),
]

SEM = Scheme("SEM")
SEM.fields = SEM_blue
SEM.write("SEM.ttl")

SEM.fields = SEM_blue + SEM_grey
SEM.write('SEM_w_gray.ttl')

SEM.fields = SEM_blue + SEM_green + SEM_grey + SEM_yellow
SEM.write('SEM_full.ttl')
