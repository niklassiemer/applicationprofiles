from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

scratch_blue = [
    Field(label="Experiment ID", required=True),
    Field(label="Operator", required=True),
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Location"),
    Field(label="Instrument used", name="instrument"),
    Field(label="Tip used", name="tip"),
    Field(label="Comments", long=True),
    ]

scratch_grey = []
scratch_grey.append(Field(label="Relative Humidity", unit='%'))
scratch_grey.append(Field(label="Temperature", unit="\u00b0C"))
scratch_grey.append(Field(label="Test date", field_type="date"))

scratch_yellow = []
scratch_yellow.append(Field(label="Preparation routine", long=True))
scratch_yellow.append(Field(label="Preparation Date", field_type="date", long=True))
scratch_yellow.append(Field(label="Sample storage"))

scratch_green = []
scratch_green.append(Field(label="Type of test"))
scratch_green.append(Field(label="Scratch Length", unit="um"))
scratch_green.append(Field(label="Scratch Velocity", unit="um/s"))
scratch_green.append(Field(label="Scratch Orientation", unit='deg'))
scratch_green.append(Field(label="Maximum scratch load", unit='mN'))
scratch_green.append(Field(label="Profiling velocity", unit="um/s"))

scratch = Scheme("Scratch")
scratch.fields = scratch_blue
with open("scratch.ttl", "w") as f:
    f.write(scratch.gen_scheme())

scratch.fields = scratch_blue + scratch_grey
with open('scratch_w_gray.ttl', 'w') as f:
    f.write(scratch.gen_scheme())

scratch.fields = scratch_blue + scratch_green + scratch_grey + scratch_yellow
with open('scratch_full.ttl', 'w') as f:
    f.write(scratch.gen_scheme())
