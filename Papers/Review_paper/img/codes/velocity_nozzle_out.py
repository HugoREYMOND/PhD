import numpy as np
import matplotlib.pyplot as plt
import os  # needed for saving

# === LaTeX / paper-style settings ===

font_scale = 1.2

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern"],

    # Base font
    "font.size": 12 * font_scale,

    # Titles and labels
    "axes.titlesize": 14 * font_scale,
    "axes.labelsize": 12 * font_scale,

    # Tick labels
    "xtick.labelsize": 11 * font_scale,
    "ytick.labelsize": 11 * font_scale,

    # Legend
    "legend.fontsize": 11 * font_scale,

    # Clean look
    "axes.grid": False
})

# Gas properties
gases = ['Helium', 'Neon', 'Argon', 'Krypton', 'Xenon', 'Nitrogen']
R_values = np.array([2.08E+03, 4.12E+02, 2.08E+02, 9.92E+01, 6.33E+01, 2.97E+02])  # J/(kg·K)				

gamma_values = np.array([1.67, 1.67, 1.69, 1.73, 1.83, 1.4])

# Colors for each gas
colors = {
    "Xenon": "red",
    "Krypton": "purple",
    "Argon": "orange",
    "Nitrogen": "blue",
    "Neon": "green",
    "Helium": "brown",
}

# Pressure range (P0) in bar
P0_bar = np.linspace(1, 70, 200)
P = 1  # bar, constant downstream pressure
T0 = 300  # K, stagnation temperature

# 3D plot
fig = plt.figure(figsize=(6.5, 4))
ax = fig.add_subplot(111, projection='3d')

# Plot each gas as an independent curve
for i, gas in enumerate(gases):
    gamma = gamma_values[i]
    R = R_values[i]
    v = np.sqrt((2 * gamma * R * T0 / (gamma - 1)) * (1 - (P / P0_bar)**((gamma - 1) / gamma)))
    ax.plot([i]*len(P0_bar), P0_bar, v, color=colors[gas], linewidth=2)

# Labels
ax.set_ylabel('Nozzle Pressure $P_0$ [bar]', labelpad=3)
ax.set_zlabel('Velocity $v$ [m/s]', labelpad=3)
ax.set_title('Velocity as a function of gas and nozzle pressure')

ax.set_ylim(0, max(P0_bar))
ax.set_zlim(0, 2000)

# Set X-ticks at the gas positions and rotate labels 90° (parallel to pressure axis)
ax.set_xticks(np.arange(len(gases)))
ax.set_xticklabels(gases, rotation=90, ha='center', va='top')

ax.tick_params(axis='both', which='major', pad=0)

# Adjust the view angle
ax.view_init(elev=20, azim=-45)

# Adjust margins
plt.subplots_adjust(left=0.2, right=0.85, top=0.9, bottom=0.1)

# Save figure
output_path = os.path.join(os.path.dirname(__file__), "velocity_nozzle_out.pdf")
plt.savefig(output_path, format='pdf')

plt.show()