from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

TEM_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Pre-treatment"),
    Field(label="Comments", long=True),
    ]

TEM_yellow = [
    Field(label="Specimen ID"),
    Field(label="Pre-Preparation routine", long=True),
    Field(label="Immersion Experiment ID", long=True),
    Field(label="TEM preparation routine"),
    Field(label="TEM preparation date", field_type="date"),
    Field(label="Operator for sample preparation"),
    Field(label="Sample storage location"),
    Field(label="Sample storage conditions"),
]

TEM_green = [
    Field(label="Microscope"),
    Field(label="Experiment Date", field_type='date'),
    Field(label="Accelerating voltage", unit="kV"),
    Field(label="Magnification / Camera length", name='magnefication', unit='mm'),
    Field(label="Electron dose", unit='e/nm**2'),
    Field(label="Dwell time", unit="ms"),
    Field(label="Data dimension"),
    Field(label="1st dimension unit"),
    Field(label="1st dimension pixels"),
    Field(label="1st dimension unit scaling"),
    Field(label="1st dimension starting pixel"),
    Field(label="2nd dimension unit"),
    Field(label="2nd dimension pixels"),
    Field(label="2nd dimension unit scaling"),
    Field(label="2nd dimension starting pixel"),
    ]

TEM = Scheme("TEM")
TEM.fields = TEM_blue
TEM.write("tem.ttl")

TEM.fields = TEM_yellow
TEM.write('tem_yellow.ttl')

TEM.fields = TEM_green
TEM.write("tem_green.ttl")


TEM.fields = TEM_blue + TEM_yellow
TEM.write('tem_w_yellow.ttl')

TEM.fields = TEM_blue + TEM_green
TEM.write('tem_w_green.ttl')

TEM.fields = TEM_blue + TEM_green + TEM_yellow
TEM.write('tem_full.ttl')
