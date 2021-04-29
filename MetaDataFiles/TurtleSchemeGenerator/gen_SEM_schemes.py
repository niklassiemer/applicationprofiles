from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SEM import SEM

SEM_scheme = Scheme("SEM")
SEM_scheme.fields = SEM()
SEM_scheme.write()
SEM_scheme.write(file_extension='.txt')

