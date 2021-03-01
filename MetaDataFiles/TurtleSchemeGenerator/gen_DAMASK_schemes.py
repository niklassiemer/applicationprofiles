from data_scheme import MetaDataSchemes as Scheme
from data_scheme import MetaDataField as Field

micro = "\u03bc"
deg = "\u00b0"

blue = [
    Field(label="Operator"),
    Field(label='Affiliation'),
    Field(label="Simulation ID/name", name='simulationID'),
    Field(label="Constitutive models"),
    Field(label="Library module"),
    Field(label="Software version"),
    Field(label="Comment", long=True)
]

green = [
    # Material input
    Field(label="Plasticity model"),
    Field(label="Lattice structure"),
    Field(label="Elastic moduli", unit='Pa'),
    Field(label="Slip families"),
    Field(label="Initial dislocation density", unit='1/m**2'),
    Field(label="Peierls stress", unit='Pa'),
    # Geometry input
    Field(label="Physical size of the geometry", unit='m'),
    Field(label="Grids of the geometry"),
    # Boundary conditions
    Field(label="Deformation gradient rate"),
    Field(label="Applied stress", unit='Pa'),
    Field(label="Simulation time", unit='s'),
    Field(label="Numerical increments"),
    # Numerical input
    Field(label="Mechanical solver"),
    Field(label="Phase field solver"),
    Field(label="Maximum iterations"),
    Field(label="Maximum cutbacks")
]

grey = [
    Field(label="Cluster name"),
    Field(label='CPU info'),
    Field(label='cores'),
    Field(label='Required RAM', unit='GB'),
    Field(label="Runtime", unit='h'),
    Field(label="Submission time"),
    Field(label="Stop time")
]



DAMASK = Scheme("DAMASK")
DAMASK.fields = blue
DAMASK.write()

DAMASK.fields = green
DAMASK.write("DAMASK_green.ttl")

DAMASK.fields = grey
DAMASK.write("DAMASK_grey.ttl")

DAMASK.fields = blue + green + grey
DAMASK.write("DAMASK_full.ttl")

