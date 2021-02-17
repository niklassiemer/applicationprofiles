from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

EDX_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Instrument used", name="instrument"),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Measurement position"),
    Field(label="Accelerating voltage", unit="kV"),
    Field(label="Magnification"),
    Field(label="Dwell time", unit='s'),
    Field(label="Tilt", unit=deg),
    Field(label="Acquisition mode", field_type="class"),
    Field(label="Comments", long=True),
]

EDX_grey = [
    Field(label="Count rate", unit='cps'),
    Field(label="Spot size"),
    Field(label="Working distance", unit='mm'),
    Field(label="Elements included/Peak ID", name='elementsIncluded'),
    Field(label="Background method")
]

EDX_yellow = [
]

EDX_green = [
    Field(label="Measurement time/date"),
    Field(label="Standard used"),
]

EDX = Scheme("EDX")
EDX.fields = EDX_blue
with open("EDX.ttl", "w") as f:
    f.write(EDX.gen_scheme())

EDX.fields = EDX_blue + EDX_grey
with open('EDX_w_gray.ttl', 'w') as f:
    f.write(EDX.gen_scheme())

EDX.fields = EDX_blue + EDX_green + EDX_grey + EDX_yellow
with open('EDX_full.ttl', 'w', encoding='utf8') as f:
    f.write(EDX.gen_scheme())
