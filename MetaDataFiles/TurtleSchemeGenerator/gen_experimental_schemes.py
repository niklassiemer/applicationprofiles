from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Sample
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import Polishing, Immersion, Etching, \
    Sample as SamplePreparation
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import ThinFilm

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.apt import AtomProbeTomography
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.icp_ms import IcpMS
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.light_microscope import LightMicroscope
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.micro_pillar import MicroPillar
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.PotentioDynPolar import PotentioDynPolar
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.scratch import Scratch
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SEM import SEM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SIET import SIET
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SKPFM import SKPFM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SVET import SVET
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.synchrotron import Synchrotron
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tem import TEM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tensile_compression import TensileCompression
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xps import XPS
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xrd import XRD
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EBSD import EBSD
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EDX import EDX
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.ElChemImpedSPec import ElChemImpedSpec
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EPMA import EPMA
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.nano_indentation import (NanoIndentation,
                                                                                                 NanoIndentationSRJ,
                                                                                                 NanoIndentationCreep)

schemes_to_write = {
    'SamplePreparation': SamplePreparation,
    "Immersion": Immersion,
    "Etching": Etching,
    "Sample": Sample,
    "Polishing": Polishing,
    "ThinFilm": ThinFilm,
    "Tomography": AtomProbeTomography,  # I would prefer the 'APT' as name, however, 'Tomography' is already in use on CoScInE
    "ICP_MS": IcpMS,
    "LightMicroscope": LightMicroscope,
    "Micropillar": MicroPillar,
    "PotentiodynPolar": PotentioDynPolar,
    "Scratch": Scratch,
    "SEM": SEM,
    "SIET": SIET,
    'SKPFM': SKPFM,
    "SVET": SVET,
    "Synchrotron": Synchrotron,
    "TEM": TEM,
    "TensileCompression": TensileCompression,
    "XPS": XPS,
    "XRD": XRD,
    "EBSD": EBSD,
    "EDX": EDX,
    "ElChemImpedSpec": ElChemImpedSpec,
    "EPMA": EPMA,
    "NanoIndentation": NanoIndentation,
    "NanoIndentationSRJ": NanoIndentationSRJ,
    "NanoIndentationCreep": NanoIndentationCreep,
}


for key, value in schemes_to_write.items():
    scheme = Scheme(key)
    scheme.fields = value()
    scheme.write()
    scheme.write(file_extension='.txt')
