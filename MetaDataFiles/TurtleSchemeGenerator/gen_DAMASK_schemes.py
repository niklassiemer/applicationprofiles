from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.damask import DamaskCoScInE, Damask

DAMASK = Scheme("DAMASK")
DAMASK.fields = DamaskCoScInE()
DAMASK.write()

DAMASK.fields = Damask()
DAMASK.write("DAMASK_full.ttl")

