from particle import Particle
import numpy as np
import matplotlib.pyplot as plt

p1 = Particle()

p1.set_initial_conditions(0, 0, 15, 45)
p1.range()
p1.plot_trajectory()