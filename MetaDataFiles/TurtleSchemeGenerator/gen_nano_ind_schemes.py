from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.measurement.nano_indentation import (NanoIndentation,
                                                                                                 NanoIndentationSRJ,
                                                                                                 NanoIndentationCreep)

nano_ind_scheme = MetaDataSchemes("NanoIndentation")
nano_ind_scheme.fields = NanoIndentation()
nano_ind_scheme.write()
nano_ind_scheme.write(file_extension="txt")

nano_ind_scheme_srj = MetaDataSchemes("NanoIndentationSRJ")
nano_ind_scheme_srj.fields = NanoIndentationSRJ()
nano_ind_scheme_srj.write()
nano_ind_scheme_srj.write(file_extension="txt")

creep_test = MetaDataSchemes("NanoIndentationCreep")
creep_test.fields = NanoIndentationCreep()
creep_test.write()
creep_test.write(file_extension="txt")

with open("nano_indentation_additional_terms.ttl", 'w', encoding='utf8') as f:
    for field in nano_ind_scheme.full_field_list:
        f.write(field.ttl_term_str)
