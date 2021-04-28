from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.ElChemImpedSPec import ElChemImpedSpecBasic, \
    Green,  \
    ElChemImpedSpec

ElChemImpedSpec_scheme = Scheme("ElChemImpedSpec")
ElChemImpedSpec_scheme.fields = ElChemImpedSpecBasic()
ElChemImpedSpec_scheme.write()

ElChemImpedSpec_scheme.fields = Green()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_green.ttl")

ElChemImpedSpec_scheme.fields = ElChemImpedSpec()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_full.ttl")
ElChemImpedSpec_scheme.write(file_extension='.txt')


