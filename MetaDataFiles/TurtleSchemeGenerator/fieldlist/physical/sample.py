from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalObject


class SampleBasic(SFBFields):
    def __init__(self):
        super().__init__()
        # This should be the ID!?
        # self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Location")


class ParentSample(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Designation")
        # Why is this not at the Sample level?
        self.add(label="Chemical composition")
        self.add(label="Production batch designation")


class Etching(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Etching routine")
        self.add(label="Operator")
        self.add(label="Chemicals")
        self.add(label="Duration", unit="s")


class Sample(PhysicalObject):
    def __init__(self):
        super().__init__()
        self.add(label="Parent ID", name="parentSample", comment="The super-sample from which this came.")
        self.add(label="Preparation ID", comment="What was done to this sample that differentiates it from its parent")
        self.sort_fields_by_order_priority()
