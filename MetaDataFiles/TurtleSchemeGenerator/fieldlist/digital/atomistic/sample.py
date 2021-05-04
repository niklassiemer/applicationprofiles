from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class SamplePreparation(SFBFields):
    def __init__(self):
        super().__init__()
        self.add('Software ID')
        self.add(label="Data format")


class SampleCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        # blue
        self.add(label="Phases", long=True)
        self.add(label="Chemical species")
        self.add(label="Chemical species identifiers")
        self.add(label="Preparation ID")
        # yellow
        self.add(label="Generator ID")
        self.add(label="Generator frame")  # int
        self.add(label="Construction method", long=True, comment='E.g. pyiron command')
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
        self.add(label="Lattice constants")
        self.add(label="Crystallographic orientation X axis", long=True)
        self.add(label="Crystallographic orientation Y axis", long=True)
        self.add(label="Crystallographic orientation Z axis", long=True)
        self.add(label="Mass", long=True)
        self.add(label="Periodicity of the crystal")
        self.add(label="Sample description")

        self.sort_fields_by_order_priority()
