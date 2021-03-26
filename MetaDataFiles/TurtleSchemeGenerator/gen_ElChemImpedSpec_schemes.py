from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.ElChemImpedSPec import ElChemImpedSpecBasic, \
    Green, Grey, \
    ElChemImpedSpec
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import ElChemImpedSpecYellow

ElChemImpedSpec_scheme = Scheme("ElChemImpedSpec")
ElChemImpedSpec_scheme.fields = ElChemImpedSpecBasic()
ElChemImpedSpec_scheme.write()

ElChemImpedSpec_scheme.fields = ElChemImpedSpecYellow()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_yellow.ttl")

ElChemImpedSpec_scheme.fields = Green()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_green.ttl")

ElChemImpedSpec_scheme.fields = Grey()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_grey.ttl")

ElChemImpedSpec_scheme.fields = ElChemImpedSpec()
ElChemImpedSpec_scheme.write("ElChemImpedSpec_full.ttl")


