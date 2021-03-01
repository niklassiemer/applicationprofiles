from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field
from data_scheme import DropdownList

micro = "\u03bc"
deg = "\u00b0"

KPFM_dropdown = DropdownList(label="KPFM mode", options=['AM', 'FM'])
applied_offset_V_dropdown = DropdownList(label="Applied offset voltage", options=['sample', 'tip'])

blue = [
    Field(label="Operator"),
    Field(label="Experiment ID"),
    Field(label="Date of preparation", field_type='date'),
    Field(label='Sample storage'),
    Field(label="Pre-treatment"),
    Field(label='AFM mode'),
    Field(label="KPFM mode", field_type=KPFM_dropdown),
    Field(label="Tip name"),
    Field(label="Working distance", unit='nm'),
    Field(label="Scan velocity", unit='Hz'),
    Field(label="Tip offset voltage", unit='V'),
    Field(label="Applied offset voltage", field_type=applied_offset_V_dropdown),
    Field(label="Tip alternating Voltage", unit='V'),
    Field(label="Scan area", unit="nm x nm"),
    Field(label="Reference"),
    Field(label="Experiment condition", long=True),
    Field(label="Comments", long=True)
]

yellow = [
    Field(label="Parent sample specimen ID"),
    Field(label="Specimen ID"),
    Field(label="Preparation routine"),
    Field(label="Immersion Experiment ID")
]

SKPFM = Scheme("SKPFM")
SKPFM.fields = blue
SKPFM.write()

SKPFM.fields = yellow
SKPFM.write("SKPFM_yellow.ttl")

SKPFM.fields = blue + yellow
SKPFM.write("SKPFM_full.ttl")

