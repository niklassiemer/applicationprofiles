from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SIET import SIET

SIET_scheme = Scheme("SIET")
SIET_scheme.fields = SIET()
SIET_scheme.write()
SIET_scheme.write(file_extension='.txt')

