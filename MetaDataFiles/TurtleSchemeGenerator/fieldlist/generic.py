from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList


class SFBFields(FieldList):
    def __init__(self, id_name="ID"):
        super().__init__()
        self.add(label=id_name, name='ID', required=True, order_priority=1, sh_path='dcterms:identifier',
                 comment="ID for the object, be it sample, experiment, sim...")
        self.add(label="User", required=True, order_priority=1, comment="The user responsible for this digital record.",
                 sh_path='dcterms:creator', default_value="{ME}")
        self.add(label="Date", required=True, order_priority=1, sh_path='dcterms:created', default_value="{TODAY}",
                 comment="Date of the current digital record; Default is today.", field_type="date")
        self.add(label="Affiliation")
        self.add(label="DOIs", long=True, comment="To associate publications produced using this object.",
                 sh_path='dcterms:isReferencedBy')
        self.add(label="Comments", long=True, order_priority=-1)  # Last entry in the Scheme