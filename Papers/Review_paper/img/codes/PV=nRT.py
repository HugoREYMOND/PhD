import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.lines import Line2D

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

# Constantes
R = 8.314  # J/(mol·K)

# Gaz : molar mass en kg/mol
gases = {
    "He": 0.004003,
    "Ne": 0.020179,
    "Ar": 0.039948,
    "Kr": 0.0838,
    "Xe": 0.13129,
    "N2": 0.028013
}

# Couleurs pour chaque gaz
colors = {
    "He": "brown",
    "Ne": "green",
    "Ar": "orange",
    "Kr": "purple",
    "Xe": "red",
    "N2": "blue"
}

# Styles de lignes pour chaque pression
line_styles = {
    1: '-',
    5: '--',
    10: '-.',
    20: ':'
}

# Plages de température (°C → K)
T_C = np.linspace(0, 1500, 200)
T = T_C + 273.15

# Pressions
pressures_bar = [1, 5, 10, 20]
pressures_Pa = [p * 1e5 for p in pressures_bar]

# === Plot ===
plt.figure()

for gas, M in gases.items():
    color = colors[gas]
    for P_bar, P in zip(pressures_bar, pressures_Pa):
        rho = P * M / (R * T)
        plt.plot(T_C, rho,
                 color=color,
                 linestyle=line_styles[P_bar])

# === Axes ===
plt.xlim(0, 1500)
plt.ylim(0, 125)

plt.xlabel("Temperature (°C)")
plt.ylabel("Density (kg/m³)")
plt.title("Density of Gases as a Function of Temperature for Different Pressures")

# === Legends ===

# Legend for gases (colors)
gas_legend = [
    Line2D([0], [0], color=colors[g], lw=2, label=g)
    for g in gases
]

# Legend for pressures (line styles)
pressure_legend = [
    Line2D([0], [0], color='black', linestyle=line_styles[p], lw=2, label=f"{p} bar")
    for p in pressures_bar
]

legend1 = plt.legend(handles=gas_legend,
                     title="Gas",
                     loc="upper right",
                    frameon=True,     # Draw a box around the legend
                    facecolor='white',    # Background color of the legend
                    edgecolor='none',    # Border color of the legend
                    framealpha=0.8,)      # Transparency of the legend box)
plt.gca().add_artist(legend1)

plt.legend(handles=pressure_legend,
            title="Pressure",
            loc="upper center",
            frameon=True,     # Draw a box around the legend
            facecolor='white',    # Background color of the legend
            edgecolor='none',    # Border color of the legend
            framealpha=0.8,)      # Transparency of the legend box

# === Layout ===
plt.tight_layout()
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.15, top=0.88)

# === Save ===
output_path = os.path.join(os.path.dirname(__file__), "PV=nRT.svg")
plt.savefig(output_path, format='svg')

plt.show()