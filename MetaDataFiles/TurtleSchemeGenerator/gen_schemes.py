import data_scheme

o = data_scheme.MetaDataSchemes("NanoIndentation")
o.add_field(label="Experiment ID", required=True)
o.add_field(label="Operator", required=True)
o.add_field(label="Specimen ID")
o.add_field(label="Parent sample specimen ID", name="parentSample")
o.add_field(label="Sample Location")
o.add_field(label="Instrument used", name="instrument")
o.add_field(label="Tip used", name="tip")
o.add_field(label="Comments", long=True)
with open("Nano-intendation.ttl", "w") as f:
    f.write(o.gen_scheme())
