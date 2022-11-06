import os
from pathlib import Path

import compas_fea2
from compas_fea2.model import Model

from compas_fea2.units import units
units = units(system='SI_mm')

compas_fea2.set_backend('abaqus')

HERE = os.path.dirname(__file__)
TEMP = os.sep.join(HERE.split(os.sep)[:-1]+['temp'])

# Note: you need to run the previous example first to get the model data.
mdl = Model.from_cfm(Path(TEMP).joinpath('01_mesh_refine', 'model.cfm'))
prb = mdl.find_problem_by_name('01_mesh_refine')

# prb.show_deformed(scale_factor=1000)
prb.show_displacements(draw_loads=100)