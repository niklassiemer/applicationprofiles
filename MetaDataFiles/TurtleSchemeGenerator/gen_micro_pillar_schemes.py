from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.micro_pillar import MicroPillar

micro_pillar = Scheme("Micropillar")
micro_pillar.fields = MicroPillar()
micro_pillar.write()
micro_pillar.write(file_extension='.txt')
