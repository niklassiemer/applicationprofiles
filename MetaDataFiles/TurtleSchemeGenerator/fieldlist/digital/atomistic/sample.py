from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class SamplePreparation(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label='Software ID')
        self.add(label="Data format")


class SampleCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        # blue
        self.add(label="Phases", long=True)
        self.add(label="Chemical species")
        self.add(label="Chemical species identifiers")
        self.add(label="Generator ID", comment='This could be a Simulation ID (cf. Generator frame), an External ID, '
                                               'or an Sample preparation ID. ')
        self.add(label="Generator frame", comment='Used to unambiguously refer to a specific structure from '
                                                  'Generator ID')  # int
        self.add(label="Construction method", long=True, comment='E.g. pyiron command; recommended only for very short'
                                                                 '/trivial generation methods, use a '
                                                                 'SamplePreparation ID otherwise.')
        # grey
        self.add(label="Defects contained")
        self.add(label="Mechanical treatment")
        self.add(label="Heat treatment")  # aka temperature
        self.add(label="Point group")
        self.add(label="Sublattices")
        self.add(label="Additional properties")

        self.add(label="File format", example_input='xyz', comment='Format of the file the Sample is stored.')

        self.sort_fields_by_order_priority()


class Sample(SampleCoScInE):
    def __init__(self):
        super().__init__()
        self.add(label="Chemical formula")  # str
        self.add(label="Chemical species")  # list(str)
        self.add(label="Number of atoms")  # int
        self.add(label="Chemical species count")  # dict
        self.add(label="Lattice constants")
        self.add(label="Crystallographic orientation X axis", long=True)
        self.add(label="Crystallographic orientation Y axis", long=True)
        self.add(label="Crystallographic orientation Z axis", long=True)
        self.add(label="Mass", long=True)
        self.add(label="Periodicity of the crystal")
        self.add(label="Sample description")
        self.add(label="Additional properties")

        self.sort_fields_by_order_priority()
