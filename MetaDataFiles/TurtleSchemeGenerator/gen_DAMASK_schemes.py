from data_scheme import MetaDataSchemes as Scheme
from data_scheme import FieldList, SFBFields

micro = "\u03bc"
deg = "\u00b0"
squared = '\u00B2'


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


class DamaskGrey(FieldList):
    def __init__(self):
        super().__init__()
        self.add(label="Cluster name")
        self.add(label='CPU info')
        self.add(label='cores')
        self.add(label='Required RAM', unit='GB')
        self.add(label="Runtime", unit='h')
        self.add(label="Submission time")
        self.add(label="Stop time")


class DamaskCoScInE(DamaskGrey, DamaskBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


class Damask(DamaskGrey, DamaskNumerical, DamaskBoundaryConditions, DamaskGeometry, DamaskMaterial, DamaskBasic):
    def __init__(self):
        super().__init__()
        self.sort_fields_by_order_priority()


DAMASK = Scheme("DAMASK")
DAMASK.fields = DamaskCoScInE()
DAMASK.write()

DAMASK.fields = Damask()
DAMASK.write("DAMASK_full.ttl")

