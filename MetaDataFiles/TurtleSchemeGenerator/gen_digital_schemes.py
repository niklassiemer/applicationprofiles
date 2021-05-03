from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import CompiledSoftware, ComputeEnvironment

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.sample import SampleCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.simulation import SimUniversal, \
    AtomisticOutputCoScInE, AtomisticSnapshotCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.potential import MLPotCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_calc import CalphadCalc
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_db import CalphadDB

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.damask import DamaskCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.image_analysis import ImageAnalysis


schemes_to_write = {
    "CompiledSoftware": CompiledSoftware,
    "ComputeEnvironment": ComputeEnvironment,
    "AtomisticSample": SampleCoScInE,
    "Atomistic_simulation": SimUniversal,
    "Atomistic_output": AtomisticOutputCoScInE,
    "Atomistic_snapshot": AtomisticSnapshotCoScInE,
    "ML_potential": MLPotCoScInE,
    "Calphad_calc": CalphadCalc,
    "Calphad_db": CalphadDB,
    "DAMASK": DamaskCoScInE,
    "ImageAnalysis": ImageAnalysis,
}


for key, value in schemes_to_write.items():
    scheme = Scheme(key)
    scheme.fields = value()
    scheme.write()
    scheme.write(file_extension='.txt')
