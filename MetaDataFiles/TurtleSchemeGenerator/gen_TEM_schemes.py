from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tem import TEM

TEM_scheme = Scheme("TEM")
TEM_scheme.fields = TEM()
TEM_scheme.write()
TEM_scheme.write(file_extension='.txt')
