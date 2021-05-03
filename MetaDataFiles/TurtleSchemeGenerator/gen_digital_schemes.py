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


comp_software_scheme = Scheme("CompiledSoftware")
comp_software_scheme.fields = CompiledSoftware()
comp_software_scheme.write()
comp_software_scheme.write(file_extension='txt')

comp_env = Scheme("ComputeEnvironment")
comp_env.fields = ComputeEnvironment()
comp_env.write()
comp_env.write(file_extension='txt')

sample_scheme = Scheme("AtomisticSample")
sample_scheme.fields = SampleCoScInE()
sample_scheme.write()
sample_scheme.write(file_extension='txt')

# lammps_min = Scheme("AtomisticSim_LammpsMin")
# lammps_min.fields = LammpsMin()
# lammps_min.write()
#
# lammps_md = Scheme("AtomisticSim_LammpsMD")
# lammps_md.fields = SimUniversal() + SimLammps() + SimMD()
# lammps_md.write()
#
# lammps_deform = Scheme("AtomisticSim_LammpsDeformMD")
# lammps_deform.fields = lammps_md.fields.copy() + SimDeform()
# lammps_deform.write()
#
# lammps_indent = Scheme("AtomisticSim_LammpsIndentMD")
# lammps_indent.fields = lammps_md.fields.copy() + SimIndent()
# lammps_indent.write()
#
# vasp_min = Scheme("AtomisticSim_VaspMin")
# vasp_min.fields = SimUniversal() + SimVasp() + SimMinimize()
# vasp_min.write()
#
# vasp_md = Scheme("AtomisticSim_VaspMD")
# vasp_md.fields = SimUniversal() + SimVasp() + SimMD()
# vasp_md.write()

scheme_name = "Atomistic_simulation"
atomistic_simul = Scheme(scheme_name)
atomistic_simul.fields = SimUniversal()
atomistic_simul.write()
atomistic_simul.write(file_extension='txt')

# atomistic_simul.fields = SimTechnical()
# atomistic_simul.write(scheme_name+"_grey.ttl")
#
# atomistic_simul.fields = SimVasp() + SimLammps()
# atomistic_simul.fields += SimMD() + SimMinimize()
# atomistic_simul.fields += SimDeform() + SimIndent()
# atomistic_simul.fields += SimHess() + SimTI()
# atomistic_simul.write(scheme_name+"_green.ttl")

scheme_name = "Atomistic_output"
output = Scheme(scheme_name)
output.fields = AtomisticOutputCoScInE()
output.write()
output.write(file_extension='txt')
output.write(file_extension="html")

# output.fields = AtomisticOutput()
# output.write(scheme_name+"_full.ttl")

scheme_name = "Atomistic_snapshot"
snapshot = Scheme(scheme_name)
snapshot.fields = AtomisticSnapshotCoScInE()
snapshot.write()
snapshot.write(file_extension='txt')

# snapshot.fields = AtomisticSnapshotGreen()
# snapshot.write(scheme_name+"_green.ttl")
#
# snapshot.fields = AtomisticSnapshot()
# snapshot.write(scheme_name+"_full.ttl")

scheme_name = "ML_potential"
ML_pot = Scheme(scheme_name)
ML_pot.fields = MLPotCoScInE()
ML_pot.write()
ML_pot.write(file_extension='txt')

# ML_pot.fields = MLPotGreen()
# ML_pot.write(scheme_name+"_green.ttl")
#
# ML_pot.fields = MLPot()
# ML_pot.write(scheme_name+"_full.ttl")


Calphad_calc = Scheme("Calphad_calc")
Calphad_calc.fields = CalphadCalc()
Calphad_calc.write(file_extension='.txt')
Calphad_calc.write()

CALPHAD_DB = Scheme("Calphad_db")
CALPHAD_DB.fields = CalphadDB()
CALPHAD_DB.write()
CALPHAD_DB.write(file_extension='.txt')

DAMASK = Scheme("DAMASK")
DAMASK.fields = DamaskCoScInE()
DAMASK.write()
DAMASK.write(file_extension='.txt')

ImageAnalysis_scheme = Scheme("ImageAnalysis")
ImageAnalysis_scheme.fields = ImageAnalysis()
ImageAnalysis_scheme.write()
ImageAnalysis_scheme.write(file_extension="txt")
