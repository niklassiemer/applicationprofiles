from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.nano_indentation import NanoIndentation

nano_ind_scheme = MetaDataSchemes("NanoIndentation")
nano_ind_scheme.fields = NanoIndentation()
nano_ind_scheme.write()

nano_ind_scheme.fields.write('NanoIndentation.txt')

with open("nano_indentation_additional_terms.ttl", 'w', encoding='utf8') as f:
    for field in nano_ind_scheme.full_field_list:
        f.write(field.ttl_term_str)
