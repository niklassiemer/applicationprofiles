from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Operator"),
    Field(label="Experiment ID"),
    Field(label="Date of preparation", field_type='date'),
    Field(label='Sample storage'),
    Field(label="Pre-treatment"),
    Field(label="Reference electrode potential", unit='mV(SHE)'),
    Field(label="Counter electrode"),
    Field(label="Ion selective electrode solution"),
    Field(label="Ion selective membrane"),
    Field(label="Reference solution")
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

SIET = Scheme("SIET")
SIET.fields = blue
SIET.write()

SIET.fields = yellow
SIET.write("SIET_yellow.ttl")

SIET.fields = blue + yellow
SIET.write("SIET_full.ttl")

