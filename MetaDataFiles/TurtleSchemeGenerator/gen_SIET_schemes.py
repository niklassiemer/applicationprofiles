from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.SIET import SIETBasic, Yellow, SIET

SIET_scheme = Scheme("SIET")
SIET_scheme.fields = SIETBasic()
SIET_scheme.write()

SIET_scheme.fields = Yellow()
SIET_scheme.write("SIET_yellow.ttl")

SIET_scheme.fields = SIET()
SIET_scheme.write("SIET_full.ttl")

