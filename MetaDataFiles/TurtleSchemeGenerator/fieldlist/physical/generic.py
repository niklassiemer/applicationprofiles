from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class PhysicalActivity(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Operator", comment="The person who did the physical work. Default is the user.")


class PhysicalObject(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Location", comment="Where is this in the real world.")
