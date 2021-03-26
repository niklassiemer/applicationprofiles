from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tensile_compression import TensileCompressionBasic, Grey, Yellow, \
    Green, TensileCompression

tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = TensileCompressionBasic()
tensile_compression.write("tensile_compression.ttl")

tensile_compression.fields = Green()
tensile_compression.write("tensile_compression_green.ttl")

tensile_compression.fields = Grey()
tensile_compression.write("tensile_compression_grey.ttl")

tensile_compression.fields = Yellow()
tensile_compression.write("tensile_compression_yellow.ttl")

tensile_compression.fields = TensileCompression()
tensile_compression.write('tensile_compression_full.ttl')
