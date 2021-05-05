from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class SimTechnical(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Software IDs", comment="Names/IDs of the Software used.")
        self.add(label="Software environment ID", comment="ID of the software environment including exact versions.")
        self.add(label="Computer name", comment="Name of the Computer / Compute cluster / Queue used.",
                 order_priority=-100)
        self.add(label="Node", comment="Number of nodes or list of node names.", order_priority=-100)
        self.add(label='CPU info', comment="Information about the CPUs used.", order_priority=-100)
        self.add(label='GPU info', comment="Information about the GPUs used.", order_priority=-100)
        self.add(label="Cores", comment="Number of compute cores used.", order_priority=-100)
        self.add(label='Required RAM', unit='GB', order_priority=-100)
        self.add(label="Runtime", unit='h', order_priority=-100)
        self.add(label="Submission time", field_type="date", order_priority=-100)
        self.add(label="Stop time", field_type="date", order_priority=-100)


class ComputeEnvironment(SFBFields):
    """Like a conda environment file, however, may also include non-conda software."""
    def __init__(self):
        super().__init__()
        self.add(label="Python version")
        self.add(label="Software IDs", long=True)

        self.sort_fields_by_order_priority()


class Software(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label='Name')
        self.add(label='Version')
        self.add(label='Licence')
        self.add(label="git repository")
        self.add(label="git hash/tag", name="gitHash")
        self.add(label="Software installation procedure")

        self.sort_fields_by_order_priority()


class CompiledSoftware(Software):
    def __init__(self):
        super().__init__()
        self.add(label="Compiler")
        self.add(label="Compiler version")
        self.add(label="Compiler options")
        self.add(label="Makefile")
        self.add(label="Dependency Software IDs", example_input="MKL_2021_1, FFTW_3",
                 comment="Other (compiled) software which is needed to compile this software (mostly libraries).")

        self.sort_fields_by_order_priority()
