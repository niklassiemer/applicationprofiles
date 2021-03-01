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
    Field(label="Vibrating electrode"),
    Field(label="Tip length", unit=micro+'m'),
    Field(label="Vibrating electrode frequency", unit='Hz'),
    Field(label="Vibrating electrode amplitude", unit='nm'),
    Field(label="Working distance", unit=micro+'m'),
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

SVET = Scheme("SVET")
SVET.fields = blue
SVET.write()

SVET.fields = yellow
SVET.write("SVET_yellow.ttl")

SVET.fields = blue + yellow
SVET.write("SVET_full.ttl")

