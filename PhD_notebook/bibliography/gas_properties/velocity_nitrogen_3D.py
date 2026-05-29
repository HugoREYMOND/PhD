import numpy as np
import matplotlib.pyplot as plt
import os

# === LaTeX / paper-style settings ===
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.figsize": (6.5, 4),
    "axes.grid": True,
    "grid.color": "gray",
    "grid.alpha": 0.3,
    "grid.linestyle": "-",
    "grid.linewidth": 0.5,
    "lines.linewidth": 1.2
})

# Properties of Nitrogen
gamma = 1.4  # heat capacity ratio
R = 2.97E+02    # specific gas constant [J/(kg·K)]

# Pressure and temperature ranges
P0_bar = np.linspace(1, 70, 200)     # nozzle (stagnation) pressure from 1 to 70 bar
T0_K = np.linspace(300, 1200, 200)   # stagnation temperature from 300 to 1200 K

# Create a 2D grid of P0 x T0
P_grid, T_grid = np.meshgrid(P0_bar, T0_K)

# Downstream (ambient) pressure constant at 1 bar
P = 1  # bar

# Calculate isentropic exit velocity
v = np.sqrt((2 * gamma * R * T_grid / (gamma - 1)) * (1 - (P / P_grid)**((gamma - 1) / gamma)))

# 3D plot
fig = plt.figure(figsize=(6.5, 4))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(P_grid, T_grid, v, cmap='plasma', edgecolor='none', alpha=0.9)

# Axis labels
ax.set_xlabel('Nozzle Pressure $P_0$ [bar]')
ax.set_ylabel('Stagnation Temperature $T_0$ [K]')
ax.set_zlabel('Velocity $v$ [m/s]')
ax.set_title('Velocity of Nitrogen as a function of Pressure and Temperature')

ax.set_xlim(0, max(P0_bar))
ax.set_ylim(300, max(T0_K))
ax.set_zlim(0, 1400)

ax.set_yticks(np.arange(300, 1200, 150))

# Add color bar
fig.colorbar(surf, shrink=0.6, label='Velocity [m/s]')

# Set viewing angle
ax.view_init(elev=20, azim=-130)

# Adjust margins
plt.subplots_adjust(left=0.15, right=0.85, top=0.9, bottom=0.1)

# Save figure as SVG
output_path = os.path.join(os.path.dirname(__file__), "velocity_nitrogen_3d.svg")
plt.savefig(output_path, format='svg')

plt.show()