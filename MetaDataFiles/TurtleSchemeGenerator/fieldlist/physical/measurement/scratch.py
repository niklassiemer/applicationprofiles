from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import MeasurementAtSpot


class Scratch(MeasurementAtSpot):  # ToDo: Is this really a MeasurementAtSpot? SampleLocation was present...
    def __init__(self):
        super().__init__()
        self.add(label="Tip ID", name="tip")
        self.add(label="Scratch crystallographic orientation")
        self.add(label="Scratch surface plane")
        self.add(label="Loading type")

        # green fields
        self.add(label="Type of test")  # Does this differ from "loading type"?
        self.add(label="Scratch length", unit=micro+"m")
        self.add(label="Scratch velocity", unit=micro+"m/s")
        self.add(label="Scratch orientation", unit=deg)
        self.add(label="Maximum scratch load", unit='mN')
        self.add(label="Profiling velocity", unit=micro+"m/s")

        self.sort_fields_by_order_priority()
