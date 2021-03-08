from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

scratch_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Location"),
    Field(label="Instrument used", name="instrument"),
    Field(label="Tip used", name="tip"),
    Field(label="Comments", long=True),
    Field(label="Scratch crystallographic orientation"),
    Field(label="Scratch surface plane"),
    Field(label="Loading type")
    ]

scratch_grey = [
    Field(label="Relative Humidity", unit='%'),
    Field(label="Temperature", unit="\u00b0C"),
    Field(label="Environmental gas"),
    Field(label="Test date", field_type="date")
]

scratch_yellow = []
scratch_yellow.append(Field(label="Preparation routine", long=True))
scratch_yellow.append(Field(label="Preparation Date", field_type="date", long=True))
scratch_yellow.append(Field(label="Sample storage"))

scratch_green = []
scratch_green.append(Field(label="Type of test"))
scratch_green.append(Field(label="Scratch Length", unit=micro+"m"))
scratch_green.append(Field(label="Scratch Velocity", unit=micro+"m/s"))
scratch_green.append(Field(label="Scratch Orientation", unit=deg))
scratch_green.append(Field(label="Maximum scratch load", unit='mN'))
scratch_green.append(Field(label="Profiling velocity", unit=micro+"m/s"))

scratch = Scheme("Scratch")
scratch.fields = scratch_blue
scratch.write("scratch.ttl")

scratch.fields = scratch_green
scratch.write('scratch_green.ttl')

scratch.fields = scratch_grey
scratch.write('scratch_grey.ttl')

scratch.fields = scratch_yellow
scratch.write('scratch_yellow.ttl')

scratch.fields = scratch_blue + scratch_grey
scratch.write('scratch_w_gray.ttl')

scratch.fields = scratch_blue + scratch_green + scratch_grey + scratch_yellow
scratch.write('scratch_full.ttl')
