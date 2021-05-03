from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg, squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import MeasurementWithDetector


class XRD(MeasurementWithDetector):
    def __init__(self):
        super().__init__()
        self.add(label="Radiation source")
        self.add(label="Current", unit='mA')
        self.add(label="Voltage", unit='kV')
        self.add(label="Scan Mode", field_type=["Bragg-Brentano", "Detector Scan", "unlocked coupled", "Rocking curve"])
        self.add(label="Incidence angle Omega", unit=deg)

        # grey
        self.add(label="Filter")
        self.add(label="Mask size", unit='mm'+squared)
        self.add(label="Scan axis", field_type=["2Theta", "Chi", "Phi"])
        self.add(label="Diffraction angle 2Theta", name='diffractionAngle', unit=deg)
        self.add(label="Rotation angle phi", unit=deg)
        self.add(label="Rotation angle chi", unit=deg)
        self.add(label="Number of frames")
        self.add(label="Measurement time", unit='s')
        self.add(label="Start 2Theta", unit=deg)
        self.add(label="End 2Theta", unit=deg)
        self.add(label="Start Theta", unit=deg)
        self.add(label="End Theta", unit=deg)
        self.add(label="Fixed 2Theta position", unit=deg)
        self.add(label="Step size", unit=deg)
        self.add(label="Time per step", unit='s')

        self.sort_fields_by_order_priority()
