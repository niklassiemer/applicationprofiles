from data_scheme import MetaDataSchemes as Scheme, FieldList, SFBFields

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
sample_scheme.write()


sim_blue = SFBFields()
sim_blue.add(label="Sample ID", required=True)
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

sim_lammps = FieldList()
sim_lammps.add(label="Potential")
sim_lammps.add(label="Lammps version")

sim_vasp = FieldList()
sim_vasp.add(label="Plane wave energy cutoff")
sim_vasp.add(label="Kpoint mesh")
sim_vasp.add(label="Pseudopotential")
sim_vasp.add(label="Spin polarization", field_type="bool")
# ...etc?

sim_md = FieldList()
sim_md.add(label="Temperature")
sim_md.add(label="Initial temperature")  # For initial kinetic energy
sim_md.add(label="Temperature end")  # For linear ramping between Temperature and this value
sim_md.add(label="Thermostat style", field_type="list")
sim_md.add(label="Thermostat timescale")
sim_md.add(label="Pressure")
sim_md.add(label="Pressure end")
sim_md.add(label="Barostat style", field_type="list")
sim_md.add(label="Barostat timescale")
sim_md.add(label="Time step")
sim_md.add(label="Atomic steps")
sim_md.add(label="Print period")
sim_md.add(label="Random seed")

sim_minimize = FieldList()
sim_minimize.add(label="Force convergence criterion")
sim_minimize.add(label="Energy convergence criterion")
sim_minimize.add(label="Max steps")
sim_minimize.add(label="Minimization scheme", field_type="list")
sim_minimize.add(label="Pressure")

sim_deform = FieldList()
sim_deform.add(label="Strain rate tensor")
sim_deform.add(label="Homogeneous scaling", field_type="bool")

sim_indent = FieldList()
sim_indent.add(label="Indentor velocity")
sim_indent.add(label="Indentor direction")
sim_indent.add(label="Indentor position")
sim_indent.add(label="Indentor shape")  # Choice e.g. spherical
sim_indent.add(label="Indentor size")
sim_indent.add(label="Indentor type")  # Choice? e.g. Virtual


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

# TODO: Output, Snapshot, and MLPotential
