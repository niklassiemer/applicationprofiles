from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Sample
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EBSD import EBSD
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EDX import EDX
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.EPMA import EPMA
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.ElChemImpedSPec import ElChemImpedSpec
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.PotentioDynPolar import PotentioDynPolar
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SEM import SEM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SIET import SIET
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SKPFM import SKPFM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SVET import SVET
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.apt import AtomProbeTomography
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.icp_ms import IcpMS
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.light_microscope import LightMicroscope
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.micro_pillar import MicroPillar
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.nano_indentation import NanoIndentation, \
    NanoIndentationSRJ, NanoIndentationCreep
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.scratch import Scratch
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.synchrotron import Synchrotron
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tem import TEM
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.tensile_compression import TensileCompression
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xps import XPS
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.xrd import XRD
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import Polishing, Immersion, Etching, \
    Sample as SamplePreparation, ThinFilm

from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import Software, CompiledSoftware, ComputeEnvironment
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.sample import SampleCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.simulation import SimUniversal, \
    AtomisticOutputCoScInE, AtomisticSnapshotCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.potential import MLPotCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_db import CalphadDB
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_calc import CalphadCalc
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.image_analysis import ImageAnalysis
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.damask import DamaskCoScInE


# Break MRO issues:
class C0(ThinFilm, Immersion):
    pass


class C1(C0, SamplePreparation, Sample):
    pass


class C2(C1, Polishing):
    pass


class C3(C2, AtomProbeTomography, Etching):
    pass


class C4(C3, IcpMS, LightMicroscope, MicroPillar, PotentioDynPolar):
    pass


class C5(C4, Scratch, SEM, SIET, SKPFM, SVET, Synchrotron, TEM, TensileCompression, XPS):
    pass


class C6(C5, XRD, EBSD, EDX, ElChemImpedSpec, EPMA, NanoIndentation, NanoIndentationSRJ):
    pass


# Finally
class ExpMasterScheme(C6, NanoIndentationCreep):
    pass


class S1(SampleCoScInE, SimUniversal, AtomisticOutputCoScInE, AtomisticSnapshotCoScInE, MLPotCoScInE, CompiledSoftware):
    pass


class S2(S1, Software,  ComputeEnvironment):
    pass


class SimMasterScheme(S2, DamaskCoScInE, ImageAnalysis, CalphadCalc, CalphadDB):
    pass


class MasterScheme(ExpMasterScheme, SimMasterScheme):
    pass


def remove_duplications(term_list):
    sfb_terms_ids = [item.split()[0] for item in term_list]

    unique_term_ids = []
    duplicated_idx = {}
    failure = False
    msg = ""

    for n, ID in enumerate(sfb_terms_ids):
        if ID not in unique_term_ids:
            unique_term_ids.append(ID)
            if n+1 < len(sfb_terms_ids):
                duplication_idxs = []
                for n2, ID2 in enumerate(sfb_terms_ids[n+1:]):
                    if ID == ID2:
                        duplication_idxs.append(n+n2+1)
                if len(duplication_idxs) > 0:
                    duplicated_idx[ID] = [n] + duplication_idxs

    for key, value in duplicated_idx.items():
        different_output = [term_list[value[0]]]
        for indx in value[1:]:
            if term_list[value[0]] != term_list[indx] and term_list[indx] not in different_output:
                different_output.append(term_list[indx])
        if len(different_output) > 1:
            failure = True
            msg += f'Not matching entries for {key}! \n'
            for output in different_output:
                msg += "-----  \n "
                msg += output + "\n "

    if failure:
        raise ValueError("Not matching Entries found: \n" + msg)

    return list(set(term_list))


MasterScheme = MasterScheme()

sfb_terms = [field.ttl_term_str for field in MasterScheme if field.ttl_term_str != ""]
sfb_terms = remove_duplications(sfb_terms)
sfb_terms.sort()

preamble = '''@base  <http://purl.org/coscine/terms/sfb1394/> .
@prefix sfb1394: <http://purl.org/coscine/terms/sfb1394#> .

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<http://purl.org/coscine/terms/sfb1394/>
dcterms:publisher <http://www.itc.rwth-aachen.de/> ;
dcterms:license <http://spdx.org/licenses/CC-BY-4.0> ;
dcterms:rights "Copyright © 2020 RWTH Aachen University" ;
dcterms:title "SFB1394 Metadata"@en 
.
\n'''

with open("sfb1394_terms.ttl", 'w', encoding='utf8') as f:
    f.write(preamble)
    for term in sfb_terms:
        f.write(term)
