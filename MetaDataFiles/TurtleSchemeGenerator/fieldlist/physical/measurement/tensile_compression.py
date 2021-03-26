from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class TensileCompressionBasic(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Type of loading", field_type="class")


class Grey(FieldList):
    def __init__(self):
        super().__init__()


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label='Specimen dimensions', unit='mm', long=True)
        self.add(label='Temperature of deformation', unit=deg+'C')
        self.add(label='Strain rate', unit='/s')
        self.add(label='Software used for data analysis')


class TensileCompression(Grey, Green, TensileCompressionBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
