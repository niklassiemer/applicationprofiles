from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EBSD import EBSDBasic, EBSDGreen, EBSDGrey, EBSD

EBSD_scheme = Scheme("EBSD")
EBSD_scheme.fields = EBSDBasic()
EBSD_scheme.write("ebsd.ttl")

EBSD_scheme.fields = EBSDGrey()
EBSD_scheme.write("ebsd_grey.ttl")

EBSD_scheme.fields = EBSDGreen()
EBSD_scheme.write("ebsd_green.ttl")

EBSD_scheme.fields = EBSD()
EBSD_scheme.write('ebsd_full.ttl')
EBSD_scheme.write(file_extension='.txt')
