from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.SKPFM import SKPFM

SKPFM_scheme = Scheme('SKPFM')
SKPFM_scheme.fields = SKPFM()

SKPFM_scheme.fields.write('SKPFM.txt')

SKPFM_scheme.write()
with open("SKPFM_additional_terms.ttl", 'w') as f:
    for field in SKPFM_scheme.full_field_list:
        f.write(field.ttl_term_str)
