from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xps import XPSBasic, Yellow, XPS

XPS_scheme = Scheme("XPS")
XPS_scheme.fields = XPSBasic()
XPS_scheme.write()

XPS_scheme.fields = Yellow()
XPS_scheme.write("XPS_yellow.ttl")

XPS_scheme.fields = XPS()
XPS_scheme.write("XPS_full.ttl")
