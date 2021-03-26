from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xrd import XRDBasic, Grey, Green, XRD

XRD_scheme = Scheme("XRD")
XRD_scheme.fields = XRDBasic()
XRD_scheme.write("XRD.ttl")

XRD_scheme.fields = Green()
XRD_scheme.write('XRD_green.ttl')

XRD_scheme.fields = Grey()
XRD_scheme.write('XRD_grey.ttl')

XRD_scheme.fields = XRD()
XRD_scheme.write('XRD_full.ttl')
