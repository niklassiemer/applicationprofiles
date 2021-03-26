from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EPMA import EPMABasic, Grey, Green, EPMA

EPMA_scheme = Scheme("EPMA")
EPMA_scheme.fields = EPMABasic()
EPMA_scheme.write()

EPMA_scheme.fields = Green()
EPMA_scheme.write('EPMA_green.ttl')

EPMA_scheme.fields = Grey()
EPMA_scheme.write("EPMA_grey.ttl")

EPMA_scheme.fields = EPMA()
EPMA_scheme.write('EPMA_full.ttl')
