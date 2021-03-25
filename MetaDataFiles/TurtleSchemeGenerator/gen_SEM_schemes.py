from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.SEM import SEMBasic, Grey, Yellow, Green, SEM

SEM_scheme = Scheme("SEM")
SEM_scheme.fields = SEMBasic()
SEM_scheme.write("SEM.ttl")

SEM_scheme.fields = Green()
SEM_scheme.write('SEM_green.ttl')

SEM_scheme.fields = Grey()
SEM_scheme.write('SEM_grey.ttl')

SEM_scheme.fields = Yellow()
SEM_scheme.write('SEM_yellow.ttl')

SEM_scheme.fields = SEM()
SEM_scheme.write('SEM_full.ttl')
