from MetaDataFiles.TurtleSchemeGenerator.fieldlist.physical.generic import PhysicalActivity


class XPS(PhysicalActivity):
    def __init__(self):
        super().__init__()
        self.add(label="Energy range start", unit='eV')
        self.add(label="Energy range end", unit='eV')
        self.add(label="Etching source")
        self.add(label="Etching energy")
        self.add(label="Etching duration")
        self.add(label="Etching power")
        self.add(label="Anode material")
        self.add(label="Anode power", unit='W')
        self.add(label="Anode voltage", unit='kV')
        self.add(label="Pass energy", unit='eV')
        self.add(label="Working pressure", unit='lg(Torr)', qudt='None')
        self.add(label="Energy resolution", unit='eV')
        self.sort_fields_by_order_priority()
