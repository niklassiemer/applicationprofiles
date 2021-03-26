from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class XPSBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label="Sample storage")
        self.add(label="Pre-treatment")
        self.add(label="Energy range start", unit='eV')
        self.add(label="Energy range end", unit='eV')
        self.add(label="Etching source")
        self.add(label="Etching energy")
        self.add(label="Etching duration")
        self.add(label="Etching power")
        self.add(label="Anode material")
        self.add(label="Anode power", unit='W')
        self.add(label="Anode voltage", unit='kV')
        self.add(label="Pass energy", unit='eV')
        self.add(label="Working pressure", unit='lg(Torr)', qudt='None')
        self.add(label="Energy resolution", unit='eV')


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class XPS(Yellow, XPSBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()