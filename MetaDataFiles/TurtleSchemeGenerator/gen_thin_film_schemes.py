from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Operator"),
    Field(label="Specimen ID"),
    Field(label="Synthesis date/time", name="synthesisTime"),
    Field(label='Instrument used'),
    Field(label="Comments"),
    Field(label="Substrate rotation", field_type='bool'),
    Field(label="Substrate temperature", unit=deg + 'C'),
    Field(label="Capping Layer")
]

us = 'us'
grey = [
    # Substrate info
    Field(label="Substrate material"),
    Field(label="Substrate geometry and size"),
    # 1:
    Field(label="Substrate bias type"),
    # depending on 1 : If pulsed DC, pulsed DC, RF or HPPMS is chosen
    Field(label="Bias power generator"),
    Field(label="Substrate voltage", unit='V'),
    # depending on 1 if pulsed DC is chosen
    Field(label="Frequency", unit='kHz'),
    Field(label="Pulse time", unit=us),
    # depending on 1 if HPPMS is chosen
    Field(label='On-time', unit=us),
    Field(label='Off-time', unit=us),
    # Deposition parameters
    Field(label="Base pressure (at room temperature)", name="BaseTatRT", unit='mbar'),
    Field(label="Base pressure (at synthesis temperature)", name="BaseTatST", unit='mbar'),
    Field(label="Setpoint temperature", unit=deg+'C'),
    Field(label="Heating time", unit='min'),
    Field(label="Argon working gas flow", unit='%'),
    Field(label="Working gas pressure", unit='Pa'),
    Field(label="Deposition time", unit='min'),
    # Magnetron settings
    Field(label="Magnetron A: Target type", name="MagnATarget"),
    Field(label="Magnetron A: Power generator", name="MagnAPowerGen"),
    # 2:
    Field(label="Magnetron A: Power mode", name="MagnAPowerMode", field_type="class"),
    Field(label="Magnetron A: Set power", name="MagnAPowerSet", unit='W'),
    # depending on 2 if DC is chosen
    Field(label='Frequency', unit='kHz'),
    Field(label="Pulse time", unit=us),
    # depending on 2 if HPPMS is chosen
    Field(label="On-time", unit=us),
    Field(label="Off-time", unit=us),
    # To be implemented also for Magnetron B and C ???
    Field(label="Capping thickness", unit='nm')
]

thin_film = Scheme("ThinFilm")
thin_film.fields = blue
thin_film.write()

thin_film.fields = grey
thin_film.write("ThinFilm_grey.ttl")

thin_film.fields = blue + grey
thin_film.write("ThinFilm_full.ttl")

