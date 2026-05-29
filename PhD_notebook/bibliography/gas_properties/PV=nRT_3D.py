import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D plotting

# === LaTeX / paper-style settings ===

font_scale = 1

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

# --- Constants ---
R = 8.314  # J/(mol·K)

# --- Gases: molar mass in kg/mol ---
gases = {
    "Xe": 0.13129,
    "Kr": 0.0838,
    "Ar": 0.039948,
    "N2": 0.028013,
    "Ne": 0.020179,
    "He": 0.004003,
}

# --- Colors for each gas ---
colors = {
    "Xenon": "red",
    "Krypton": "purple",
    "Argon": "orange",
    "Nitrogen": "blue",
    "Neon": "green",
    "Helium": "brown",
}

# --- Pressure (bar) and temperature (°C) ranges ---
temps_C = np.linspace(0, 1000, 100)
pressures_bar = np.linspace(1, 50, 50)  # keep original start at 1 bar

# --- Create meshgrid ---
P_grid, T_grid = np.meshgrid(pressures_bar, temps_C)
T_K_grid = T_grid + 273.15  # convert °C → K

# --- 3D Figure setup ---
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111, projection='3d')

# --- Plot surfaces for each gas ---
for gas, M in gases.items():
    rho_grid = P_grid * 1e5 * M / (R * T_K_grid)  # Ideal gas law
    ax.plot_surface(
        T_grid, P_grid, rho_grid,
        color=colors[gas],
        alpha=0.9,           # keep original transparency
        edgecolor='none',    # no mesh lines
        antialiased=False    # remove small white lines
    )

# --- Labels and title with original labelpad ---
ax.set_xlabel('Temperature (°C)', labelpad=5)
ax.set_ylabel('Pressure (bar)', labelpad=5)
ax.set_zlabel('Density (kg/m³)', rotation=270, labelpad=5)  # vertical Z label
ax.zaxis.set_label_coords(1.05, 0.5, 0)  # adjust position to the right
ax.view_init(elev=20, azim=60)
plt.title('Density of Various Gases as Function of Temperature and Pressure', pad=1)

# --- Set axes limits to include the origin ---
ax.set_xlim(0, temps_C.max())
ax.set_ylim(0, pressures_bar.max())
ax.set_zlim(0, None)

# --- Optional: create a table of densities for export ---
df_rows = []
for gas, M in gases.items():
    for P in pressures_bar:
        densities = [P * 1e5 * M / (R * (T+273.15)) for T in temps_C]
        row = {'Gas': gas, 'Pressure (bar)': P}
        for T_val, rho_val in zip(temps_C, densities):
            row[f'{T_val} °C'] = rho_val
        df_rows.append(row)

df = pd.DataFrame(df_rows)
print(df)
df.to_csv('PV=nRT_3D.csv', index=False)

# --- Legend to the right with original settings ---
legend_elements = [Line2D([0], [0], color=color, lw=4, label=gas) 
                   for gas, color in colors.items()]
ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5),
          ncol=1, frameon=False)

# --- Adjust margins around the plot ---
plt.subplots_adjust(
    left=0.2,    # space on the left
    right=0.8,  # space on the right
    top=0.9,     # space above for title
    bottom=0.1   # space below
)

# --- Save figure ---
output_path = os.path.join(os.path.dirname(__file__), "PV=nRT_3D.svg")
plt.savefig(output_path, format='svg')

plt.show()