from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.sample import SampleCoScInE
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.simulation import SimBasic, SimTechnical, \
    SimUniversal, SimLammps, SimVasp, SimMD, SimMinimize, SimDeform, SimIndent, SimHess, SimTI, LammpsMin, \
    AtomisticOutputCoScInE, AtomisticOutput, AtomisticSnapshotCoScInE, AtomisticSnapshotGreen, AtomisticSnapshot
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.atomistic.potential import MLPotCoScInE, MLPotGreen, MLPot

sample_scheme = Scheme("AtomisticSample")
sample_scheme.fields = SampleCoScInE()
sample_scheme.fields.write('AtomisticSample.txt')
sample_scheme.write("AtomisticSample.ttl")


lammps_min = Scheme("AtomisticSim_LammpsMin")
lammps_min.fields = LammpsMin()
lammps_min.write()

lammps_md = Scheme("AtomisticSim_LammpsMD")
lammps_md.fields = SimUniversal() + SimLammps() + SimMD()
lammps_md.write()

lammps_deform = Scheme("AtomisticSim_LammpsDeformMD")
lammps_deform.fields = lammps_md.fields.copy() + SimDeform()
lammps_deform.write()

lammps_indent = Scheme("AtomisticSim_LammpsIndentMD")
lammps_indent.fields = lammps_md.fields.copy() + SimIndent()
lammps_indent.write()

vasp_min = Scheme("AtomisticSim_VaspMin")
vasp_min.fields = SimUniversal() + SimVasp() + SimMinimize()
vasp_min.write()

vasp_md = Scheme("AtomisticSim_VaspMD")
vasp_md.fields = SimUniversal() + SimVasp() + SimMD()
vasp_md.write()

scheme_name = "Atomistic_simulation"
atomistic_simul = Scheme(scheme_name)
atomistic_simul.fields = SimBasic()
atomistic_simul.write()

atomistic_simul.fields = SimTechnical()
atomistic_simul.write(scheme_name+"_grey.ttl")

atomistic_simul.fields = SimVasp() + SimLammps()
atomistic_simul.fields += SimMD() + SimMinimize()
atomistic_simul.fields += SimDeform() + SimIndent()
atomistic_simul.fields += SimHess() + SimTI()
atomistic_simul.write(scheme_name+"_green.ttl")

scheme_name = "Atomistic_output"
output = Scheme(scheme_name)
output.fields = AtomisticOutputCoScInE()
output.write()

output.fields = AtomisticOutput()
output.write(scheme_name+"_full.ttl")

scheme_name = "Atomistic_snapshot"
snapshot = Scheme(scheme_name)
snapshot.fields = AtomisticSnapshotCoScInE()
snapshot.write()

snapshot.fields = AtomisticSnapshotGreen()
snapshot.write(scheme_name+"_green.ttl")

snapshot.fields = AtomisticSnapshot()
snapshot.write(scheme_name+"_full.ttl")

scheme_name = "ML_potential"
ML_pot = Scheme(scheme_name)
ML_pot.fields = MLPotCoScInE()
ML_pot.write()

ML_pot.fields = MLPotGreen()
ML_pot.write(scheme_name+"_green.ttl")

ML_pot.fields = MLPot()
ML_pot.write(scheme_name+"_full.ttl")

