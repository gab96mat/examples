from compas_fea2.model import Model
from compas_fea2.model import DeformablePart
from compas_fea2.model import Node

from compas.geometry import Point

mdl = Model()

prt1 = DeformablePart(name="Part1")

mdl.add_parts([prt1])

node1 = Node(xyz=[0.0, 0.0, 0.0], name="Node1")
node2 = Node(xyz=[0.0, 0.0, 10.0], name="Node2")
node2 = Node(xyz=[0.0, 0.0, 100.0], name="Node3")

#Adding only the first 2 nodes
prt1.add_nodes([node1, node2])

names = ["Node1", "Node2", "Node3"]

a = [prt1.find_nodes_by_name(name = n) for n in names] 
print(a)