from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Operator"),
    Field(label="Python function"),
    Field(label="Python module"),
    Field(label="Git repository"),
    Field(label="Commit hash"),
    Field(label="Python version"),
    Field(label="Python package versions"),
    Field(label="Parameters", long=True),
    Field(label="Comment", long=True),
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

yellow = [
    Field(label="Image width", unit='nm'),
    Field(label="Image height", unit='nm'),
]

green = [
    Field(label="Other parameters specific to the minimization algorithm"),
    Field(label="Other segmentation parameters"),
    Field(label="Other defect detection parameters")
]

grey = [
    Field(label='CPU info'),
    Field(label='Used codes'),
    Field(label='Required RAM', unit='GB'),
    Field(label="Runtime", unit='h'),
]

SchemeName = "ImageAnalysis"
ImageAnalysis = Scheme(SchemeName)
ImageAnalysis.fields = blue
ImageAnalysis.write()

ImageAnalysis.fields = green
ImageAnalysis.write(SchemeName+"_green.ttl")

ImageAnalysis.fields = grey
ImageAnalysis.write(SchemeName+"_grey.ttl")

ImageAnalysis.fields = yellow
ImageAnalysis.write(SchemeName+"_yellow.ttl")

ImageAnalysis.fields = blue + green + yellow + grey
ImageAnalysis.write(SchemeName+"_full.ttl")

