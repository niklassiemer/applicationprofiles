from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalObject


class Sample(PhysicalObject):
    def __init__(self):
        super().__init__()
        self.add(label="Parent ID", name="parentSample", comment="The super-sample from which this came.")
        self.add(
            label="Preparation IDs",
            comment="What was done to this sample that differentiates it from its parent, in order of operation. "
                    "Multiple routines should only be given for perfectly contiguous sample chains."
        )
        self.sort_fields_by_order_priority()
