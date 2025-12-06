import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import copy
from src.physics import calculate_gravitational_force

class NBodySimulator:
    def __init__(self, bodies, integrator, dt):
        self.bodies = [copy.deepcopy(b) for b in bodies]
        self.integrator = integrator
        self.dt = dt

    def step(self):
        self.bodies = self.integrator(self.bodies, self.dt)

    def energy(self):
        KE = 0.0
        PE = 0.0
        G = 6.67430e-11
        for b in self.bodies:
            KE += 0.5 * b.mass * np.dot(b.vel, b.vel)
        for i in range(len(self.bodies)):
            for j in range(i+1, len(self.bodies)):
                r = np.linalg.norm(self.bodies[i].pos - self.bodies[j].pos)
                if r != 0:
                    PE -= G * self.bodies[i].mass * self.bodies[j].mass / r
        return KE + PE

    def run(self, steps):
        energies = []
        for _ in range(steps):
            energies.append(self.energy())
            self.step()
        energies.append(self.energy())
        return energies

    def animation(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.grid()

        max_initial_dist = 0
        if len(self.bodies) > 1:
            max_initial_dist = max(np.linalg.norm(b.pos) for b in self.bodies if b.name != "Sun")
        ax.set_xlim(-max_initial_dist * 1.5, max_initial_dist * 1.5)
        ax.set_ylim(-max_initial_dist * 1.5, max_initial_dist * 1.5)

        scatter_plots = [
            ax.plot([b.pos[0]], [b.pos[1]], 'o', markersize=10 if b.name == "Sun" else 5, color=b.color, label=b.name)[
                0] for b
            in self.bodies]
        path_plots = [ax.plot([b.pos[0]], [b.pos[1]], color=b.color, alpha=0.5)[0] for b in self.bodies]

        ax.legend()

        def animate(frame_num):
            #  Рассчёт сил на каждое тело
            forces = {b.name: np.array([0, 0], dtype=float) for b in self.bodies}
            for i in range(len(self.bodies)):
                for j in range(i + 1, len(self.bodies)):
                    b1 = self.bodies[i]
                    b2 = self.bodies[j]
                    force_on_b1 = calculate_gravitational_force(b1, b2)
                    forces[b1.name] += force_on_b1
                    forces[b2.name] -= force_on_b1

            # Обновление координат и скорости
            self.step()

            #  Обновление графика
            for idx, b in enumerate(self.bodies):
                scatter_plots[idx].set_data([b.pos[0]], [b.pos[1]])  # Новое положение точки
                path_data = np.array(b.path).T
                path_plots[idx].set_data(path_data[0], path_data[1])  # Рисуем траекторию

            ax.set_title(f"Day: {frame_num}")

            return scatter_plots + path_plots

        num_frames = 365 * 5  # Время анимации
        ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=0.01)
        plt.show()