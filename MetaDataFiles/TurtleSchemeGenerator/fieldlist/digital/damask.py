from MetaDataFiles.TurtleSchemeGenerator.data_scheme.data_scheme import FieldList
from MetaDataFiles.TurtleSchemeGenerator.data_scheme.units import squared
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.digital.generic import SimTechnical
from MetaDataFiles.TurtleSchemeGenerator.fieldlist.generic import SFBFields


class DamaskBasic(SFBFields):
    def __init__(self):
        super().__init__()
        self.add(label="Constitutive models")
        self.add(label="Library module")
        self.add(label="Software version")


class DamaskMaterial(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Plasticity model")
        self.add(label="Lattice structure")
        self.add(label="Elastic moduli", unit='Pa')
        self.add(label="Slip families")
        self.add(label="Initial dislocation density", unit='1/m'+squared)
        self.add(label="Peierls stress", unit='Pa')


class DamaskGeometry(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Physical size of the geometry", unit='m')
        self.add(label="Grids of the geometry")


class DamaskBoundaryConditions(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Deformation gradient rate")
        self.add(label="Applied stress", unit='Pa')
        self.add(label="Simulation time", unit='s')
        self.add(label="Numerical increments")


class DamaskNumerical(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Mechanical solver")
        self.add(label="Phase field solver")
        self.add(label="Maximum iterations")
        self.add(label="Maximum cutbacks")


class DamaskCoScInE(SimTechnical, DamaskBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


class Damask(SimTechnical, DamaskNumerical, DamaskBoundaryConditions, DamaskGeometry, DamaskMaterial, DamaskBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()