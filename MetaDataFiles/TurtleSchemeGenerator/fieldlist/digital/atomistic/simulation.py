from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import SimTechnical
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import angstrom, squared


class SimBasic(SFBFields):
    # TODO: discuss: This is listed in green for simulations!
    # sim_blue.add(label="Sample ID", required=True)
    def __init__(self):
        super().__init__()
        self.add(label="Status", field_type=['initialized', 'created', 'submitted', 'running',
                 'collect', 'finished', 'refresh', 'suspended'])
        self.add(label="Last status update", field_type="date", sh_path='csmd:dataset_endDate')


# Inherit from SimTechnical first since then its fields are added to the SimBasic.
class SimUniversal(SimTechnical, SimBasic):
    def __init__(self):
        super().__init__()
        # Since I took it out of the blue:
        self.add(label="Sample ID") #, required=True)
        self.add(label="Simulation type")
        self.add(label="Job submission commands", long=True)

        self.sort_fields_by_order_priority()


class SimLammps(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Potential")


class SimVasp(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Plane wave energy cutoff", unit='eV')
        self.add(label="Kpoint mesh")
        self.add(label="Pseudopotential")
        self.add(label="Spin polarization", field_type="bool")
        # TODO: ...etc? Vasp has so many options...


class SimMDCoscine(SimUniversal):
    def __init__(self):
        super().__init__()
        # moved here from old AtomisticOutput
        self.add(label="File format", example_input='xyz', comment='Format of the file the Sample is stored.')
        self.add(label="Time sampled", unit='ps')
        self.add(label="Number of individual configurations sampled")


class SimMD(SimMDCoscine):
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
        self.add(label="Minimization scheme parameter")  # TODO: What is this?
        self.add(label="Energy convergence criterion", unit='eV')
        self.add(label="Max steps")
        self.add(label="Max steps force evaluation")  # TODO: What is this? Why not only limiting steps?
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
        self.add(label="Reference Job")  # TODO: What is this?


class SimTI(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Reference A ID", name="TIRefJobA")
        self.add(label="Reference B ID", name="TIRefJobB")
        self.add(label="Sample Reference A ID", name="TISampleRefA")
        self.add(label="Sample Reference B ID", name="TISampleRefB")  # Optional
        self.add(label="Thermalization steps")
        self.add(label="Number of lambda points")
        self.add(label="Custom lambda points")
        self.add(label="Statistical error tolerance", unit='eV')


class LammpsMin(SimMinimize, SimLammps, SimUniversal):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


class PostProcessingCoScInE(SimTechnical):
    def __init__(self):
        super().__init__()
        # This is the ID: self.add(label="Snapshot ID")
        self.add(label="Source IDs", comment='Simulation IDs (cf. Frames used) / SampleIDs which are post processed.')
        self.add(label="External ID")
        self.add(label='Frames used', long=True, comment='A list of frames per Simulation ID, which are used for the'
                                                         'post-processing.')
        self.add(label="Data format")

        self.sort_fields_by_order_priority()


class PostProcessing(PostProcessingCoScInE):
    def __init__(self):
        super().__init__()
        self.add('Steps', long=True)
        self.add('Related post processing IDs')


class AtomisticSnapshotCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add('Post processing ID')
        self.add('Format', example_input='jpg')
        self.add('External ID')


class AtomisticSnapshotGreen(AtomisticSnapshotCoScInE):
    def __init__(self):
        super().__init__()
        self.add(label='Atomistic color')
        self.add(label="Color information")
        self.add(label="Perspective", field_type='bool')
        self.add(label="Resolution")
        self.add(label="Frame rate")
        self.add(label="Duration")
        self.add(label="Codec")

        self.sort_fields_by_order_priority()
