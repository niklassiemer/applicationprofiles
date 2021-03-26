from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class SampleCoScInE(SFBFields):
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
