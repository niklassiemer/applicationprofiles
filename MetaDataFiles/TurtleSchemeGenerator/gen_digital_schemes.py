from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import CompiledSoftware, ComputeEnvironment

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.sample import SampleCoScInE, SamplePreparation
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.simulation import SimUniversal, \
    AtomisticSnapshotCoScInE, PostProcessingCoScInE, SimMDCoscine
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.potential import MLPotCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_calc import CalphadCalc
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_db import CalphadDB

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.damask import DamaskCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.image_analysis import ImageAnalysis


schemes_to_write = {
    "CompiledSoftware": CompiledSoftware,
    "ComputeEnvironment": ComputeEnvironment,
    "SamplePreparation": SamplePreparation,
    "AtomisticSample": SampleCoScInE,
    "Atomistic_simulation": SimUniversal,
    "Atomistic_MD": SimMDCoscine,
    "Atomistic_snapshot": AtomisticSnapshotCoScInE,
    "PostProcessing": PostProcessingCoScInE,
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
