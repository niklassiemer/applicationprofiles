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
    Field(label="Mode"),
    Field(label="Alternating Current", unit='mA'),
    Field(label="Alternating Voltage", unit='mV'),
    Field(label="Reference electrode potential", unit='mV(SHE)'),
    Field(label="Counter electrode"),
    Field(label="Comment", long=True)
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

green = [
    Field(label="Potentiostat"),
    Field(label="Time OCP", unit='s'),
    Field(label="Frequency Start", unit='Hz'),
    Field(label="Frequency End", unit='Hz'),
]

grey = [Field(label="Time of measurement", unit='min')]

ElChemImpedSpec = Scheme("ElChemImpedSpec")
ElChemImpedSpec.fields = blue
ElChemImpedSpec.write()

ElChemImpedSpec.fields = yellow
ElChemImpedSpec.write("ElChemImpedSpec_yellow.ttl")

ElChemImpedSpec.fields = green
ElChemImpedSpec.write("ElChemImpedSpec_green.ttl")

ElChemImpedSpec.fields = grey
ElChemImpedSpec.write("ElChemImpedSpec_grey.ttl")

ElChemImpedSpec.fields = blue + yellow + green + grey
ElChemImpedSpec.write("ElChemImpedSpec_full.ttl")


