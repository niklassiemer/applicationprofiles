from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import DropdownList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class PreparationRoutine(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Parent sample specimen ID")
        self.add(label="Specimen ID")
        self.add(label="Preparation routine")
        self.add(label="Immersion Experiment ID")


class SKPFM(PreparationRoutine):
    def __init__(self):
        super().__init__()
        KPFM_dropdown = DropdownList(label="KPFM mode", options=['AM', 'FM'])
        self.add(label="Date of preparation", sh_path="dcterms:created", field_type='date')
        self.add(label='Sample storage')
        self.add(label="Pre-treatment")
        self.add(label='AFM mode')
        self.add(label="KPFM mode", field_type=KPFM_dropdown)
        self.add(label="Tip name")
        self.add(label="Working distance", unit='nm')
        self.add(label="Scan velocity", unit='Hz')
        self.add(label="Tip offset voltage", unit='V')
        self.add(label="Applied offset voltage", field_type=['sample', 'tip'])
        self.add(label="Tip alternating Voltage", unit='V')
        self.add(label="Scan area", unit="nm x nm")
        self.add(label="Reference")
        self.add(label="Experiment condition", long=True)

        self.sort_fields_by_order_priority()