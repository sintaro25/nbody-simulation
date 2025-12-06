import os, sys
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, repo_root)

import matplotlib.pyplot as plt
from src.nbody_solver import NBodySimulator
from data.solar_system_data import bodies
from src.rk4_integrator import rk4_step
from src.leapfrog_integrator import leapfrog_step

dt = 3600*24

sim_rk = NBodySimulator(bodies, rk4_step, dt)
E_rk = sim_rk.run(1000)

sim_lf = NBodySimulator(bodies, leapfrog_step, dt)
E_lf = sim_lf.run(1000)

plt.plot(E_rk, label='RK4')
plt.plot(E_lf, label='Leapfrog')
plt.legend()
plt.title('Energy comparison — Full system')
out = os.path.join(repo_root, 'results', 'example_full_system.png')
plt.savefig(out)
print('Saved', out)


# simulation = NBodySimulator(bodies, rk4_step, DT)
# simulation.animation()