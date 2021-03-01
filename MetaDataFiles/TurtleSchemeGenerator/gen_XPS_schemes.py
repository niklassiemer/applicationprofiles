from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

XPS_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Date of preparation", field_type='date'),
    Field(label="Sample storage"),
    Field(label="Pre-treatment"),
    Field(label="Energy range start", unit='eV'),
    Field(label="Energy range end", unit='eV'),
    Field(label="Etching source"),
    Field(label="Etching energy"),
    Field(label="Etching duration"),
    Field(label="Etching power"),
    Field(label="Anode material"),
    Field(label="Anode power", unit='W'),
    Field(label="Anode voltage", unit='kV'),
    Field(label="Pass energy", unit='eV'),
    Field(label="Working pressure", unit='lg(Torr)'),
    Field(label="Energy resolution", unit='eV'),
    Field(label="Comments", long=True),
]

XPS_yellow = [
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

XPS = Scheme("XPS")
XPS.fields = XPS_blue
XPS.write()

XPS.fields = XPS_yellow
XPS.write("XPS_yellow.ttl")

XPS.fields = XPS_blue + XPS_yellow
XPS.write("XPS_full.ttl")
