from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xps import XPS

XPS_scheme = Scheme("XPS")
XPS_scheme.fields = XPS()
XPS_scheme.write("XPS_full.ttl")
XPS_scheme.write(file_extension='txt')
