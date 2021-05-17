from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import Software, CompiledSoftware, ComputeEnvironment

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.sample import SampleCoScInE, SamplePreparation
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.simulation import SimUniversal, \
    AtomisticProcessedCoScInE, PostProcessingCoScInE, SimMDCoscine
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.potential import MLPotCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_calc import CalphadCalc
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_db import CalphadDB

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.damask import DamaskCoScInE

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.image_analysis import ImageAnalysis


schemes_to_write = {
    "Software": Software,
    "CompiledSoftware": CompiledSoftware,
    "ComputeEnvironment": ComputeEnvironment,
    "AtomisticSamplePreparation": SamplePreparation,
    "AtomisticSample": SampleCoScInE,
    "AtomisticSimulation": SimUniversal,
    "AtomisticSimulationMD": SimMDCoscine,
    "AtomisticProcessed": AtomisticProcessedCoScInE,
    "AtomisticPostProcessing": PostProcessingCoScInE,
    "MLPotential": MLPotCoScInE,
    "CalphadCalc": CalphadCalc,
    "CalphadDB": CalphadDB,
    "DAMASK": DamaskCoScInE,
    "ImageAnalysis": ImageAnalysis,
}


for key, value in schemes_to_write.items():
    scheme = Scheme(key)
    scheme.fields = value()
    scheme.write()
    scheme.write(file_extension='.txt')
