from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class AtomProbeTomography(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Lift-out region", long=True)
        self.add(label="Annular milling parameters", long=True)
        self.add(label="Low voltage cleaning")
        self.add(label="Mode")
        self.add(label="Pulse fraction", unit='%', qudt="PERCENT")
        self.add(label="Laser pulse energy", unit="pJ")
        self.add(label="Pulse frequency", unit='kHz')
        self.add(label="Base temperature", unit="K")
        self.add(label="Detection rate", unit="%", qudt="PERCENT")
        self.add(label="Run time", unit="min")
        self.add(label="Stop voltage", unit="kV")
        self.add(label="Acquired ions", unit="10^6", qudt='NUM')

        self.sort_fields_by_order_priority()


