from data_scheme import MetaDataSchemes as Scheme, FieldList, SFBFields

angstrom = "\u212B"

sample_blue = SFBFields()
sample_blue.add(label="Parent ID")

sample_yellow = FieldList()
sample_yellow.add(label="Generator ID")
sample_yellow.add(label="Generator frame")  # int
sample_yellow.add(label="Construction method", long=True)  # i.e. pyiron command

sample_green = FieldList()
sample_green.add(label="Chemical formula")  # str
sample_green.add(label="Chemical species")  # list(str)
sample_green.add(label="Number of atoms")  # int
sample_green.add(label="Chemical species count")  # dict

sample_grey = FieldList()
sample_grey.add(label="Defects contained")
sample_grey.add(label="Mechanical treatment")
sample_grey.add(label="Heat treatment")  # aka temperature
sample_grey.add(label="Point group")
sample_grey.add(label="Sublattices")

sample_scheme = Scheme("AtomisticSample")
sample_scheme.fields = sample_blue + sample_yellow + sample_green + sample_grey
sample_scheme.write("AtomisticSample_full.ttl")

sample_scheme.fields = sample_blue
sample_scheme.write()

sample_scheme.fields = sample_grey
sample_scheme.write("AtomisticSample_grey.ttl")

sample_scheme.fields = sample_green
sample_scheme.write("AtomisticSample_green.ttl")

sample_scheme.fields = sample_yellow
sample_scheme.write("AtomisticSample_yellow.ttl")


sim_blue = SFBFields()
# TODO: discuss: This is listed in green for simulations!
#sim_blue.add(label="Sample ID", required=True)
sim_blue.add(label="Status", field_type="list")  # Choice ('initialized', 'running', etc)
sim_blue.add(label="Last status update")  # timestamp
sim_blue.add(label="pyiron version")
sim_blue.add(label="Other software versions")

sim_technical = FieldList()
sim_technical.add(label="Cluster")
sim_technical.add(label="Node")
sim_technical.add(label="Cores")
sim_technical.add(label="Runtime")
sim_technical.add(label="Submission time")
sim_technical.add(label="Stop time")

sim_universal = sim_blue + sim_technical
# Since I took it out of the blue:
sim_universal.add(label="Sample ID") #, required=True)

sim_lammps = FieldList()
sim_lammps.add(label="Potential")
sim_lammps.add(label="Lammps version")

sim_vasp = FieldList()
sim_vasp.add(label="Plane wave energy cutoff", unit='eV')
sim_vasp.add(label="Kpoint mesh")
sim_vasp.add(label="Pseudopotential")
sim_vasp.add(label="Spin polarization", field_type="bool")
# ...etc?

sim_md = FieldList()
sim_md.add(label="Temperature", unit='K')
sim_md.add(label="Thermodynamic ensemble")
sim_md.add(label="Initial temperature", unit='K')  # For initial kinetic energy
sim_md.add(label="Temperature end", unit='K')  # For linear ramping between Temperature and this value
sim_md.add(label="Thermostat style", field_type="list")
sim_md.add(label="Thermostat timescale", unit='fs')
sim_md.add(label="Pressure", unit="GPa")
sim_md.add(label="Pressure end", unit="GPa")
sim_md.add(label="Barostat style", field_type="list")
sim_md.add(label="Barostat timescale", unit="fs")
sim_md.add(label="Time step", unit='fs')
sim_md.add(label="Atomic steps")
sim_md.add(label="Print period")
sim_md.add(label="Print detail")
sim_md.add(label="Random seed")

sim_minimize = FieldList()
sim_minimize.add(label="Force convergence criterion", unit='eV/'+angstrom)
sim_minimize.add(label="Force convergence criterion norm type")
sim_minimize.add(label="Minimization scheme parameter")
sim_minimize.add(label="Energy convergence criterion", unit='eV')
sim_minimize.add(label="Max steps")
sim_minimize.add(label="Max steps force evaluation")
sim_minimize.add(label="Minimization scheme", field_type="list")
sim_minimize.add(label="Pressure", unit="GPa")
sim_minimize.add(label="Print detail", name="calcMinPrintDetail")

sim_deform = FieldList()
sim_deform.add(label="Deformation direction")
sim_deform.add(label="Strain rate tensor")
sim_deform.add(label="Homogeneous scaling", field_type="bool")

sim_indent = FieldList()
sim_indent.add(label="Indentor velocity", unit='m/s')
sim_indent.add(label="Indentor direction")
sim_indent.add(label="Indentor position")
sim_indent.add(label="Indentor shape")  # Choice e.g. spherical
sim_indent.add(label="Indentor size")
sim_indent.add(label="Indentor type")  # Choice? e.g. Virtual

