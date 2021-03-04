from data_scheme import MetaDataSchemes as Scheme, \
    MetaDataField as Field, \
    DropdownList, \
    SFBFields

micro = "\u03bc"
deg = "\u00b0"

KPFM_dropdown = DropdownList(label="KPFM mode", options=['AM', 'FM'])
applied_offset_V_dropdown = DropdownList(label="Applied offset voltage", options=['sample', 'tip'])

blue = [
#    Field(label="Operator"),
#    Field(label="Experiment ID"),
    Field(label="Date of preparation", field_type='date'),
    Field(label='Sample storage'),
    Field(label="Pre-treatment"),
    Field(label='AFM mode'),
    Field(label="KPFM mode", field_type=KPFM_dropdown),
    Field(label="Tip name"),
    Field(label="Working distance", unit='nm', other_relations={"qudt:Unit": "unit:NanoM"}),
    Field(label="Scan velocity", unit='Hz', other_relations={"qudt:Unit": "unit:HZ"}),
    Field(label="Tip offset voltage", unit='V', other_relations={"qudt:Unit": "unit:V"}),
    Field(label="Applied offset voltage", field_type=['sample', 'tip']),  # applied_offset_V_dropdown),
    Field(label="Tip alternating Voltage", unit='V', other_relations={"qudt:Unit": "unit:V"}),
    Field(label="Scan area", unit="nm x nm", other_relations={'#': "ideally this would be two float inputs",
                                                              "#qudt:Unit": "unit:NanoM2  Does not yet exist"}),
    Field(label="Reference"),
    Field(label="Experiment condition", long=True),
#    Field(label="Comments", long=True)
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

basic_scheme = Scheme("SKPFM/SFB_basic")
basic_scheme.fields = SFBFields()

sample_origin_scheme = Scheme("SKPFM/SampleOrigin", extends=basic_scheme)
sample_origin_scheme.fields = yellow

SKPFM_scheme = Scheme("SKPFM", extends=sample_origin_scheme)
SKPFM_scheme.fields = blue

SKPFM_scheme.write()
