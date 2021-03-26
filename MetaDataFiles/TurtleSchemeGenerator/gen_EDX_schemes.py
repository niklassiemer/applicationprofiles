from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EDX import EDXBasic, EDXGrey, EDXGreen, EDX

EDX_scheme = Scheme("EDX")
EDX_scheme.fields = EDXBasic()
EDX_scheme.write("EDX.ttl")

EDX_scheme.fields = EDXGreen()
EDX_scheme.write('EDX_green.ttl')

EDX_scheme.fields = EDXGrey()
EDX_scheme.write("EDX_grey.ttl")

EDX_scheme.fields = EDX()
EDX_scheme.write('EDX_full.ttl')
