from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Operator"),
    Field(label='Affiliation'),
    Field(label="Database"),
    Field(label="Date", field_type='date'),
    Field(label="Software used"),
    Field(label="Elements selected"),
    Field(label="Type of calculation"),
    Field(label="Conditions", long=True),
    Field(label="Axes used for stepping or mapping", long=True),
    Field(label="Fixed phases"),
    Field(label="Rejected phases"),
    Field(label="Axes used for plotting", long=True),
    Field(label="Comment", long=True)
]

Calphad_calc = Scheme("Calphad_calc")
Calphad_calc.fields = blue
Calphad_calc.write()
