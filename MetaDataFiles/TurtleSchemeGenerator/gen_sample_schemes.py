from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue_parent = [
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Designation"),
    Field(label="Chemical composition"),
    Field(label="Production batch designation"),
]

blue_sample = [
    Field(label="Specimen ID"),
    Field(label="Parent sample specimen ID", name="parentSample"),
    Field(label="Sample Location"),
    ]

blue_sample_preparation = [
    Field(label="Preparation routine"),
    Field(label="Grit 1"),
    Field(label="Solvent grit 1"),
    Field(label="Grit 2"),
    Field(label="Solvent grit 2"),
    Field(label="Grit material"),
    Field(label="Polishing Suspension", unit=micro + 'm'),
    Field(label="Material Suspension"),
    Field(label="Solvent"),
]

blue_immersion = [
    Field(label='Immersion experiment ID'),
    Field(label='Immersion experiment routine'),
    Field(label="Electrolyte pH"),
    Field(label="Electrolyte condition"),
    Field(label="Flow rate", unit="ml/h"),
    Field(label="Revolutions per minute", unit='rpm'),
    Field(label="Volume", unit='ml')
]
grey_immersion = [Field(label="Temperature", unit=deg+'C')]

blue_etching = [
    Field(label="Etching routine"),
    Field(label="Operator"),
    Field(label="Chemicals"),
    Field(label="Duration", unit="s")
]

parent = Scheme('Parent_sample')
parent.fields = blue_parent
parent.write()

sample_info = Scheme('Sample_info')
sample_info.fields = blue_sample
sample_info.write()

sample_prep = Scheme('Sample_preparation')
sample_prep.fields = blue_sample_preparation
sample_prep.write()

immersion = Scheme("Immersion")
immersion.fields = blue_immersion
immersion.write()

immersion.fields = grey_immersion
immersion.write("Immersion_grey.ttl")

etching = Scheme("Etching")
etching.fields = blue_etching
etching.write()

sample = Scheme("Sample")
sample.fields = blue_parent + blue_sample + blue_sample_preparation + blue_etching + blue_immersion
sample.write()

# same as Immersion_grey
# sample.fields = grey_immersion
# sample.write("Sample_grey.ttl")

sample.fields = blue_parent + blue_sample + blue_sample_preparation + blue_etching + blue_immersion + grey_immersion
sample.write("Sample_full.ttl")
