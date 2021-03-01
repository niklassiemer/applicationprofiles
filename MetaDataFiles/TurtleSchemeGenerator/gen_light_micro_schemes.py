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
    Field(label="Instrument used"),
    Field(label="Position sample"),
    Field(label="Filter"),
    Field(label="Magnification"),
    Field(label="Scale", unit=micro+'m/px')
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

LightMicro = Scheme("LightMicroscope")
LightMicro.fields = blue
LightMicro.write()

LightMicro.fields = yellow
LightMicro.write("LightMicroscope_yellow.ttl")

LightMicro.fields = blue + yellow
LightMicro.write("LightMicroscope_full.ttl")

