from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro_pillar_blue = []
micro_pillar_blue.append(Field(label="Experiment ID", required=True))
micro_pillar_blue.append(Field(label="Operator", required=True))
micro_pillar_blue.append(Field(label="Specimen ID"))
micro_pillar_blue.append(Field(label="Parent sample specimen ID", name="parentSample"))
micro_pillar_blue.append(Field(label="Sample Location"))
micro_pillar_blue.append(Field(label="Instrument used", name="instrument"))
micro_pillar_blue.append(Field(label="Tip used", name="tip"))
micro_pillar_blue.append(Field(label="Comments", long=True))

micro_pillar_grey = []
micro_pillar_grey.append(Field(label="Relative Humidity", unit='%'))
micro_pillar_grey.append(Field(label="Environmental protection during specimen testing", name="TestingEnv"))
micro_pillar_grey.append(Field(label="Environmental gas"))
micro_pillar_grey.append(Field(label="Test duration"))
micro_pillar_grey.append(Field(label="Test date", field_type="date"))

micro_pillar_yellow = []
micro_pillar_yellow.append(Field(label="Preparation routine", long=True))
micro_pillar_yellow.append(Field(label="Preparation Date", field_type="date", long=True))
micro_pillar_yellow.append(Field(label="Sample storage"))
micro_pillar_yellow.append(Field(label="Pillar Orientation", long=True))

micro_pillar_green = []
micro_pillar_green.append(Field(label="Type of test"))
micro_pillar_green.append(Field(label="Tip ID"))
micro_pillar_green.append(Field(label="Diamond area function"))
micro_pillar_green.append(Field(label="Date of Calibration", field_type="date"))
micro_pillar_green.append(Field(label="Frame stiffness", unit='N/m'))
micro_pillar_green.append(Field(label="Target load", unit="mN"))
micro_pillar_green.append(Field(label="Target depth", unit="nm"))
micro_pillar_green.append(Field(label="Target strain rate", unit='/s'))
micro_pillar_green.append(Field(label="Target loading rate", unit='mN/s'))
micro_pillar_green.append(Field(label="Continuous stiffness measurement", field_type='bool'))
micro_pillar_green.append(Field(label="Drift correction enabled", field_type="bool"))
micro_pillar_green.append(Field(label="Sample temperature", unit="\u00b0C"))
micro_pillar_green.append(Field(label="Tip temperature", unit="\u00b0C"))


micro_pillar = Scheme("Micropillar")
micro_pillar.fields = micro_pillar_blue
micro_pillar.write("micropillar.ttl")

micro_pillar.fields = micro_pillar_grey
micro_pillar.write('micropillar_grey.ttl')

micro_pillar.fields = micro_pillar_yellow
micro_pillar.write('micropillar_yellow.ttl')

micro_pillar.fields = micro_pillar_green
micro_pillar.write('micropillar_green.ttl')

micro_pillar.fields = micro_pillar_blue + micro_pillar_grey
micro_pillar.write('micropillar_w_gray.ttl')

micro_pillar.fields = micro_pillar_blue + micro_pillar_green + micro_pillar_grey + micro_pillar_yellow
micro_pillar.write('micropillar_full.ttl')
