from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class CalphadDB(SFBFields):
    def __init__(self):
        super().__init__()
        # This will not be unique:
        self.add(label="Database filename")
        self.add(label="Elements included", example_input='[Al, Ca, Mg]')
        self.add(label="Element data")
        self.add(label="Date", field_type='date')
        self.add(label="Licence")
        self.add(label="Software used to test", example_input='Thermo-Calc 2020b')
        # TODO: What is the purpose?
        self.add(label="References")

        # green
        self.add(label="Phases and models", example_input='[C15_LAVES, sublattice, 2 2 1, Al Ca Mg, Al Ca Mg]',
                 comment="One line for each phase. First (int) is number of sublattices followed by number of sites"
                         " on each sublattice (float) and the occupation of each sublattice (string).")

        # grey
        self.add(label="Crystal structure", long=True, example_input='[C15_LAVES, Cu2Mg, cF24, Fd-3m (227)]',
                 comment='One line for each phase. Phase name, prototype, Pearson symbol, Space group')
        self.add(label="Compounds", long=True, example_input='[C15_LAVES, (Al,Mg)2Ca]',
                 comment='One line for each phase. Phase name, known compounds')

        self.sort_fields_by_order_priority()
