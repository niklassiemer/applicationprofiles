from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.SVET import Yellow, SVET
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

SVET_scheme = Scheme("SVET")
SVET_scheme.fields = SFBFields()
SVET_scheme.write()

SVET_scheme.fields = Yellow()
SVET_scheme.write("SVET_yellow.ttl")

SVET_scheme.fields = SVET()
SVET_scheme.write("SVET_full.ttl")

