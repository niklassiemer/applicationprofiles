from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EPMA import EPMA

EPMA_scheme = Scheme("EPMA")
EPMA_scheme.fields = EPMA()
EPMA_scheme.write()
EPMA_scheme.write(file_extension='txt')
