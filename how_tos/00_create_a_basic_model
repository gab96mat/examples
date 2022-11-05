import compas_fea2
from compas_fea2.model import Model, DeformablePart, Node
from compas_fea2.model import CircularSection, ElasticIsotropic, BeamElement

mdl = Model(name='my_model')
prt = DeformablePart(name='my_part')
n1 = Node(xyz=[0,0,0])
n2 = Node(xyz=[1,0,0])

mat = ElasticIsotropic(E=210_000_000_000, v=0.2, density=7800)
sec = CircularSection(r=0.01, material=mat)
beam = BeamElement(nodes=[n1,n2], section=sec)

prt.add_element(beam)
print(prt)

mdl.add_part(part=prt)

mdl.summary()
mdl.show()