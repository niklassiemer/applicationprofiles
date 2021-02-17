from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

XRD_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Instrument used", name="instrument"),
    Field(label="Specimen type", field_type='class'),
    Field(label="Specimen ID"),
    Field(label="Radiation source"),
    Field(label="Detector"),
    Field(label="Current", unit='mA'),
    Field(label="Voltage", unit='kV'),
    Field(label="Measurement position"),
    Field(label="Scan Mode", field_type='class'),
    Field(label="Incidence angle Omega", unit=deg),
    Field(label="Comments", long=True),
]

XRD_grey = [
    Field(label="Filter"),
    Field(label="Mask size", unit='mm'),
    Field(label="Scan axis", field_type='class'),
    Field(label="Diffraction angle 2Theta", name='diffractionAngle', unit=deg),
    Field(label="Rotation angle phi", unit=deg),
    Field(label="Rotation angle chi", unit=deg),
    Field(label="Number of frames"),
    Field(label="Measurement time", unit='s'),
    Field(label="Start 2Theta", unit=deg),
    Field(label="End 2Theta", unit=deg),
    Field(label="Start Theta", unit=deg),
    Field(label="End Theta", unit=deg),
    Field(label="Fixed 2Theta position", unit=deg),
    Field(label="Step size", unit=deg),
    Field(label="Time per step", unit='s'),
]

XRD_yellow = [
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Preparation routine"),
    Field(label='Pre-treatment', field_type='class'),
    Field(label="Sample storage"),
    Field(label="Immersion Experiment ID")
]

XRD_green = [
    Field(label="Measurement time/date"),
]

XRD = Scheme("XRD")
XRD.fields = XRD_blue
with open("XRD.ttl", "w") as f:
    f.write(XRD.gen_scheme())

XRD.fields = XRD_blue + XRD_grey
with open('XRD_w_gray.ttl', 'w') as f:
    f.write(XRD.gen_scheme())

XRD.fields = XRD_blue + XRD_green + XRD_grey + XRD_yellow
with open('XRD_full.ttl', 'w', encoding='utf8') as f:
    f.write(XRD.gen_scheme())
