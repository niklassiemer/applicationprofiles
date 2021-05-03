from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class ElChemImpedSpec(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Mode")
        self.add(label="Alternating current", unit='mA')
        self.add(label="Alternating voltage", unit='mV')
        self.add(label="Reference electrode potential", unit='mV(SHE)', qudt="MilliV")
        self.add(label="Counter electrode")

        # green
        self.add(label="Potentiostat")
        self.add(label="Time OCP", unit='s')
        self.add(label="Frequency start", unit='Hz')
        self.add(label="Frequency end", unit='Hz')

        self.sort_fields_by_order_priority()
