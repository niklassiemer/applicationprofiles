from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.micro_pillar import MicroPillarBasic, Grey, \
    Green, \
    MicroPillar

micro_pillar = Scheme("Micropillar")
micro_pillar.fields = MicroPillarBasic()
micro_pillar.write("micropillar.ttl")

micro_pillar.fields = Grey()
micro_pillar.write('micropillar_grey.ttl')

micro_pillar.fields = Green()
micro_pillar.write('micropillar_green.ttl')


micro_pillar.fields = MicroPillar()
micro_pillar.write('micropillar_full.ttl')
