from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.PotentioDynPolar import PotentioDynPolarBasic, \
    Green, \
    PotentioDynPolar
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import PotentioDynPolarYellow

potentio_dyn_polar = Scheme("PotentiodynPolar")
potentio_dyn_polar.fields = PotentioDynPolarBasic()
potentio_dyn_polar.write()

potentio_dyn_polar.fields = PotentioDynPolarYellow()
potentio_dyn_polar.write("PotentiodynPolar_yellow.ttl")

potentio_dyn_polar.fields = Green()
potentio_dyn_polar.write("PotentiodynPolar_green.ttl")

potentio_dyn_polar.fields = PotentioDynPolar()
potentio_dyn_polar.write("PotentiodynPolar_full.ttl")

