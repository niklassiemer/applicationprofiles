from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataField as Field, FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class ImageAnalysisBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Python function"),
            Field(label="Python module"),
            Field(label="Git repository"),
            Field(label="Commit hash"),
            Field(label="Python version"),
            Field(label="Python package versions"),
            Field(label="Parameters", long=True),
            # Parameter file
            Field(label="Input image(s)", name="inputImages"),
            Field(label="Minimization algorithm"),
            Field(label="Maximum number of iterations"),
            Field(label="Stopping criterion"),
            Field(label="Regularizer coefficient(s)", name='regularizerCoefficients', long=True),
            # Segmentation parameters
            Field(label="Number of segments"),
            Field(label="Feature extractor"),
            Field(label="Feature size"),
            # Defect detection parameters
            Field(label="Defect type"),
            Field(label="Unit cell vectors", unit="nm")
        ]


class Yellow(FieldList):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Image width", unit='nm'),
            Field(label="Image height", unit='nm'),
        ]


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label="Other parameters specific to the minimization algorithm"),
            Field(label="Other segmentation parameters"),
            Field(label="Other defect detection parameters")
        ]


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        self._fields += [
            Field(label='CPU info'),
            Field(label='Used codes'),
            Field(label='Required RAM', unit='GB'),
            Field(label="Runtime", unit='h'),
        ]


class ImageAnalysis(Grey, Green, Yellow, ImageAnalysisBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()