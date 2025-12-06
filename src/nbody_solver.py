import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from data.solar_system_data import bodies
from src.physics import calculate_gravitational_force, DT

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid()

max_initial_dist = 0
if len(bodies) > 1:
    max_initial_dist = max(np.linalg.norm(b.pos) for b in bodies if b.name != "Sun")
ax.set_xlim(-max_initial_dist * 1.5, max_initial_dist * 1.5)
ax.set_ylim(-max_initial_dist * 1.5, max_initial_dist * 1.5)

scatter_plots = [ax.plot([b.pos[0]], [b.pos[1]], 'o', markersize=10 if b.name == "Sun" else 5, color=b.color, label=b.name)[0] for b
                 in bodies]
path_plots = [ax.plot([b.pos[0]], [b.pos[1]], color=b.color, alpha=0.5)[0] for b in bodies]

ax.legend()

def animate(frame_num):
    #  Рассчёт сил на каждое тело
    forces = {b.name: np.array([0, 0], dtype=float) for b in bodies}
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            b1 = bodies[i]
            b2 = bodies[j]
            force_on_b1 = calculate_gravitational_force(b1, b2)
            forces[b1.name] += force_on_b1
            forces[b2.name] -= force_on_b1

    #  Обновление координат и скорости
    for b in bodies:
        b.update_acc(forces[b.name])
        b.update_velocity(DT)
        b.update_position(DT)

    #  Обновление графика
    for idx, b in enumerate(bodies):
        scatter_plots[idx].set_data([b.pos[0]], [b.pos[1]])  # Новое положение точки
        path_data = np.array(b.path).T
        path_plots[idx].set_data(path_data[0], path_data[1])  # Рисуем траекторию

    ax.set_title(f"Day: {frame_num}")

    return scatter_plots + path_plots


num_frames = 365 * 5
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=0.01)
plt.show()