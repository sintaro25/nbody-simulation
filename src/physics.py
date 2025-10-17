import numpy as np

G = 6.67430e-11


class Body:
    def __init__(self, mass, x, y, vx, vy, name, color):
        self.mass = float(mass)
        self.pos = np.array([float(x), float(y)], dtype=float)
        self.vel = np.array([float(vx), float(vy)], dtype=float)
        self.name = name
        self.color = color
        self.acc = np.array([0, 0], dtype=float)

    def update_acc(self, force):
        self.acc = force / self.mass

    def update_velocity(self, dt):
        self.vel += self.acc * dt

    def update_position(self, dt):
        self.pos += self.vel * dt


def calculate_gravitational_force(p1, p2):
    r_vec = p2.pos - p1.pos  # Вектор между частицами
    r_mag = np.linalg.norm(r_vec)  # Расстояние между частицами
    r_hat = r_vec / r_mag  # Единичный вектор, направленный от p1 к p2

    force_mag = (G * p1.mass * p2.mass) / (r_mag ** 2)  # Величина силы
    force_vec = force_mag * r_hat  # Вектор силы, действующей на p1 со стороны p2
    return force_vec
