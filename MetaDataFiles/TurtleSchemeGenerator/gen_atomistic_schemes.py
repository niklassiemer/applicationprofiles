from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme, FieldList, SFBFields

angstrom = "\u212B"
squared = '\u00B2'
cubic = '\u00B3'


class SampleBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Parent ID")


class SampleCoScInE(SampleBasic):
    def __init__(self):
        super().__init__()
        # yellow
        self.add(label="Generator ID")
        self.add(label="Generator frame")  # int
        self.add(label="Construction method", long=True)  # i.e. pyiron command
        # grey
        self.add(label="Defects contained")
        self.add(label="Mechanical treatment")
        self.add(label="Heat treatment")  # aka temperature
        self.add(label="Point group")
        self.add(label="Sublattices")

        self.sort_fields_by_order_priority()


class Sample(SampleCoScInE):
    def __init__(self):
        super().__init__()
        self.add(label="Chemical formula")  # str
        self.add(label="Chemical species")  # list(str)
        self.add(label="Number of atoms")  # int
        self.add(label="Chemical species count")  # dict

        self.sort_fields_by_order_priority()


sample_scheme = Scheme("AtomisticSample")
sample_scheme.fields = SampleCoScInE()
sample_scheme.fields.write('AtomisticSample.txt')
sample_scheme.write("AtomisticSample.ttl")


class SimBasic(SFBFields):
    # TODO: discuss: This is listed in green for simulations!
    # sim_blue.add(label="Sample ID", required=True)
    def __init__(self):
        super().__init__()
        self.add(label="Status", field_type="list")  # Choice ('initialized', 'running', etc)
        self.add(label="Last status update")  # timestamp
        self.add(label="pyiron version")
        self.add(label="Other software versions")
        self.add(label="External ID")
        self.add(label="Simulation type")
        # We have DOI and References, DOI is for papers about this and references for what?!
        self.add(label="References")


class SimTechnical(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Cluster")
        self.add(label="Node")
        self.add(label="Cores")
        self.add(label="Runtime")
        self.add(label="Submission time")
        self.add(label="Stop time")


# Inherit from SimTechnical first since then its fields are added to the SimBasic.
class SimUniversal(SimTechnical, SimBasic):
    def __init__(self):
        super().__init__()
        # Since I took it out of the blue:
        self.add(label="Sample ID") #, required=True)


class SimLammps(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Potential")
        self.add(label="Lammps version")


class SimVasp(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Plane wave energy cutoff", unit='eV')
        self.add(label="Kpoint mesh")
        self.add(label="Pseudopotential")
        self.add(label="Spin polarization", field_type="bool")
        # ...etc?


class SimMD(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Temperature", unit='K')
        self.add(label="Thermodynamic ensemble")
        self.add(label="Initial temperature", unit='K')  # For initial kinetic energy
        self.add(label="Temperature end", unit='K')  # For linear ramping between Temperature and this value
        self.add(label="Thermostat style", field_type="list")
        self.add(label="Thermostat timescale", unit='fs')
        self.add(label="Pressure", unit="GPa")
        self.add(label="Pressure end", unit="GPa")
        self.add(label="Barostat style", field_type="list")
        self.add(label="Barostat timescale", unit="fs")
        self.add(label="Time step", unit='fs')
        self.add(label="Atomic steps")
        self.add(label="Print period")
        self.add(label="Print detail")
        self.add(label="Random seed")


class SimMinimize(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Force convergence criterion", unit='eV/'+angstrom)
        self.add(label="Force convergence criterion norm type")
        self.add(label="Minimization scheme parameter")
        self.add(label="Energy convergence criterion", unit='eV')
        self.add(label="Max steps")
        self.add(label="Max steps force evaluation")
        self.add(label="Minimization scheme", field_type="list")
        self.add(label="Pressure", unit="GPa")
        self.add(label="Print detail", name="calcMinPrintDetail")


class SimDeform(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Deformation direction")
        self.add(label="Strain rate tensor")
        self.add(label="Homogeneous scaling", field_type="bool")


class SimIndent(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Indentor velocity", unit='m/s')
        self.add(label="Indentor direction")
        self.add(label="Indentor position")
        self.add(label="Indentor shape")  # Choice e.g. spherical
        self.add(label="Indentor size")
        self.add(label="Indentor type")  # Choice? e.g. Virtual


class SimHess(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Spring constant", unit="eV/"+angstrom+squared)
        self.add(label="Reference Job")


class SimTI(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Reference A, B", name="TIRefJobs")
        self.add(label="Sample Reference", name="TISampleRef")
        self.add(label="Thermalization Steps")
        self.add(label="Number of lambda points")
        self.add(label="Custom lambda points")
        self.add(label="Statistical error tolerance", unit='eV')


class LammpsMin(SimMinimize, SimLammps, SimUniversal):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


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


class AtomisticOutputCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Sample ID", required=True)
        self.add(label="Trajectory ID")
        self.add(label="Simulation ID")
        self.add(label="External ID")
        self.add(label="Configuration format")
        self.add(label="References")


class AtomisticOutputGreen(FieldList):
    def __init__(self):
        super().__init__()
        # green
        self.add("Chemical species")
        self.add("Number of atoms")
        self.add("Chemical species count")
        self.add("Additional properties")
        self.add("Timestep")
        self.add("Time", unit='ps')


class AtomisticOutput(AtomisticOutputGreen, AtomisticOutputCoScInE):
    pass


scheme_name = "Atomistic_output"
output = Scheme(scheme_name)
output.fields = AtomisticOutputCoScInE()
output.write()

output.fields = AtomisticOutput()
output.write(scheme_name+"_full.ttl")


class AtomisticSnapshotCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Snapshot ID")
        self.add(label="Sample ID")
        self.add(label="External ID")
        self.add(label="Snapshot format")
        self.add(label="Visualization program")
        self.add(label="Visualization program command")
        self.add(label="References")


class AtomisticSnapshotGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label='Atomistic color')
        self.add(label="Color information")
        self.add(label="Perspective", field_type='bool')


class AtomisticSnapshot(AtomisticSnapshotGreen, AtomisticSnapshotCoScInE):
    pass


scheme_name = "Atomistic_snapshot"
snapshot = Scheme(scheme_name)
snapshot.fields = AtomisticSnapshotCoScInE()
snapshot.write()

snapshot.fields = AtomisticSnapshotGreen()
snapshot.write(scheme_name+"_green.ttl")

snapshot.fields = AtomisticSnapshot()
snapshot.write(scheme_name+"_full.ttl")


class MLPotCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Potential ID")
        self.add("Potential type/ format", name="potentialID")
        self.add("Software used")
        self.add("References")
        # Training metadata
        self.add("Parent Potential")
        self.add("Training data")
        self.add("Optimizer parameters")


class MLPotGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Species treated")
        self.add(label='Structure types treated')


class MLPot(MLPotGreen, MLPotCoScInE):
    pass


scheme_name = "ML_potential"
ML_pot = Scheme(scheme_name)
ML_pot.fields = MLPotCoScInE()
ML_pot.write()

ML_pot.fields = MLPotGreen()
ML_pot.write(scheme_name+"_green.ttl")

ML_pot.fields = MLPot()
ML_pot.write(scheme_name+"_full.ttl")

