from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.PotentioDynPolar import PotentioDynPolar

potentio_dyn_polar = Scheme("PotentiodynPolar")
potentio_dyn_polar.fields = PotentioDynPolar()
potentio_dyn_polar.write()
potentio_dyn_polar.write(file_extension='.txt')
