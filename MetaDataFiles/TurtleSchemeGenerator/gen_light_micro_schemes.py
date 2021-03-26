from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.light_microscope import LightMicroscopeBasic, \
    LightMicroscope
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import LightMicroscopeYellow

LightMicro_scheme = Scheme("LightMicroscope")
LightMicro_scheme.fields = LightMicroscopeBasic()
LightMicro_scheme.write()

LightMicro_scheme.fields = LightMicroscopeYellow()
LightMicro_scheme.write("LightMicroscope_yellow.ttl")

LightMicro_scheme.fields = LightMicroscope()
LightMicro_scheme.write("LightMicroscope_full.ttl")

