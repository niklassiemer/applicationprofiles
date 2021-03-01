from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Creator"),
    Field(label='Affiliation'),
    # This will not be unique:
    Field(label="Database filename"),
    Field(label="Elements included"),
    Field(label="Element data"),
    Field(label="Date", field_type='date'),
    Field(label="Licence"),
    Field(label="Software used to test"),
    Field(label="Comment", long=True),
    Field(label="References"),
    Field(label='DOI')
]

green = [
    # Details of Database content
    Field(label="Phases and models")
]

grey = [
    Field(label="Crystal structure", long=True),
    Field(label="Compounds", long=True)
]


CALPHAD_DB = Scheme("Calphad_db")
CALPHAD_DB.fields = blue
CALPHAD_DB.write()

CALPHAD_DB.fields = green
CALPHAD_DB.write("Calphad_db_green.ttl")

CALPHAD_DB.fields = grey
CALPHAD_DB.write("Calphad_db_grey.ttl")

CALPHAD_DB.fields = blue + green + grey
CALPHAD_DB.write("Calphad_db_full.ttl")

