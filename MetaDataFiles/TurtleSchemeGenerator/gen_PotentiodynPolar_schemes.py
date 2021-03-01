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
    Field(label="Potential Measurement"),
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
    Field(label="Time OCP", unit='s'),
    Field(label="Scan velocity", unit="mV/s"),
    Field(label="Scan Start", unit='V'),
    Field(label="Scan End", unit='V'),
    Field(label="Sample area", unit='mm**2'),
    Field(label="IR Compensation", field_type='bool'),
    Field(label="Potentiostat")
]

PotentiodynPolar = Scheme("PotentiodynPolar")
PotentiodynPolar.fields = blue
PotentiodynPolar.write()

PotentiodynPolar.fields = yellow
PotentiodynPolar.write("PotentiodynPolar_yellow.ttl")

PotentiodynPolar.fields = green
PotentiodynPolar.write("PotentiodynPolar_green.ttl")

PotentiodynPolar.fields = blue + yellow + green
PotentiodynPolar.write("PotentiodynPolar_full.ttl")

