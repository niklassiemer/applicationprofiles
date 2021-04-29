from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class IcpMS(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Analyzed elements")
        self.add(label="Isotope")
        self.add(label="Measurement modus", field_type=["STD", "KED"])
        self.add(label="Sweeps")
        self.add(label="Replicates")
        self.sort_fields_by_order_priority()

