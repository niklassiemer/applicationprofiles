from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.ElChemImpedSPec import ElChemImpedSpec

ElChemImpedSpec_scheme = Scheme("ElChemImpedSpec")
ElChemImpedSpec_scheme.fields = ElChemImpedSpec()
ElChemImpedSpec_scheme.write()
ElChemImpedSpec_scheme.write(file_extension='.txt')


