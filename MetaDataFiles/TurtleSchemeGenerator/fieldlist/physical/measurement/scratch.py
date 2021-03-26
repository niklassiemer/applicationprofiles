from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class ScratchBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Sample Location")
        self.add(label="Instrument used", name="instrument")
        self.add(label="Tip used", name="tip")
        self.add(label="Scratch crystallographic orientation")
        self.add(label="Scratch surface plane")
        self.add(label="Loading type")


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Relative Humidity", unit='%', qudt="PERCENT_RH")
        self.add(label="Temperature", unit="\u00b0C")
        self.add(label="Environmental gas")
        self.add(label="Test date", field_type="date")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Type of test")
        self.add(label="Scratch Length", unit=micro+"m")
        self.add(label="Scratch Velocity", unit=micro+"m/s")
        self.add(label="Scratch Orientation", unit=deg)
        self.add(label="Maximum scratch load", unit='mN')
        self.add(label="Profiling velocity", unit=micro+"m/s")


class Scratch(Grey, Green, ScratchBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()