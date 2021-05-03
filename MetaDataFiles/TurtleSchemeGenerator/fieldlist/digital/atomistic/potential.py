from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class MLPotCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Potential ID")
        self.add("Potential type/ format", name="potentialID")
        self.add("Software used")
        self.add("References")
        # Training metadata
        self.add("Parent potential")
        self.add("Training data")
        self.add("Optimizer parameters")


class MLPotGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Species treated")
        self.add(label='Structure types treated')


class MLPot(MLPotGreen, MLPotCoScInE):
    pass