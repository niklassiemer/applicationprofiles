from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tensile_compression import TensileCompression

tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = TensileCompression()
tensile_compression.write()
tensile_compression.write(file_extension='txt')
