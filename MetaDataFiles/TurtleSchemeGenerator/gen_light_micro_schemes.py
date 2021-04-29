from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.light_microscope import LightMicroscope

LightMicro_scheme = Scheme("LightMicroscope")
LightMicro_scheme.fields = LightMicroscope()
LightMicro_scheme.write()
LightMicro_scheme.write(file_extension='.txt')
