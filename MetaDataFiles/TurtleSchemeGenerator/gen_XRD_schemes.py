from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xrd import XRD

XRD_scheme = Scheme("XRD")
XRD_scheme.fields = XRD()
XRD_scheme.write()
XRD_scheme.write(file_extension='.txt')
