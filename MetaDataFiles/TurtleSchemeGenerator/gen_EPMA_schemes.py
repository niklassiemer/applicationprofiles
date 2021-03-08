from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

EPMA_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Instrument used", name="instrument"),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Acquisition mode", field_type="class"),
    Field(label="Comments", long=True),
    Field(label="Elements included/Peak ID", name='elementsIncluded'),
]

EPMA_grey = [
    Field(label="Count rate", unit='cps'),
    Field(label="Spot size"),
    Field(label="Measurement time/date", name="measurementTime"),
    Field(label="Background method")
]

EPMA_yellow = [
]

EPMA_green = [
    Field(label="Accelerating voltage", unit="kV"),
    Field(label="Standard used"),
    Field(label="Magnification"),
    Field(label="Dwell time", unit='s'),
    Field(label="Working distance", unit='mm'),
    Field(label="Tilt", unit=deg),
]

EPMA = Scheme("EPMA")
EPMA.fields = EPMA_blue
EPMA.write()

EPMA.fields = EPMA_green
EPMA.write('EPMA_green.ttl')

EPMA.fields = EPMA_grey
EPMA.write("EPMA_grey.ttl")

EPMA.fields = EPMA_blue + EPMA_green + EPMA_grey + EPMA_yellow
EPMA.write('EPMA_full.ttl')
