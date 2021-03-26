from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.scratch import ScratchBasic, Green, Scratch

scratch = Scheme("Scratch")
scratch.fields = ScratchBasic()
scratch.write("scratch.ttl")

scratch.fields = Green()
scratch.write('scratch_green.ttl')

scratch.fields = Scratch()
scratch.write('scratch_full.ttl')
