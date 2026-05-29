import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# === LaTeX / paper-style settings ===
plt.rcParams.update({
    "text.usetex": True,          # Use LaTeX for all text rendering
    "font.family": "serif",       # Use a serif font for the plot
    "font.serif": ["Computer Modern"],  # Specify "Computer Modern" as the serif font (default LaTeX font)
    "font.size": 11,              # Base font size for all text in the figure
    "axes.titlesize": 12,         # Font size for the axis titles
    "axes.labelsize": 11,         # Font size for the x and y axis labels
    "xtick.labelsize": 10,         # Font size for x-axis tick labels
    "ytick.labelsize": 10,         # Font size for y-axis tick labels
    "legend.fontsize": 10,         # Font size for the legend text
    "figure.figsize": (6.5, 4),   # Figure size in inches (width x height) – suitable for paper/column
    "axes.grid": True,            # Turn on grid for both x and y axes
    "grid.color": "gray",         # Grid line color
    "grid.alpha": 0.3,            # Grid line transparency (0 = invisible, 1 = opaque)
    "grid.linestyle": "-",        # Style of the grid lines (solid line)
    "grid.linewidth": 0.5,        # Thickness of the grid lines
    "lines.linewidth": 1.2        # Default width for plotted lines
})

# === Read the file ===
file_path = r"m:\PhD_notebook\experiments\atomization_1\data\temp_sensor_test\it1.txt"
df = pd.read_csv(file_path, sep="\t", skiprows=3)

# === Extract data ===
temp = df.iloc[:, 1].astype(str).str.replace(",", ".").astype(float)

# === Create time axis ===
sampling_interval = 0.01  # 10 ms
num_points = len(temp)
time = np.arange(0, num_points * sampling_interval, sampling_interval)
time = time[:num_points]  # ensure alignment with temp

# === Create figure and axis ===
fig, ax = plt.subplots()

ax.plot(time, temp, color='darkblue', linewidth=0.8, label='Temperature')

# === Titles and labels ===
ax.set_title("Furnace Temperature", pad=10)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Temperature (°C)")

# === Limits and ticks ===
xmin, xmax = 14, 27
ax.set_xlim(xmin, xmax)
ax.set_ylim(900, temp.max() + 10)

ax.set_xticks(np.arange(xmin, xmax + 1, 1))
ax.set_yticks(np.arange(900, int(temp.max()) + 20, 30))
ax.tick_params(axis='x', rotation=45)

# === Grid and style ===
ax.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.3)

# === Clean legend ===
ax.legend(loc='lower right', # Location of the legend
          frameon=True,     # Draw a box around the legend
          facecolor='white',    # Background color of the legend
          edgecolor='none',    # Border color of the legend
          framealpha=0.8,)      # Transparency of the legend box

# === Layout adjustment for publication ===
plt.tight_layout(pad=1)

# === Save as SVG ===
output_path = os.path.join(os.path.dirname(__file__), "temperature_plot.svg")
plt.savefig(output_path, format='svg')

plt.show()
print(f"Graph saved at: {output_path}")