from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EBSD import EBSD

EBSD_scheme = Scheme("EBSD")
EBSD_scheme.fields = EBSD()
EBSD_scheme.write()
EBSD_scheme.write(file_extension='.txt')
