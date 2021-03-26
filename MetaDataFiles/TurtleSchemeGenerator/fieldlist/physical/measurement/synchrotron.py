from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class SynchrotronBasic(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Radiation type")
        self.add(label="Beam size", unit=micro+'m')
        self.add(label="Photon flux", unit="Photons/s x 10^", qudt='NUM-PER-SEC')
        self.add(label="Energy bandwidth", unit='%', qudt="PERCENT")
        self.add(label="Incoming beam focus", unit=micro+'m'+squared)
        self.add(label="Deflected beam focus", unit=micro+'m'+squared)
        self.add(label="Detector")


class Synchrotron(SynchrotronBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
