from src.physics import calculate_gravitational_force
import numpy as np
import copy

def acc_array(positions, masses):
    N = len(positions)
    acc = [np.zeros(2) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j: continue
            r = positions[j] - positions[i]
            dist = np.linalg.norm(r)
            if dist == 0:
                continue
            acc[i] += (6.67430e-11 * masses[j]) * r / (dist**3)
    return acc

def rk4_step(bodies, dt):
    # convert bodies to arrays
    N = len(bodies)
    pos0 = [b.pos.copy() for b in bodies]
    vel0 = [b.vel.copy() for b in bodies]
    masses = [b.mass for b in bodies]

    # k1
    a1 = acc_array(pos0, masses)
    k1p = [v for v in vel0]
    k1v = [a for a in a1]

    # k2
    pos_k2 = [pos0[i] + 0.5*dt*k1p[i] for i in range(N)]
    vel_k2 = [vel0[i] + 0.5*dt*k1v[i] for i in range(N)]
    a2 = acc_array(pos_k2, masses)
    k2p = vel_k2
    k2v = a2

    # k3
    pos_k3 = [pos0[i] + 0.5*dt*k2p[i] for i in range(N)]
    vel_k3 = [vel0[i] + 0.5*dt*k2v[i] for i in range(N)]
    a3 = acc_array(pos_k3, masses)
    k3p = vel_k3
    k3v = a3

    # k4
    pos_k4 = [pos0[i] + dt*k3p[i] for i in range(N)]
    vel_k4 = [vel0[i] + dt*k3v[i] for i in range(N)]
    a4 = acc_array(pos_k4, masses)
    k4p = vel_k4
    k4v = a4

    # update
    for i,b in enumerate(bodies):
        b.pos = pos0[i] + (dt/6.0)*(k1p[i] + 2*k2p[i] + 2*k3p[i] + k4p[i])
        b.vel = vel0[i] + (dt/6.0)*(k1v[i] + 2*k2v[i] + 2*k3v[i] + k4v[i])
        b.path.append(b.pos.copy())

    return bodies