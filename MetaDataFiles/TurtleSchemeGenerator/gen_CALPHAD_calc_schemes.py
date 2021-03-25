from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields

micro = "\u03bc"
deg = "\u00b0"


class CalphadCalc(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Database")
        self.add(label="Date", field_type='date')
        self.add(label="Software used")
        self.add(label="Elements selected")
        self.add(label="Type of calculation")
        self.add(label="Conditions", long=True)
        self.add(label="Axes used for stepping or mapping", long=True)
        self.add(label="Fixed phases")
        self.add(label="Rejected phases")
        self.add(label="Axes used for plotting", long=True)

        self.sort_fields_by_order_priority()


Calphad_calc = Scheme("Calphad_calc")
Calphad_calc.fields = CalphadCalc()
Calphad_calc.write()
