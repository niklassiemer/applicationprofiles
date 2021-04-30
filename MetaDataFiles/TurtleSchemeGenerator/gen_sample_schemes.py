from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Sample
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import Polishing, Immersion, Etching, \
    SamplePreparation

sample_prep = Scheme('Sample_preparation')
sample_prep.fields = SamplePreparation()
sample_prep.write()
sample_prep.write(file_extension='.txt')

immersion = Scheme("Immersion")
immersion.fields = Immersion()
immersion.write()
immersion.write(file_extension='.txt')

etching = Scheme("Etching")
etching.fields = Etching()
etching.write()
etching.write(file_extension='.txt')

sample = Scheme("Sample")
sample.fields = Sample()
sample.write()
sample.write(file_extension='.txt')

polish = Scheme("Polishing")
polish.fields = Polishing()
polish.write()
polish.write(file_extension="txt")
