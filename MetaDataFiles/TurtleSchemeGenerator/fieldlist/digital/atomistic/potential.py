from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class MLPotCoScInE(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Potential ID")
        self.add(label="Potential type/ format", name="potentialID")
        self.add(label="Software ID")
        self.add(label="References")
        # Training metadata
        self.add(label="Parent potential")
        self.add(label="Training data")
        self.add(label="Optimizer parameters")


class MLPotGreen(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Species treated")
        self.add(label='Structure types treated')


class MLPot(MLPotGreen, MLPotCoScInE):
    pass