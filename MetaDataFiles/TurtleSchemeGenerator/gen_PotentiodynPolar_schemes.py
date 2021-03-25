from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

micro = "\u03bc"
deg = "\u00b0"
squared = '\u00B2'


class PotentioDynPolarBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Date of preparation", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label="Potential Measurement")
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt='MilliV')
        self.add(label="Counter electrode")


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Time OCP", unit='s')
        self.add(label="Scan velocity", unit="mV/s")
        self.add(label="Scan Start", unit='V')
        self.add(label="Scan End", unit='V')
        self.add(label="Sample area", unit='mm'+squared)
        self.add(label="IR Compensation", field_type='bool')
        self.add(label="Potentiostat")


class PotentioDynPolar(Green, Yellow, PotentioDynPolarBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


potentio_dyn_polar = Scheme("PotentiodynPolar")
potentio_dyn_polar.fields = PotentioDynPolarBasic()
potentio_dyn_polar.write()

potentio_dyn_polar.fields = Yellow()
potentio_dyn_polar.write("PotentiodynPolar_yellow.ttl")

potentio_dyn_polar.fields = Green()
potentio_dyn_polar.write("PotentiodynPolar_green.ttl")

potentio_dyn_polar.fields = PotentioDynPolar()
potentio_dyn_polar.write("PotentiodynPolar_full.ttl")

