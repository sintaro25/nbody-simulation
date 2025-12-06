import numpy as np

G = 6.67430e-11
DT = 3600 * 24


class Body:
    def __init__(self, mass, x, y, vx, vy, name, color):
        self.mass = float(mass)
        self.pos = np.array([float(x), float(y)])
        self.vel = np.array([float(vx), float(vy)])
        self.name = name
        self.color = color
        self.acc = np.array([0, 0])
        self.path = [self.pos.copy()]

    def update_acc(self, force):
        self.acc = force / self.mass

    def update_velocity(self, dt):
        self.vel += self.acc * dt

    def update_position(self, dt):
        self.pos += self.vel * dt
        self.path.append(self.pos.copy())


def calculate_gravitational_force(b1, b2):
    r_vec = b2.pos - b1.pos  # Вектор между телами
    r_mag = np.linalg.norm(r_vec)  # Расстояние между телами

    if r_mag == 0:
        return np.zeros(2)

    r_hat = r_vec / r_mag  # Единичный вектор, направленный от b1 к b2

    force_mag = (G * b1.mass * b2.mass) / (r_mag ** 2)  # Величина силы
    force_vec = force_mag * r_hat  # Вектор силы, действующей на b1 со стороны b2
    return force_vec

