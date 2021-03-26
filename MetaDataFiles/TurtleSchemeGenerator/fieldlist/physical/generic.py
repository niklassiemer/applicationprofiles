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


class Sample(PhysicalObject):
    def __init__(self):
        super().__init__()
        self.add(label="Parent ID", name="parentSample", comment="The super-sample from which this came.")
        self.add(
            label="Preparation IDs",
            comment="What was done to this sample that differentiates it from its parent, in order of operation. "
                    "Multiple routines should only be given for perfectly contiguous sample chains."
        )
        self.sort_fields_by_order_priority()