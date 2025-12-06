from src.physics import calculate_gravitational_force
import numpy as np
import copy

def leapfrog_step(bodies, dt):
    N = len(bodies)
    forces = [np.zeros(2) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j: continue
            forces[i] += calculate_gravitational_force(bodies[i], bodies[j])

    for i,b in enumerate(bodies):
        b.update_acc(forces[i])
        b.vel += 0.5 * dt * b.acc

    for b in bodies:
        b.pos += dt * b.vel
        b.path.append(b.pos.copy())

    forces = [np.zeros(2) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j: continue
            forces[i] += calculate_gravitational_force(bodies[i], bodies[j])

    for i,b in enumerate(bodies):
        b.update_acc(forces[i])
        b.vel += 0.5 * dt * b.acc
    return bodies