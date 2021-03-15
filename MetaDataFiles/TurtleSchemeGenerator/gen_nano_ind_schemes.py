from data_scheme import MetaDataSchemes as Scheme, FieldList
from data_scheme import DropdownList, SFBFields, MetaDataField

nano_ind_blue = FieldList()
nano_ind_blue.add(label="Experiment ID", required=True)
nano_ind_blue.add(label="Operator", required=True)
nano_ind_blue.add(label="Specimen ID", sh_path="csmd:investigation_sample")
nano_ind_blue.add(label="Parent sample specimen ID", name="parentSample")
nano_ind_blue.add(label="Sample Location")
nano_ind_blue.add(label="Instrument used", name="instrument")
nano_ind_blue.add(label="Tip used", name="tip")
nano_ind_blue.add(label="Test location on sample")
nano_ind_blue.add(label="Type of test")
nano_ind_blue.add(label="Control method")
nano_ind_blue.add(label="Tip ID")
nano_ind_blue.add(label="Diamond area function")
nano_ind_blue.add(label="Date of Calibration", field_type="date")
nano_ind_blue.add(label="Frame stiffness", unit='N/m', other_relations={"qudt:Unit": "unit:N-PER-M"})
nano_ind_blue.add(label="Comments", long=True)

nano_ind_grey = FieldList()
nano_ind_grey.add(label="Relative Humidity", unit='%', other_relations={"qudt:Unit": "unit:PERCENT_RH"})
nano_ind_grey.add(label="Environmental protection during specimen testing", name="TestingEnv")
nano_ind_grey.add(label="Environmental gas")
nano_ind_grey.add(label="Test date", field_type="date")

nano_ind_yellow = FieldList()
nano_ind_yellow.add(label="Preparation routine", long=True)
nano_ind_yellow.add(label="Sample storage")
nano_ind_yellow.add(label="Preparation Date", field_type="date", long=True)
nano_ind_yellow.add(label="Etching routine")
nano_ind_yellow.add(label="Sample Orientation", long=True)
nano_ind_yellow.add(label="Experiment IDs of other tests performed on the same specimen", long=True)
nano_ind_yellow.add(label='Any data set to be linked with this experiment', long=True)

nano_ind_green = FieldList()
nano_ind_green.add(label="Target load", unit="mN", other_relations={"qudt:Unit": "unit:MilliN"})
nano_ind_green.add(label="Target depth", unit="nm", other_relations={"qudt:Unit": "unit:NanoM"})
nano_ind_green.add(label="Target strain rate", unit='/s', other_relations={"qudt:Unit": "unit:PER-SEC"})
nano_ind_green.add(label="Target loading rate", unit="mN/s", other_relations={"qudt:Unit": "unit:MilliN-PER-SEC"})
nano_ind_green.add(label="Target displacement rate", unit="nm/s", other_relations={"qudt:Unit": "unit:NanoM-PER-SEC"})
nano_ind_green.add(label="Continuous stiffness measurement", field_type='bool')
nano_ind_green.add(label="Start of averaging depth", unit="nm", other_relations={"qudt:Unit": "unit:NanoM"})
nano_ind_green.add(label="End of averaging depth", unit="nm", other_relations={"qudt:Unit": "unit:NanoM"})
nano_ind_green.add(label="Hold time at maximum load", unit='s', other_relations={"qudt:Unit": "unit:SEC"})
nano_ind_green.add(label="Drift correction enabled", field_type="bool")
nano_ind_green.add(label="Sample temperature", unit="\u00b0C", other_relations={"qudt:Unit": "unit:DEG_C"})
nano_ind_green.add(label="Tip temperature", unit="\u00b0C", other_relations={"qudt:Unit": "unit:DEG_C"})

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

basic_scheme = Scheme("NanoIndentation/basic")
basic_scheme.fields = SFBFields(id_name="Experiment ID")

# Missing blue fields:
nano_ind_blue = FieldList()
nano_ind_blue.add(label="Specimen ID", sh_path="csmd:investigation_sample", order_priority=2)
nano_ind_blue.add(label="Parent sample specimen ID", name="parentSample", order_priority=2)
nano_ind_blue.add(label="Sample Location", order_priority=2)
nano_ind_blue.add(label="Instrument used", name="instrument", sh_path="csmd:investigation_instrument")
nano_ind_blue.add(label="Tip used", name="tip")
nano_ind_blue.add(label="Test location on sample")
nano_ind_blue.add(label="Type of test")
nano_ind_blue.add(label="Control method")
nano_ind_blue.add(label="Tip ID")
nano_ind_blue.add(label="Diamond area function")
nano_ind_blue.add(label="Date of Calibration", field_type="date")
nano_ind_blue.add(label="Frame stiffness", unit='N/m', other_relations={"qudt:Unit": "unit:N-PER-M"})

sample_origin_scheme = Scheme("NanoIndentation/SampleOrigin", extends=basic_scheme)
sample_origin_scheme.fields = nano_ind_yellow

nano_ind_scheme = Scheme("NanoIndentation", extends=sample_origin_scheme)
nano_ind_scheme.order_fields_by_priority = True
nano_ind_scheme.fields = nano_ind_blue + nano_ind_green + nano_ind_grey

nano_ind_scheme.write()

with open("nano_indentation_additional_terms.ttl", 'w') as f:
    for field in nano_ind_scheme.full_field_list:
        f.write(field.ttl_term_str)
