from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement


class ScratchBasic(SpotMeasurement):  # ToDo: Is this really a SpotMeasurement? SampleLocation was present...
    def __init__(self):
        super().__init__()
        self.add(label="Tip ID", name="tip")
        self.add(label="Scratch crystallographic orientation")
        self.add(label="Scratch surface plane")
        self.add(label="Loading type")

        # green fields
        self.add(label="Type of test")  # Does this differ from "loading type"?
        self.add(label="Scratch Length", unit=micro+"m")
        self.add(label="Scratch Velocity", unit=micro+"m/s")
        self.add(label="Scratch Orientation", unit=deg)
        self.add(label="Maximum scratch load", unit='mN')
        self.add(label="Profiling velocity", unit=micro+"m/s")

        self.sort_fields_by_order_priority()
