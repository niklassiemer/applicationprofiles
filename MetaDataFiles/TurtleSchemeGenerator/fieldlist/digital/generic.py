from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList, MetaDataField as Field


class SimTechnical(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Computer name", comment="Name of the Computer / Compute cluster / Queue used.")
        self.add(label="Node", comment="Number of nodes or list of node names.")
        self.add(label='CPU info', comment="Information about the CPUs used.")
        self.add(label='GPU info', comment="Information about the GPUs used.")
        self.add(label="Cores", comment="Number of compute cores used.")
        self.add(label='Required RAM', unit='GB')
        self.add(label="Runtime", unit='h')
        self.add(label="Submission time", field_type="date")
        self.add(label="Stop time", field_type="date")


class ComputeEnvironment(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Python version")
        self.add(label="pyiron version")
        self.add(label="git repository")
        self.add(label="git hash/tag")
        self.add(label="Software used")
        self.add(label="Software versions")
        self.add(label="Software installation procedure")
