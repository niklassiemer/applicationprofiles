from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class MicroPillar(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Tip ID", name="tip")  # TODO: Make a Tip object
        self.add(label="Test duration")
        self.add(label="Sample location", example_input="Longitudinal cross-section; from top surface")
        self.add(label='Location on sample', example_input="5mm in X and 4 mm in Y from lower left corner")
        self.add(label="Type of test")
        self.add(label="Control Method")
        self.add(label="Diamond area function")
        self.add(label="Date of Calibration", field_type="date")
        self.add(label="Frame stiffness", unit='N/m')
        self.add(label="Target load", unit="mN")
        self.add(label="Target depth", unit="nm")
        self.add(label="Target strain rate", unit='/s')
        self.add(label="Target loading rate", unit='mN/s')
        self.add(label="Continuous stiffness measurement", field_type='bool')
        self.add(label="Drift correction enabled", field_type="bool")
        self.add(label="Sample temperature", unit=deg+"C")
        self.add(label="Tip temperature", unit=deg+"C")

        self.sort_fields_by_order_priority()
