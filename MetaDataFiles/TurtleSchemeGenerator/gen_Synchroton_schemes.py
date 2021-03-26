from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.synchrotron import SynchrotronBasic, Synchrotron

Synchro = Scheme("Synchrotron")
Synchro.fields = SynchrotronBasic()
Synchro.write()

Synchro.fields = Synchrotron()
Synchro.write("Synchrotron_full.ttl")
