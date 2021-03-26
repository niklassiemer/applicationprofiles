from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.preparation import ThinFilmBasic, ThinFilmGrey, ThinFilm

thin_film = Scheme("ThinFilm")
thin_film.fields = ThinFilmBasic()
thin_film.write()

thin_film.fields = ThinFilmGrey()
thin_film.write("ThinFilm_grey.ttl")

thin_film.fields = ThinFilm()
thin_film.write("ThinFilm_full.ttl")

