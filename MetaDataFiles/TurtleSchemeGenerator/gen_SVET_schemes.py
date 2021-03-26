from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SVET import SVET

SVET_scheme = Scheme("SVET")
SVET_scheme.fields = SVET()
SVET_scheme.write("SVET_full.ttl")

