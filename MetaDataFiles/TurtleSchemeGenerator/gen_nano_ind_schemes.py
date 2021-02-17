from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

nano_ind_blue = []
nano_ind_blue.append(Field(label="Experiment ID", required=True))
nano_ind_blue.append(Field(label="Operator", required=True))
nano_ind_blue.append(Field(label="Specimen ID"))
nano_ind_blue.append(Field(label="Parent sample specimen ID", name="parentSample"))
nano_ind_blue.append(Field(label="Sample Location"))
nano_ind_blue.append(Field(label="Instrument used", name="instrument"))
nano_ind_blue.append(Field(label="Tip used", name="tip"))
nano_ind_blue.append(Field(label="Comments", long=True))

nano_ind_grey = []
nano_ind_grey.append(Field(label="Relative Humidity", unit='%'))
nano_ind_grey.append(Field(label="Environmental protection during specimen testing", name="TestingEnv"))
nano_ind_grey.append(Field(label="Environmental gas"))
nano_ind_grey.append(Field(label="Test date", field_type="date"))

nano_ind_yellow = []
nano_ind_yellow.append(Field(label="Preparation routine", long=True))
nano_ind_yellow.append(Field(label="Preparation Date", field_type="date", long=True))
nano_ind_yellow.append(Field(label="Sample storage"))
nano_ind_yellow.append(Field(label="Sample Orientation", long=True))

nano_ind_green = []
nano_ind_green.append(Field(label="Type of test"))
nano_ind_green.append(Field(label="Tip ID"))
nano_ind_green.append(Field(label="Diamond area function"))
nano_ind_green.append(Field(label="Date of Calibration", field_type="date"))
nano_ind_green.append(Field(label="Frame stiffness", unit='N/m'))
nano_ind_green.append(Field(label="Target load", unit="mN"))
nano_ind_green.append(Field(label="Target depth", unit="nm"))
nano_ind_green.append(Field(label="Target strain rate", unit='/s'))
nano_ind_green.append(Field(label="Continuous stiffness measurement", field_type='bool'))
nano_ind_green.append(Field(label="Start of averaging depth", unit="nm"))
nano_ind_green.append(Field(label="End of averaging depth", unit="nm"))
nano_ind_green.append(Field(label="Drift correction enabled", field_type="bool"))
nano_ind_green.append(Field(label="Sample temperature", unit="\u00b0C"))
nano_ind_green.append(Field(label="Tip temperature", unit="\u00b0C"))


nano_ind = Scheme("NanoIndentation")
nano_ind.fields = nano_ind_blue
nano_ind.write("Nano-intendation3.ttl")

nano_ind.fields = nano_ind_blue + nano_ind_grey
nano_ind.write('Nano-intendation_w_gray.ttl')

nano_ind.fields = nano_ind_blue + nano_ind_green + nano_ind_grey + nano_ind_yellow
nano_ind.write('Nano-intendation_full.ttl')
