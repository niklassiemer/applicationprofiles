from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataField as Field, FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class LightMicroscopeBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Date of preparation", field_type='date'),
            Field(label='Sample storage'),
            Field(label="Pre-treatment"),
            Field(label="Instrument used"),
            Field(label="Position sample"),
            Field(label="Filter"),
            Field(label="Magnification"),
            Field(label="Scale", unit=micro+'m/px', qudt='MicroM-PER-NUM')
        ]


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Parent sample specimen ID"),
            Field(label="Specimen ID"),
            Field(label="Preparation routine"),
            Field(label="Immersion Experiment ID")
        ]


class LightMicroscope(Yellow, LightMicroscopeBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()