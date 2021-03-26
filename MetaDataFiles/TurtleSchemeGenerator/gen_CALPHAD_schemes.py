from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.calphad_db import CalphadDBBasic, CalphadDBGreen, \
    CalphadDBGrey, CalphadDB

CALPHAD_DB = Scheme("Calphad_db")
CALPHAD_DB.fields = CalphadDBBasic()
CALPHAD_DB.write()

CALPHAD_DB.fields = CalphadDBGreen()
CALPHAD_DB.write("Calphad_db_green.ttl")

CALPHAD_DB.fields = CalphadDBGrey()
CALPHAD_DB.write("Calphad_db_grey.ttl")

CALPHAD_DB.fields = CalphadDB()
CALPHAD_DB.write("Calphad_db_full.ttl")

