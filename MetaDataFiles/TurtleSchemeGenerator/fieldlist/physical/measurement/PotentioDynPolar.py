from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class PotentioDynPolar(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Potential Measurement")
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")

        # green fields
        self.add(label="Time OCP", unit='s')
        self.add(label="Scan velocity", unit="mV/s")
        self.add(label="Scan Start", unit='V')
        self.add(label="Scan End", unit='V')
        self.add(label="Sample area", unit='mm'+squared)
        self.add(label="IR Compensation", field_type='bool')
        self.add(label="Potentiostat")

        self.sort_fields_by_order_priority()
