from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg


class NanoIndentationBasic(SpotMeasurement):
    def __init__(self):
        super().__init__()
        self.add(label="Sample Orientation", long=True)

        self.add(label="Type of test")
        self.add(label="Control method")
        self.add(label="Tip ID", name="tip")
        self.add(label="Diamond area function")
        self.add(label="Date of calibration", field_type="date")  # TODO: Do we need a tip calibration activity?
        self.add(label="Frame stiffness", unit='N/m')

        self.add(label="Target load", unit="mN")
        self.add(label="Target depth", unit="nm")
        self.add(label="Continuous stiffness measurement", field_type='bool')
        self.add(label="Drift correction enabled", field_type="bool")
        self.add(label="Sample temperature", unit=deg+"C")
        self.add(label="Tip temperature", unit=deg+"C")


class NanoIndentation(NanoIndentationBasic):
    def __init__(self):
        super().__init__()
        self.add(label="Target strain rate", unit='/s')
        self.add(label="Target loading rate", unit="mN/s")
        self.add(label="Target displacement rate", unit="nm/s")
        self.add(label="Start of averaging depth", unit="nm")
        self.add(label="End of averaging depth", unit="nm")
        self.add(label="Hold time at maximum load", unit='s')
        # Listed later in case of creep test in the docx
        self.sort_fields_by_order_priority()


class NanoIndentationSRJ(NanoIndentationBasic):
    def __init__(self):
        super().__init__()
        self.add(label="Initial strain rate", unit='/s')
        self.add(label="Initial displacement", unit="nm")
        self.add(label="No. of cycles", name="NoOfCycles")
        self.add(label="Final strain rate", unit='/s')
        self.add(label="Displacement range for strain rate ", unit="nm")
        self.sort_fields_by_order_priority()


class NanoIndentationCreep(NanoIndentation):
    def __init__(self):
        super().__init__()
        self.add(label="Creep dwell period", unit='s')
        self.sort_fields_by_order_priority()
