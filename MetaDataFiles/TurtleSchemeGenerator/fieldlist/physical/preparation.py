from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity, Experiment


class Casting(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Nominal composition", required=True)
        self.add(label="Production batch designation")
        raise NotImplementedError("We don't have information from the S-project.")


class Rolling(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Roller diameter")
        self.add(label="Speed")
        self.add(label="Temperature")
        raise NotImplementedError("We don't have information from the S-project.")


class Annealing(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Temperature")
        self.add(label="Time")
        raise NotImplementedError("We don't have information from the S-project.")


class Storage(Annealing):
    # Honestly, unless you're doing weird storage it really is long-time ambient condition annealing!
    # But the subclass reveals the intent of the processing, and could have different defaults
    pass


class Division(PhysicalActivity):
    def __init__(self):
        super().__init__()
        raise NotImplementedError("We don't have information from the S-project.")


class ThinFilm(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Substrate rotation", field_type='bool')
        self.add(label="Substrate temperature", unit=deg + 'C')

        # Grey fields
        us = micro+'s'  # TODO: clarify! In the docx this is 'us'
        # Substrate info
        self.add(label="Substrate material")
        self.add(label="Substrate geometry and size")
        # 1:
        self.add(label="Substrate bias type", field_type=['floating', 'DC', 'pulsed DC', 'RF', 'HPPMS', 'grounded'])
        # depending on 1 : If pulsed DC, pulsed DC, RF or HPPMS is chosen
        self.add(label="Bias power generator",
                 comment="If 'Substrate bias type' is 'DC', 'pulsed DC', 'RF', or 'HPPMS' (not applicable in CoScInE)")
        self.add(label="Substrate voltage", unit='V',
                 comment="If 'Substrate bias type' is 'DC', 'pulsed DC', 'RF', or 'HPPMS' (not applicable in CoScInE)")
        # depending on 1 if pulsed DC is chosen
        self.add(label="Frequency", unit='kHz',
                 comment="If 'Substrate bias type' is 'pulsed DC' (not applicable in CoScInE)")
        self.add(label="Pulse time", unit=us,
                 comment="If 'Substrate bias type' is 'pulsed DC' (not applicable in CoScInE)")
        # depending on 1 if HPPMS is chosen
        self.add(label='On-time', unit=us,
                 comment="If 'Substrate bias type' is 'HPPMS' (not applicable in CoScInE)")
        self.add(label='Off-time', unit=us,
                 comment="If 'Substrate bias type' is 'HPPMS' (not applicable in CoScInE)")
        # Deposition parameters
        self.add(label="Base pressure (at room temperature)", name="BaseTatRT", unit='mbar')
        self.add(label="Base pressure (at synthesis temperature)", name="BaseTatST", unit='mbar')
        self.add(label="Setpoint temperature", unit=deg+'C')
        self.add(label="Heating time", unit='min')
        self.add(label="Argon working gas flow", unit='%', qudt="PERCENT")
        self.add(label="Working gas pressure", unit='Pa')
        self.add(label="Deposition time", unit='min')
        # Magnetron settings
        self.add(label="Magnetron ID")
        self.add(label="Magnetron: Target type", name="MagnTarget")
        self.add(label="Magnetron: Power generator", name="MagnPowerGen")
        # 2:
        self.add(label="Magnetron: Power mode", name="MagnPowerMode",
                 field_type=['DC', 'pulsed DC', 'RF', 'HPPMS'])
        self.add(label="Magnetron: Set power", name="MagnPowerSet", unit='W')
        # depending on 2 if DC is chosen
        self.add(label='Frequency', unit='kHz',
                 comment="if DC is chosen for Magnetron Power mode (not applicable on CoScInE)")
        self.add(label="Pulse time", unit=us,
                comment="if DC is chosen for Magnetron Power mode (not applicable on CoScInE)")
        # depending on 2 if HPPMS is chosen
        self.add(label="On-time", unit=us,
                comment="if HPPMS is chosen for Magnetron Power mode (not applicable on CoScInE)")
        self.add(label="Off-time", unit=us,
                comment="if HPPMS is chosen for Magnetron Power mode (not applicable on CoScInE)")
        # To be implemented also for Magnetron B and C ???
        # Added Magnetron ID field - I hope this captures this! TODO: clarify!
        self.add(label="Capping Layer")
        self.add(label="Capping thickness", unit='nm')

        self.sort_fields_by_order_priority()


class Polishing(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Grit 1")
        self.add(label="Solvent grit 1")
        self.add(label="Grit 2")
        self.add(label="Solvent grit 2")
        self.add(label="Grit material")
        self.add(label="Polishing Suspension", unit=micro + 'm')
        self.add(label="Material Suspension")
        self.add(label="Solvent")


class Immersion(PhysicalActivity):
    def __init__(self):
        super().__init__()
        # This should be the ID?!
        # self.add(label='Immersion experiment ID')
        self.add(label="Immersion experiment routine")
        self.add(label="Electrolyte pH", qudt='PH')
        self.add(label="Electrolyte condition")
        self.add(label="Flow rate", unit="ml/h")
        self.add(label="Revolutions per minute", unit='rpm', qudt='PER-MIN')
        self.add(label="Volume", unit='ml')
        # grey
        self.add(label="Temperature", unit=deg+'C')


class Etching(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Chemicals")
        self.add(label="Duration", unit="s")


class SamplePreparation(Etching, Immersion, Polishing, Experiment):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()
