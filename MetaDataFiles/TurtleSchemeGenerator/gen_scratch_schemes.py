from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.scratch import Scratch

scratch = Scheme("Scratch")
scratch.fields = Scratch()
scratch.write()
scratch.write(file_extension='.txt')
