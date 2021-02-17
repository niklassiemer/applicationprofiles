from data_scheme import MetaDataSchemes as Scheme, FieldList, SFBFields

sample_blue = SFBFields()
sample_blue.add(label="Parent ID")

sample_yellow = FieldList()
sample_yellow.add(label="Generator ID")
sample_yellow.add(label="Generator frame")  # int
sample_yellow.add(label="Construction method", long=True)  # i.e. pyiron command

sample_green = FieldList()
sample_green.add(label="Chemical formula")  # str
sample_green.add(label="Chemical species")  # list(str)
sample_green.add(label="Number of atoms")  # int
sample_green.add(label="Chemical species count")  # dict

sample_grey = FieldList()
sample_grey.add(label="Defects contained")
sample_grey.add(label="Mechanical treatment")
sample_grey.add(label="Heat treatment")  # aka temperature
sample_grey.add(label="Point group")
sample_grey.add(label="Sublattices")

sample_scheme = Scheme("AtomisticSample")
sample_scheme.fields = sample_blue + sample_yellow + sample_green + sample_grey
sample_scheme.write("AtomisticSample.ttl")
