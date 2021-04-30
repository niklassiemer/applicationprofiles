from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import Experiment


class TensileCompressionBasic(Experiment):
    def __init__(self):
        super().__init__()
        self.add(label="Sample location", example_input="Longitudinal cross-section; from top surface")
        self.add('In-situ / Quasi-in-situ', field_type="bool", name='inSitu',
                 comment="If false skip preparation and etching routines")
        self.add(label="Type of loading", field_type=['tensile', 'compression'])
        self.add(label="State of stress")
        self.add(label="Sample geometry", field_type=['flat', 'round'])


class Green(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label='Specimen dimensions', unit='mm', long=True)
        self.add(label='Temperature of deformation', unit=deg+'C')
        self.add(label='Strain rate', unit='/s')
        self.add(label='Software used for data analysis')


class TensileCompression(Green, TensileCompressionBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
