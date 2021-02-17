from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

EBSD_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample location"),
    Field(label="Grit 1"),
    Field(label="Solvent grit 1"),
    Field(label="Grit 2"),
    Field(label="Solvent grit 2"),
    Field(label="Grit material"),
    Field(label="Polishing Suspension", unit=micro+'m'),
    Field(label="Material Suspension"),
    Field(label="Fine polishing Suspension"),
    Field(label="Solvent Polishing"),
    Field(label="Operator", name="etchingOperator"),
    Field(label="Etchant"),
    Field(label="Parameter"),
    Field(label="Corrosion", field_type="bool"),
    Field(label="Immersion Experiment ID"),
    Field(label="Instrument used"),
    Field(label='Detectors used'),
    Field(label="Comments", long=True),
    ]

EBSD_yellow = [
    Field(label="Specimen ID"),
    Field(label="Preparation routine", long=True),
    Field(label="Sample storage"),
    Field(label="Date of preparation", field_type='date'),
    Field(label="Etching routine"),
]

EBSD_green = [
    Field(label="Accelerating voltage", unit="kV"),
    Field(label="Current", unit="nA"),
    Field(label="Magnification"),
    Field(label="Step size", unit=micro+"m"),
    Field(label="Raster size", unit=micro+"m(width) x "+micro+"m(height)"),
    Field(label="Acquisition mode", field_type="class"),
    Field(label="No. of points"),
    Field(label="Working distance"),
    Field(label="Tilt angle", unit=deg),
    Field(label="Software used for data analysis"),
    ]

EBSD_grey = [
    Field(label="Temperature", unit=deg+'C'),
    Field(label="Relative Humidity", unit='%'),
    Field(label="Temperature"),
    Field(label="Environmental protection during specimen testing", name="TestingEnv"),
    Field(label="Environmental gas"),
    Field(label="Test date", field_type="date"),
]

EBSD = Scheme("EBSD")
EBSD.fields = EBSD_blue
EBSD.write("ebsd.ttl")

EBSD.fields = EBSD_blue + EBSD_yellow
EBSD.write('ebsd_w_yellow.ttl')

EBSD.fields = EBSD_blue + EBSD_green
EBSD.write('ebsd_w_green.ttl')

EBSD.fields = EBSD_blue + EBSD_green + EBSD_yellow
EBSD.write('ebsd_full.ttl')
