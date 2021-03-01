from data_scheme import MetaDataSchemes as Scheme, FieldList, SFBFields

generic_SFB = SFBFields()

generic = Scheme("Generic")
generic.fields = generic_SFB
generic.write()

