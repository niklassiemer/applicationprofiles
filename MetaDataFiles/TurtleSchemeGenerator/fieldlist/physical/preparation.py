from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList, MetaDataField as Field
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class EBSDYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Sample storage")
        self.add(label="Date of preparation", field_type='date')
        self.add(label="Etching routine")
        self.add(label="Immersion Experiment ID")
        self.add(label="Experiment IDs of other tests performed on the same specimen", long=True)
        self.add(label='Any data set to be linked with this experiment', long=True,
                 comment="e.g. EBSD_scheme map etc.")

        #    Field(label="Grit 1"),
        #    Field(label="Solvent grit 1"),
        #    Field(label="Grit 2"),
        #    Field(label="Solvent grit 2"),
        #    Field(label="Grit material"),
        #    Field(label="Polishing Suspension", unit=micro + 'm'),
        #    Field(label="Material Suspension"),
        #    Field(label="Fine polishing Suspension"),
        #    Field(label="Solvent Polishing"),
        #    Field(label="Operator", name="etchingOperator"),
        #    Field(label="Etchant"),
        #    Field(label="Parameter"),
        #    Field(label="Comments", long=True),
        pass


class ElChemImpedSpecYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class IcpMsYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class LightMicroscopeYellow(FieldList):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Parent sample specimen ID"),
            Field(label="Specimen ID"),
            Field(label="Preparation routine"),
            Field(label="Immersion Experiment ID")
        ]


class MicroPillarYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")
        self.add(label="Pillar Orientation", long=True)


class PotentioDynPolarYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class ScratchYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")


class SEMYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")


class SIETYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class SVETYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class SynchrotronYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class TEMYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Pre-Preparation routine", long=True)
        self.add(label="Immersion Experiment ID", long=True)
        self.add(label="TEM preparation routine")
        self.add(label="TEM preparation date", field_type="date")
        self.add(label="Operator for sample preparation")
        self.add(label="Sample storage location")
        self.add(label="Sample storage conditions")


class TensileCompressionYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine", long=True)
        self.add(label="Preparation Date", field_type="date", long=True)
        self.add(label="Sample storage")


class XPSYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class XRDYellow(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID", name="parentSample")
        self.add(label="Preparation routine")
        self.add(label='Pre-treatment', field_type='class')
        self.add(label="Sample storage")
        self.add(label="Immersion Experiment ID")


class Polish(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Preparation routine")
        self.add(label="Grit 1")
        self.add(label="Solvent grit 1")
        self.add(label="Grit 2")
        self.add(label="Solvent grit 2")
        self.add(label="Grit material")
        self.add(label="Polishing Suspension", unit=micro + 'm')
        self.add(label="Material Suspension")
        self.add(label="Solvent")


class Immersion(SFBFields):
    def __init__(self):
        super().__init__()
        # This should be the ID?!
        # self.add(label='Immersion experiment ID')
        self.add(label='Immersion experiment routine')
        self.add(label="Electrolyte pH", qudt='PH')
        self.add(label="Electrolyte condition")
        self.add(label="Flow rate", unit="ml/h")
        self.add(label="Revolutions per minute", unit='rpm', qudt='PER-MIN')
        self.add(label="Volume", unit='ml')
        # grey
        self.add(label="Temperature", unit=deg+'C')


class Etching(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Etching routine")
        self.add(label="Operator")
        self.add(label="Chemicals")
        self.add(label="Duration", unit="s")