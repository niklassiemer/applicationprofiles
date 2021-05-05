from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import (MeasurementAtSpot, PhysicalObject,
                                                                            PhysicalActivity)
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg

# info:
# The Tip ID is not unique! It refers to a specific Tip which, however, changes its properties over time.
# Thus, the ID of a Tip object != Tip ID


class NanoIndentationBasic(MeasurementAtSpot):
    def __init__(self):
        super().__init__()
        self.add(label="Sample orientation", long=True)

        self.add(label="Type of test")
        self.add(label="Control method")
        self.add(label="Tip ID", name="tipName")  # the TipID used within nano indentation experiments is not unique!
        self.add(label="Diamond area function")   # ToDo: Use the unique TipID (=TipName + Calibration date) only
        self.add(label="Date of calibration", field_type="date")  # Same here
        self.add(label="Frame stiffness", unit='N/m')  # Same here

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
        self.add(label="No. of cycles", name="noOfCycles")
        self.add(label="Final strain rate", unit='/s')
        self.add(label="Displacement range for strain rate ", unit="nm")
        self.sort_fields_by_order_priority()


class NanoIndentationCreep(NanoIndentation):
    def __init__(self):
        super().__init__()
        self.add(label="Creep dwell period", unit='s')
        self.sort_fields_by_order_priority()


class TipCalibration(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label='Calibration sample ID')
        self.add(label='Measurement position', example_input="5mm in X and 4 mm in Y from lower left corner")
        # ToDo refactor NanoIndentationBasic to include all not Tip- or Sample- related fields here.
        self.add(label='Date of calibration', field_type='date')


class Tip(PhysicalObject):
    def __init__(self):
        super().__init__()
        self.add(label="Tip ID", name="tipName")  # the TipID used within nano indentation experiments is not unique!
        self.add(label="Tip calibration ID")
        self.add(label="Diamond area function")
        self.add(label='Frame stiffness', unit='N/m')
