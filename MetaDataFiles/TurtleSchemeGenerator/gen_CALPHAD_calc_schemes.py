from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.calphad_calc import CalphadCalc

Calphad_calc = Scheme("Calphad_calc")
Calphad_calc.fields = CalphadCalc()
Calphad_calc.write()
