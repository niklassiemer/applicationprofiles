from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.light_microscope import LightMicroscopeBasic, Yellow, LightMicroscope

LightMicro_scheme = Scheme("LightMicroscope")
LightMicro_scheme.fields = LightMicroscopeBasic()
LightMicro_scheme.write()

LightMicro_scheme.fields = Yellow()
LightMicro_scheme.write("LightMicroscope_yellow.ttl")

LightMicro_scheme.fields = LightMicroscope()
LightMicro_scheme.write("LightMicroscope_full.ttl")

