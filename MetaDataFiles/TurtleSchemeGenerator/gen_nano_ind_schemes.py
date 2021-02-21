from data_scheme import MetaDataSchemes as Scheme, FieldList

nano_ind_blue = FieldList()
nano_ind_blue.add(label="Experiment ID", required=True)
nano_ind_blue.add(label="Operator", required=True)
nano_ind_blue.add(label="Specimen ID")
nano_ind_blue.add(label="Parent sample specimen ID", name="parentSample")
nano_ind_blue.add(label="Sample Location")
nano_ind_blue.add(label="Instrument used", name="instrument")
nano_ind_blue.add(label="Tip used", name="tip")
nano_ind_blue.add(label="Comments", long=True)

nano_ind_grey = FieldList()
nano_ind_grey.add(label="Relative Humidity", unit='%')
nano_ind_grey.add(label="Environmental protection during specimen testing", name="TestingEnv")
nano_ind_grey.add(label="Environmental gas")
nano_ind_grey.add(label="Test date", field_type="date")

nano_ind_yellow = FieldList()
nano_ind_yellow.add(label="Preparation routine", long=True)
nano_ind_yellow.add(label="Preparation Date", field_type="date", long=True)
nano_ind_yellow.add(label="Sample storage")
nano_ind_yellow.add(label="Sample Orientation", long=True)

nano_ind_green = FieldList()
nano_ind_green.add(label="Type of test")
nano_ind_green.add(label="Tip ID")
nano_ind_green.add(label="Diamond area function")
nano_ind_green.add(label="Date of Calibration", field_type="date")
nano_ind_green.add(label="Frame stiffness", unit='N/m')
nano_ind_green.add(label="Target load", unit="mN")
nano_ind_green.add(label="Target depth", unit="nm")
nano_ind_green.add(label="Target strain rate", unit='/s')
nano_ind_green.add(label="Continuous stiffness measurement", field_type='bool')
nano_ind_green.add(label="Start of averaging depth", unit="nm")
nano_ind_green.add(label="End of averaging depth", unit="nm")
nano_ind_green.add(label="Drift correction enabled", field_type="bool")
nano_ind_green.add(label="Sample temperature", unit="\u00b0C")
nano_ind_green.add(label="Tip temperature", unit="\u00b0C")

nano_ind = Scheme("NanoIndentation")
nano_ind.fields = nano_ind_blue
nano_ind.write("Nano-intendation.ttl")

nano_ind.fields = nano_ind_grey
nano_ind.write("Nano-intendation_gray.ttl")

nano_ind.fields = nano_ind_green
nano_ind.write("Nano-intendation_green.ttl")

nano_ind.fields = nano_ind_yellow
nano_ind.write("Nano-intendation_yellow.ttl")

nano_ind.fields = nano_ind_blue + nano_ind_grey + nano_ind_green + nano_ind_yellow
nano_ind.write("Nano-intendation_full.ttl")
