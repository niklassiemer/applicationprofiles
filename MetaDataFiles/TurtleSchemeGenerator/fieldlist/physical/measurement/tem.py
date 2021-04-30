from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import SpotMeasurement


class TEM(SpotMeasurement):
    def __init__(self):
        super().__init__()

        # green
        # instrument: self.add(label="Microscope")
        self.add(label="Accelerating voltage", unit="kV")
        self.add(label="Current", unit='mA')
        self.add(label="Acquisition mode")
        self.add(label="Working distance", unit='mm')
        self.add(label="Lighting mode", field_type=['bright field', 'high angle annular dark-field', 'dark field'])
        self.add(label="Operation Mode")
        self.add(label="Magnification / Camera length", name='magnification', unit='mm')
        self.add(label="Electron source")
        self.add(label="Electron dose", unit='e/nm'+squared, qudt="E-PER-NanoM2")
        self.add(label="Dwell time", unit="ms")
        self.add(label="Data dimension")
        self.add(label="1st dimension unit")
        self.add(label="1st dimension pixels")
        self.add(label="1st dimension unit scaling")
        self.add(label="1st dimension starting pixel")
        self.add(label="2nd dimension unit")
        self.add(label="2nd dimension pixels")
        self.add(label="2nd dimension unit scaling")
        self.add(label="2nd dimension starting pixel")

        self.sort_fields_by_order_priority()


