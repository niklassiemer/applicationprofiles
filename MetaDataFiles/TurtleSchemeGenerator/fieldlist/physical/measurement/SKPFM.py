from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import DropdownList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class SKPFM(PhysicalActivity):
    def __init__(self):
        super().__init__()
        KPFM_dropdown = DropdownList(label="KPFM mode", options=['AM', 'FM'])
        self.add(label='AFM mode')
        self.add(label="KPFM mode", field_type=KPFM_dropdown)
        self.add(label="Tip ID", name="tip")
        self.add(label="Working distance", unit='nm')
        self.add(label="Scan velocity", unit='Hz')
        self.add(label="Tip offset voltage", unit='V')
        self.add(label="Applied offset voltage", field_type=['sample', 'tip'])
        self.add(label="Tip alternating Voltage", unit='V')
        self.add(label="Scan area", unit="nm x nm")
        self.add(label="Reference")  #???
        self.add(label="Experiment condition", long=True)  #??? This
        # TODO: We haven't gotten enough info from the SKPFM team, those last two are brutally vague

        self.sort_fields_by_order_priority()
