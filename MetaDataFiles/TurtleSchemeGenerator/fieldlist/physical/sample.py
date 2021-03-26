from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


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


class SamplePreparation(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine")
        self.add(label="Grit 1")
        self.add(label="Solvent grit 1")
        self.add(label="Grit 2")
        self.add(label="Solvent grit 2")
        self.add(label="Grit material")
        self.add(label="Polishing Suspension", unit=micro + 'm')
        self.add(label="Material Suspension")
        self.add(label="Solvent")


class Immersion(SFBFields):
    def __init__(self):
        super().__init__()
        # This should be the ID?!
        # self.add(label='Immersion experiment ID')
        self.add(label='Immersion experiment routine')
        self.add(label="Electrolyte pH", qudt='PH')
        self.add(label="Electrolyte condition")
        self.add(label="Flow rate", unit="ml/h")
        self.add(label="Revolutions per minute", unit='rpm', qudt='PER-MIN')
        self.add(label="Volume", unit='ml')
        # grey
        self.add(label="Temperature", unit=deg+'C')


class Etching(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Etching routine")
        self.add(label="Operator")
        self.add(label="Chemicals")
        self.add(label="Duration", unit="s")


class Sample(Etching, Immersion, SamplePreparation, ParentSample, SampleBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()