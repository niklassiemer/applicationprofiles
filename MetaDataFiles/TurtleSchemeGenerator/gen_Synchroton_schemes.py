from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

Synchro_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Date of preparation", field_type='date'),
    Field(label="Sample storage"),
    Field(label="Pre-treatment"),
    Field(label="Radiation type"),
    Field(label="Beam size", unit=micro+'m'),
    Field(label="Photon flux", unit="Photons/s x 10^"),
    Field(label="Energy bandwidth", unit='%'),
    Field(label="Incoming beam focus", unit=micro+'m**2'),
    Field(label="Deflected beam focus", unit=micro+'m**2'),
    Field(label="Detector"),
    Field(label="Comments", long=True),
]

Synchro_yellow = [
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

Synchro = Scheme("Synchrotron")
Synchro.fields = Synchro_blue
Synchro.write()

Synchro.fields = Synchro_yellow
Synchro.write("Synchrotron_yellow.ttl")

Synchro.fields = Synchro_blue + Synchro_yellow
Synchro.write("Synchrotron_full.ttl")
