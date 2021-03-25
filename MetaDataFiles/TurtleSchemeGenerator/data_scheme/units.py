deg = "\u00b0"
angstrom = "\u212B"
micro = "\u03bc"
squared = '\u00B2'
cubic = '\u00B3'
qudt_unit_relations = {
    "mm": "MilliM",
    "ms": "MilliSec",
    "nm": "NanoM",
    deg+"C": "Deg_C",
    "V": "V",
    "Hz": "HZ",
    "s": "SEC",
    "N/m": "N-PER-M",
    "mN": "MilliN",
    "/s": "PER-SEC",
    "mN/s": "MilliN-PER-SEC",
    "nm/s": "NanoM-PER-SEC",
    "nm x nm": "NanoM2",
    "fs": "FemtoSEC",
    "eV": "EV",
    "eV/"+angstrom: "EV-PER-ANGSTROM",
    'ps': "PicoSEC",
    'GPa': "GigaPA",
    'K': 'K',
    'm/s': 'M-PER-SEC',
    'eV/'+angstrom+squared: "EV-PER-ANGSTROM2",
    "GB": "GigaBYTE",
    'h': 'HR',
    'Pa': 'PA',
    '1/m'+squared: 'PER-M2',
    'm': 'M',
    'kV': 'KiloV',
    'kHz': "KiloHZ",
    'nA': 'NanoA',
    micro+'m': 'MicroM',
    micro+'s': "MicroSec",
    'mbar': "MilliBAR",
    micro+'m(width) x '+micro+'m(height)': "MicroM2",
    deg: "DEG",
    'mA': "MilliA",
    'W': 'W',
    'mV': "MilliV",
    'min': "MIN",
    'mV/s': "MilliV-PER-SEC",
    'mm'+squared: "MilliM2",
    'ml': 'MilliL',
    'ml/h': "MilliL-PER-HR",
    micro+'m/s': 'MicroM-PER-SEC',
    micro+'m'+squared: 'MicroM2'
}


def _gen_unit_relation(unit, qudt=False):
    if qudt:
        return ["qudt:Unit", "unit:"+unit]
    return ["qudt:Unit", "unit:" + qudt_unit_relations[unit]]