from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import micro, deg
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity, PreSample


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


class Cut(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Cutting position")
        raise NotImplementedError("We don't have information from the S-project.")


class ThinFilm(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Substrate rotation", field_type='bool')
        self.add(label="Substrate temperature", unit=deg + 'C')

        # Grey fields
        us = micro+'s'
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
        # Same possible settings for three Magnetrons (A,B,C):
        for mag in ['A', 'B', 'C']:
            # IMO it would make sense to have one sh_path for these fields, however, I do not know how to handle the
            #     different labels in the ontology framework...
            self.add(label=f"Magnetron {mag}: Target type",
                     name=f"magn{mag}Target",
                     # sh_path='sfb1394:magnTarget'
                     )
            self.add(label=f"Magnetron {mag}: Power generator",
                     name=f"magn{mag}PowerGen",
                     # sh_path='sfb1394:magnPowerGen'
                     )
            # 2:
            self.add(label=f"Magnetron {mag}: Power mode",
                     name=f"magn{mag}PowerMode",
                     # sh_path='sfb1394:magnPowerMode',
                     field_type=['DC', 'pulsed DC', 'RF', 'HPPMS']
                     )
            self.add(label=f"Magnetron {mag}: Set power",
                     name=f"magn{mag}PowerSet",
                     # sh_path='sfb1394:magnPowerSet',
                     unit='W'
                     )
            # depending on 2 if DC is chosen
            self.add(label=f'Magnetron {mag}: Frequency',
                     unit='kHz',
                     name=f"magn{mag}Freq",
                     # sh_path='sfb1394:magnFreq',
                     comment=f"if DC is chosen for Magnetron {mag} Power mode (not applicable on CoScInE)"
                     )
            self.add(label=f"Magnetron {mag}: Pulse time",
                     name=f'magn{mag}PulseTime',
                     unit=us,
                     # sh_path='sfb1394:magnPulseTime',
                     comment=f"if DC is chosen for Magnetron {mag} Power mode (not applicable on CoScInE)"
                     )
            # depending on 2 if HPPMS is chosen
            self.add(label=f"Magnetron {mag}: On-time",
                     name=f'magn{mag}OnTime',
                     unit=us,
                     # sh_path='sfb1394:magnOnTime',
                     comment=f"if HPPMS is chosen for Magnetron {mag} Power mode (not applicable on CoScInE)"
                     )
            self.add(label=f"Magnetron {mag}: Off-time",
                     name=f'magn{mag}OffTime',
                     unit=us,
                     # sh_path='sfb1394:magnOffTime',
                     comment=f"if HPPMS is chosen for Magnetron {mag} Power mode (not applicable on CoScInE)"
                     )
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
        self.add(label="Polishing suspension", unit=micro + 'm')
        self.add(label="Material suspension")
        self.add(label="Solvent")
        self.sort_fields_by_order_priority()


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
        self.sort_fields_by_order_priority()


class Etching(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Chemicals")
        self.add(label="Duration", unit="s")
        self.sort_fields_by_order_priority()


class Sample(Etching, Immersion, Polishing,  # ToDo: include:  Cut, etc.,
             PreSample):
    def __init__(self):
        super().__init__()
        self.add(label="Order of operation", comment='If multiple modifications to the sample are performed ('
                                                     'Only for perfectly contiguous preparations), '
                                                     'provide the order of the operations.')

        self.sort_fields_by_order_priority()
