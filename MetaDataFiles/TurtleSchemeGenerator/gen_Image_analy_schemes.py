from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.image_analysis import (
    ImageAnalysisBasic,
    Yellow,
    Green,
    Grey,
    ImageAnalysis
)

SchemeName = "ImageAnalysis"
ImageAnalysis_scheme = Scheme(SchemeName)
ImageAnalysis_scheme.fields = ImageAnalysisBasic()
ImageAnalysis_scheme.write()

ImageAnalysis_scheme.fields = Green()
ImageAnalysis_scheme.write(SchemeName+"_green.ttl")

ImageAnalysis_scheme.fields = Grey()
ImageAnalysis_scheme.write(SchemeName+"_grey.ttl")

ImageAnalysis_scheme.fields = Yellow()
ImageAnalysis_scheme.write(SchemeName+"_yellow.ttl")

ImageAnalysis_scheme.fields = ImageAnalysis()
ImageAnalysis_scheme.write(SchemeName+"_full.ttl")

