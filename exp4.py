#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:30:31 2023

@author: uday
"""

import meep as mp


cell = mp.Vector3(16, 8, 0)

geometry = [
    mp.Block(
        mp.Vector3(mp.inf, 1, mp.inf),
        center=mp.Vector3(),
        material=mp.Medium(epsilon=30),
    )
]
sources = [
    mp.Source(
        mp.ContinuousSource(frequency=0.15), component=mp.Ez, center=mp.Vector3(-7, 0)
    )
]


pml_layers = [mp.PML(1.0)]



resolution = 10

sim = mp.Simulation(
    cell_size=cell,
    boundary_layers=pml_layers,
    geometry=geometry,
    sources=sources,
    resolution=resolution,
)
from matplotlib import pyplot as plt


plt.figure(dpi=100)
sim.plot2D()
plt.show()


sim.run(until=200)



plt.figure(dpi=100)
sim.plot2D(fields=mp.Ez)
plt.show()

