from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SKPFM import SKPFM

SKPFM_scheme = Scheme('SKPFM')
SKPFM_scheme.fields = SKPFM()
#SKPFM_scheme.coscine_demo = True
SKPFM_scheme.write()
SKPFM_scheme.write(file_extension="txt")
