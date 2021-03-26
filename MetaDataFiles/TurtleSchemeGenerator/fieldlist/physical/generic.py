from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class PhysicalActivity(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Operator", comment="The person who did the physical work. Default is the user.")
        self.add(label="Instrument ID", comment="Which device was used for this activity.")


class PhysicalObject(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Location", comment="Where is this in the real world.")


class Instrument(PhysicalObject):
    def __init__(self):
        super().__init__()
        raise NotImplementedError("We have never even talked about this. Maybe it's perfectly a `PhysicalObject`.")
