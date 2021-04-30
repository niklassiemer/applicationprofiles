from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EDX import EDXBasic, EDXGrey, EDXGreen, EDX

EDX_scheme = Scheme("EDX")
EDX_scheme.fields = EDX()
EDX_scheme.write()
EDX_scheme.write(file_extension='.txt')
