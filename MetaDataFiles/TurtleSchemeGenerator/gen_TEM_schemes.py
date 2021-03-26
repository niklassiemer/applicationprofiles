from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tem import TEMBasic, Yellow, Green, TEM

TEM_scheme = Scheme("TEM")
TEM_scheme.fields = TEMBasic()
TEM_scheme.write("tem.ttl")

TEM_scheme.fields = Yellow()
TEM_scheme.write('tem_yellow.ttl')

TEM_scheme.fields = Green()
TEM_scheme.write("tem_green.ttl")

TEM_scheme.fields = TEM()
TEM_scheme.write('tem_full.ttl')
