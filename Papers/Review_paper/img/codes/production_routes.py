import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.colors import LinearSegmentedColormap

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

# === Data ===
processes = [
    "VIGA",
    "EIGA / PIGA",
    "PREP",
    "Water atomization",
    "Centrifugal atomization",
    "Ultrasonic atomization",
    "Mechanical attrition",
    "PVD / CVD"
]

criteria = ["PSD", "LPBF", "Sphericity", "Cost", "Speed"]

data = np.array([
    [3,3,2,2,3], # VIGA
    [3,3,3,1,1], # EIGA / PIGA
    [3,3,3,1,1], # PREP
    [1,0,0,3,3], # Water atomization
    [2,2,2,2,2], # Centrifugal atomization
    [3,3,3,2,0], # Ultrasonic atomization
    [0,0,0,2,0], # Mechanical attrition
    [3,0,3,0,0], # PVD / CVD
])

# === Colormap (pastel) ===
colors = ["#ffffff", "#5d82ff"]
custom_cmap = LinearSegmentedColormap.from_list("custom_pastel", colors)

# === Figure (CENTERED LAYOUT CONTROL) ===
fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)

# === Heatmap ===
im = ax.imshow(data, cmap=custom_cmap, vmin=0, vmax=3)

# Axis labels
ax.set_xticks(np.arange(len(criteria)))
ax.set_yticks(np.arange(len(processes)))
ax.set_xticklabels(criteria, rotation=30, ha="right")
ax.set_yticklabels(processes)

# === Cell annotations ===
for i in range(len(processes)):
    for j in range(len(criteria)):
        ax.text(j, i, data[i, j],
                ha="center", va="center", color="black")

# === Title ===
ax.set_title("Comparative Assessment of Powder Production Routes")

# === CENTERED COLORBAR (attached to axes, not figure coords) ===
cbar = fig.colorbar(im, ax=ax, orientation="horizontal", pad=0.03, fraction=0.05)
cbar.set_label("Performance level (0 = unfavorable → 3 = favorable)")
cbar.set_ticks([0, 1, 2, 3])
cbar.outline.set_visible(False)

# === Save ===
output_path = os.path.join(os.path.dirname(__file__), "production_routes.svg")
plt.savefig(output_path, format='svg')

plt.show()