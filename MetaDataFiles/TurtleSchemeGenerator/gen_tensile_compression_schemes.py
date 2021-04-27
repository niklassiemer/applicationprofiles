from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tensile_compression import (
    TensileCompressionBasic,
    Green,
    TensileCompression
)

tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = TensileCompressionBasic()
tensile_compression.write("tensile_compression.ttl")

tensile_compression.fields = Green()
tensile_compression.write("tensile_compression_green.ttl")

tensile_compression.fields = TensileCompression()
tensile_compression.write('tensile_compression_full.ttl')
tensile_compression.write(file_extension='txt')
