from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.icp_ms import IcpMS

ICP_MS = Scheme("ICP_MS")
ICP_MS.fields = IcpMS()
ICP_MS.write("ICP_MS_full.ttl")
ICP_MS.write(file_extension='txt')