sim_hess = FieldList()
sim_hess.add(label="Spring constant", unit="eV/"+angstrom+"**2")
sim_hess.add(label="Reference Job")

sim_TI = FieldList()
sim_TI.add(label="Reference A, B", name="TIRefJobs")
sim_TI.add(label="Sample Reference", name="TISampleRef")
sim_TI.add(label="Thermalization Steps")
sim_TI.add(label="Number of lambda points")
sim_TI.add(label="Custom lambda points")
sim_TI.add(label="Statistical error tolerance", unit='eV')

lammps_min = Scheme("AtomisticSim_LammpsMin")
lammps_min.fields = sim_universal + sim_lammps + sim_minimize
lammps_min.write()

lammps_md = Scheme("AtomisticSim_LammpsMD")
lammps_md.fields = sim_universal + sim_lammps + sim_md
lammps_md.write()

lammps_deform = Scheme("AtomisticSim_LammpsDeformMD")
lammps_deform.fields = lammps_md.fields.copy() + sim_deform
lammps_deform.write()

lammps_indent = Scheme("AtomisticSim_LammpsIndentMD")
lammps_indent.fields = lammps_md.fields.copy() + sim_deform
lammps_indent.write()

vasp_min = Scheme("AtomisticSim_VaspMin")
vasp_min.fields = sim_universal + sim_vasp + sim_minimize
vasp_min.write()

vasp_md = Scheme("AtomisticSim_VaspMD")
vasp_md.fields = sim_universal + sim_vasp + sim_md
vasp_md.write()

scheme_name = "Atomistic_simulation"
atomistic_simul = Scheme(scheme_name)
atomistic_simul.fields = sim_blue
atomistic_simul.write()

atomistic_simul.fields = sim_technical
atomistic_simul.write(scheme_name+"_grey.ttl")

atomistic_simul.fields = sim_vasp + sim_lammps
atomistic_simul.fields += sim_md + sim_minimize
atomistic_simul.fields += sim_deform + sim_indent
atomistic_simul.fields += sim_hess + sim_TI
atomistic_simul.write(scheme_name+"_green.ttl")

output_blue = SFBFields()
output_blue.add(label="Sample ID", required=True)
output_blue.add(label="Trajectory ID")
output_blue.add(label="Simulation ID")
output_blue.add(label="External ID")
output_blue.add(label="Configuration format")
output_blue.add(label="References")

output_green = FieldList()
output_green.add("Chemical species")
output_green.add("Number of atoms")
output_green.add("Chemical species count")
output_green.add("Additional properties")
output_green.add("Timestep")
output_green.add("Time", unit='ps')

scheme_name = "Atomistic_output"
output = Scheme(scheme_name)
output.fields = output_blue
output.write()

output.fields = output_green
output.write(scheme_name+"_green.ttl")

output.fields = output_blue + output_green
output.write(scheme_name+"_full.ttl")


snapshot_blue = SFBFields()
snapshot_blue.add(label="Snapshot ID")
snapshot_blue.add(label="Sample ID")
snapshot_blue.add(label="External ID")
snapshot_blue.add(label="Snapshot format")
snapshot_blue.add(label="Visualization program")
snapshot_blue.add(label="Visualization program command")
snapshot_blue.add(label="References")

snapshot_green = FieldList()
snapshot_green.add(label='Atomistic color')
snapshot_green.add(label="Color information")
snapshot_green.add(label="Perspective", field_type='bool')

scheme_name = "Atomistic_snapshot"
snapshot = Scheme(scheme_name)
snapshot.fields = snapshot_blue
snapshot.write()

snapshot.fields = snapshot_green
snapshot.write(scheme_name+"_green.ttl")

snapshot.fields = snapshot_blue + snapshot_green
snapshot.write(scheme_name+"_full.ttl")

ML_pot_blue = SFBFields()
ML_pot_blue.add(label="Potential ID")
ML_pot_blue.add("Potential type/ format", name="potentialID")
ML_pot_blue.add("Software used")
ML_pot_blue.add("References")
# Training metadata
ML_pot_blue.add("Parent Potential")
ML_pot_blue.add("Training data")
ML_pot_blue.add("Optimizer parameters")

ML_pot_green = FieldList()
ML_pot_green.add(label="Species treated")
ML_pot_green.add(label='Structure types treated')

scheme_name = "ML_potential"
ML_pot = Scheme(scheme_name)
ML_pot.fields = ML_pot_blue
ML_pot.write()

ML_pot.fields = ML_pot_green
ML_pot.write(scheme_name+"_green.ttl")

ML_pot.fields = ML_pot_blue + ML_pot_green
ML_pot.write(scheme_name+"_full.ttl")

