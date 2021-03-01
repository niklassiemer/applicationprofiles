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
    Field(label="Analyzed elements"),
    Field(label="Isotope"),
    Field(label="Measurement modus"),
    Field(label='Sweeps'),
    Field(label="Replicates"),
    Field(label="Instrument used")
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

ICP_MS = Scheme("ICP_MS")
ICP_MS.fields = blue
ICP_MS.write()

ICP_MS.fields = yellow
ICP_MS.write("ICP_MS_yellow.ttl")

ICP_MS.fields = blue + yellow
ICP_MS.write("ICP_MS_full.ttl")

