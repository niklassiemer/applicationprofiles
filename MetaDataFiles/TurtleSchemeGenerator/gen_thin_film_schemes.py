from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import SFBFields, FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import deg, micro


class ThinFilmBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Specimen ID")
        self.add(label="Synthesis date/time", name="synthesisTime")
        self.add(label='Instrument used')
        self.add(label="Substrate rotation", field_type='bool')
        self.add(label="Substrate temperature", unit=deg + 'C')
        self.add(label="Capping Layer")


class Grey(FieldList):
    def __init__(self):
        super().__init__()
        us = micro+'s'  # TODO: clarify! In the docx this is us
        # Substrate info
        self.add(label="Substrate material")
        self.add(label="Substrate geometry and size")
        # 1:
        self.add(label="Substrate bias type")
        # depending on 1 : If pulsed DC, pulsed DC, RF or HPPMS is chosen
        self.add(label="Bias power generator")
        self.add(label="Substrate voltage", unit='V')
        # depending on 1 if pulsed DC is chosen
        self.add(label="Frequency", unit='kHz')
        self.add(label="Pulse time", unit=us)
        # depending on 1 if HPPMS is chosen
        self.add(label='On-time', unit=us)
        self.add(label='Off-time', unit=us)
        # Deposition parameters
        self.add(label="Base pressure (at room temperature)", name="BaseTatRT", unit='mbar')
        self.add(label="Base pressure (at synthesis temperature)", name="BaseTatST", unit='mbar')
        self.add(label="Setpoint temperature", unit=deg+'C')
        self.add(label="Heating time", unit='min')
        self.add(label="Argon working gas flow", unit='%', qudt="PERCENT")
        self.add(label="Working gas pressure", unit='Pa')
        self.add(label="Deposition time", unit='min')
        # Magnetron settings
        self.add(label="Magnetron A: Target type", name="MagnATarget")
        self.add(label="Magnetron A: Power generator", name="MagnAPowerGen")
        # 2:
        self.add(label="Magnetron A: Power mode", name="MagnAPowerMode", field_type="class")
        self.add(label="Magnetron A: Set power", name="MagnAPowerSet", unit='W')
        # depending on 2 if DC is chosen
        self.add(label='Frequency', unit='kHz')
        self.add(label="Pulse time", unit=us)
        # depending on 2 if HPPMS is chosen
        self.add(label="On-time", unit=us)
        self.add(label="Off-time", unit=us)
        # To be implemented also for Magnetron B and C ???
        self.add(label="Capping thickness", unit='nm')


class ThinFilm(Grey, ThinFilmBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


thin_film = Scheme("ThinFilm")
thin_film.fields = ThinFilmBasic()
thin_film.write()

thin_film.fields = Grey()
thin_film.write("ThinFilm_grey.ttl")

thin_film.fields = ThinFilm()
thin_film.write("ThinFilm_full.ttl")

