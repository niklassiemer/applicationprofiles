from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg


class PhysicalEnvironment(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Temperature", unit=deg+'C')
        self.add(label="Relative Humidity", unit='%', other_ttl_relations={"qudt:Unit": "unit:PERCENT_RH"})
        self.add(label="Environmental gas")


class PhysicalActivity(PhysicalEnvironment):
    def __init__(self):
        super().__init__()
        self.add(label="Operator", comment="The person who did the physical work. Default is the user.")
        self.add(label="Instrument ID", comment="Which device was used for this activity.",
                 sh_path="csmd:investigation_instrument")


class Experiment(PhysicalActivity):
    """An experiment is a PhysicalActivity on a sample"""
    def __init__(self):
        super().__init__()
        self.add(label='Sample ID')  # In an ideal world, this would keep track of everything, however:
        self.add(label="Parent Sample ID")
        self.add(label='Any data set to be linked with this experiment', long=True)
        self.add(label="Environmental protection during sample processing", name="TestingEnv")
        self.add(label="Pre-treatment")


class PhysicalObject(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Location", comment="Where is this in the real world.")


class Instrument(PhysicalObject):
    def __init__(self):
        super().__init__()
        self.add(label="Manufacturer")
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


class Tip(PhysicalObject):
    def __init__(self):
        super().__init__()
        raise NotImplementedError("We don't have any info on this.")