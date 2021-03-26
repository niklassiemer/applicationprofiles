from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.sample import SampleBasic, ParentSample, Sample
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import Polish, Immersion, Etching

parent = Scheme('Parent_sample')
parent.fields = ParentSample()
parent.write()

sample_info = Scheme('Sample_info')
sample_info.fields = SampleBasic()
sample_info.write()

sample_prep = Scheme('Sample_preparation')
sample_prep.fields = Polish()
sample_prep.write()

immersion = Scheme("Immersion")
immersion.fields = Immersion()
immersion.write()

etching = Scheme("Etching")
etching.fields = Etching()
etching.write()

sample = Scheme("Sample")
sample.fields = Sample()
sample.write()

