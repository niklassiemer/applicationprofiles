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

sample_prep = Scheme('Sample_preparation')
# sample_prep.fields = SamplePreparation()
# sample_prep.write()
# sample_prep.write(file_extension='.txt')

immersion = Scheme("Immersion")
immersion.fields = Immersion()
immersion.write()
immersion.write(file_extension='.txt')

etching = Scheme("Etching")
etching.fields = Etching()
etching.write()
etching.write(file_extension='.txt')

sample = Scheme("Sample")
sample.fields = Sample()
sample.write()
sample.write(file_extension='.txt')

polish = Scheme("Polishing")
polish.fields = Polishing()
polish.write()
polish.write(file_extension="txt")

thin_film = Scheme("ThinFilm")
thin_film.fields = ThinFilm()
thin_film.write()
thin_film.write(file_extension='txt')

APT = Scheme("APT")
APT.fields = AtomProbeTomography()
APT.write()
APT.write(file_extension='txt')

ICP_MS = Scheme("ICP_MS")
ICP_MS.fields = IcpMS()
ICP_MS.write()
ICP_MS.write(file_extension='txt')

LightMicro_scheme = Scheme("LightMicroscope")
LightMicro_scheme.fields = LightMicroscope()
LightMicro_scheme.write()
LightMicro_scheme.write(file_extension='.txt')

micro_pillar = Scheme("Micropillar")
micro_pillar.fields = MicroPillar()
micro_pillar.write()
micro_pillar.write(file_extension='.txt')

potentio_dyn_polar = Scheme("PotentiodynPolar")
potentio_dyn_polar.fields = PotentioDynPolar()
potentio_dyn_polar.write()
potentio_dyn_polar.write(file_extension='.txt')

scratch = Scheme("Scratch")
scratch.fields = Scratch()
scratch.write()
scratch.write(file_extension='.txt')

SEM_scheme = Scheme("SEM")
SEM_scheme.fields = SEM()
SEM_scheme.write()
SEM_scheme.write(file_extension='.txt')

SIET_scheme = Scheme("SIET")
SIET_scheme.fields = SIET()
SIET_scheme.write()
SIET_scheme.write(file_extension='.txt')

SKPFM_scheme = Scheme('SKPFM')
SKPFM_scheme.fields = SKPFM()
# SKPFM_scheme.coscine_demo = True
SKPFM_scheme.write()
SKPFM_scheme.write(file_extension="txt")

SVET_scheme = Scheme("SVET")
SVET_scheme.fields = SVET()
SVET_scheme.write()
SVET_scheme.write(file_extension='.txt')

Synchro = Scheme("Synchrotron")
Synchro.fields = Synchrotron()
Synchro.write()
Synchro.write(file_extension='.txt')

TEM_scheme = Scheme("TEM")
TEM_scheme.fields = TEM()
TEM_scheme.write()
TEM_scheme.write(file_extension='.txt')

tensile_compression = Scheme("Tensile_Compression")
tensile_compression.fields = TensileCompression()
tensile_compression.write()
tensile_compression.write(file_extension='txt')

XPS_scheme = Scheme("XPS")
XPS_scheme.fields = XPS()
XPS_scheme.write()
XPS_scheme.write(file_extension='txt')

XRD_scheme = Scheme("XRD")
XRD_scheme.fields = XRD()
XRD_scheme.write()
XRD_scheme.write(file_extension='.txt')

EBSD_scheme = Scheme("EBSD")
EBSD_scheme.fields = EBSD()
EBSD_scheme.write()
EBSD_scheme.write(file_extension='.txt')

EDX_scheme = Scheme("EDX")
EDX_scheme.fields = EDX()
EDX_scheme.write()
EDX_scheme.write(file_extension='.txt')

ElChemImpedSpec_scheme = Scheme("ElChemImpedSpec")
ElChemImpedSpec_scheme.fields = ElChemImpedSpec()
ElChemImpedSpec_scheme.write()
ElChemImpedSpec_scheme.write(file_extension='.txt')

EPMA_scheme = Scheme("EPMA")
EPMA_scheme.fields = EPMA()
EPMA_scheme.write()
EPMA_scheme.write(file_extension='txt')

nano_ind_scheme = Scheme("NanoIndentation")
nano_ind_scheme.fields = NanoIndentation()
nano_ind_scheme.write()
nano_ind_scheme.write(file_extension="txt")

nano_ind_scheme_srj = Scheme("NanoIndentationSRJ")
nano_ind_scheme_srj.fields = NanoIndentationSRJ()
nano_ind_scheme_srj.write()
nano_ind_scheme_srj.write(file_extension="txt")

creep_test = Scheme("NanoIndentationCreep")
creep_test.fields = NanoIndentationCreep()
creep_test.write()
creep_test.write(file_extension="txt")

