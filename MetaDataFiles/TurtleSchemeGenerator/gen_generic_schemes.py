from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import MetaDataSchemes as Scheme, SFBFields

generic_SFB = SFBFields()

generic = Scheme("Generic")
generic.fields = generic_SFB
generic.write()

some_test = Scheme("TEST")
some_test.fields.add(label="test", unit="mm")
some_test.fields.add(label="test2", unit="awfull long unit", qudt='Unit-String')
some_test.write()

