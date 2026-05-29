import os
import numpy as np
import matplotlib.pyplot as plt

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

# --- Universal gas constant ---
R = 8.314  # J/(mol·K)

# --- Gases: molar mass in kg/mol ---
gases = {
    "He": 0.004003,
    "Ne": 0.020179,
    "Ar": 0.039948,
    "Kr": 0.0838,
    "Xe": 0.13129,
    "N2": 0.028013,
    "O2": 0.031999
}

# --- Gamma values ---
gammas = {
    "He": 1.67,
    "Ne": 1.67,
    "Ar": 1.67,
    "Kr": 1.67,
    "Xe": 1.67,
    "N2": 1.40,
    "O2": 1.40
}

# =========================
# AIR MIXTURE MODEL
# =========================

# Volume % ≈ mole fraction
air_mix = {
    "N2": 0.7808,
    "O2": 0.2095,
    "Ar": 0.0093
}

# --- molar heat capacities ---
cp_molar = {}
cv_molar = {}

for gas in air_mix:
    gamma = gammas[gas]
    cp_molar[gas] = (gamma / (gamma - 1)) * R
    cv_molar[gas] = cp_molar[gas] - R

# --- mixture molar mass ---
M_air = sum(air_mix[g] * gases[g] for g in air_mix)

# --- mixture heat capacities ---
cp_air = sum(air_mix[g] * cp_molar[g] for g in air_mix)
cv_air = sum(air_mix[g] * cv_molar[g] for g in air_mix)

gamma_air = cp_air / cv_air

# --- specific gas constant ---
R_air = R / M_air

# --- Add Air as computed gas ---
gases["Air"] = M_air
gammas["Air"] = gamma_air

# --- Specific gas constants (J/(kg·K)) ---
R_specific = {gas: R / M for gas, M in gases.items()}
R_specific["Air"] = R_air

# --- Colors for each gas ---
colors = {
    "Xe": "red",
    "Kr": "purple",
    "Ar": "orange",
    "N2": "blue",
    "Ne": "green",
    "He": "brown",
    "Air": "black"
}

# --- Temperature range ---
T = np.linspace(293, 1200, 500)  # K

# --- Speed of sound ---
c = {gas: np.sqrt(gammas[gas] * R_specific[gas] * T) for gas in gases}

# --- Plot ---
fig, ax = plt.subplots()

for gas in gases:
    ax.plot(T, c[gas], label=gas, color=colors.get(gas, None), linewidth=1.0)

ax.set_xlabel("Temperature $T$ (K)", labelpad=10)
ax.set_ylabel("Speed of sound $c$ (m/s)", labelpad=10)
ax.set_title("Speed of sound in gases as a function of temperature", pad=15)

ax.set_xlim(300, 1200)
ax.set_ylim(0, max([max(cg) for cg in c.values()]) * 1.05)

ax.set_xticks(np.arange(300, 1251, 100))
ax.set_yticks(np.arange(0, 2500, 150))

ax.legend(title="Gas")

plt.tight_layout()

# --- Save figure ---
output_path = os.path.join(os.path.dirname(__file__), "speed_of_sound.pdf")
plt.savefig(output_path, format='pdf')

plt.show()

# --- Table of values ---
T_table = np.arange(293, 1301, 100)

print("\nSpeed of sound c (m/s):\n")

# Header
header = "T (K)".ljust(8)
for gas in gases:
    header += f"{gas}".rjust(10)

print(header)
print("-" * len(header))

# Rows
for T_val in T_table:
    row = f"{T_val:<8}"
    for gas in gases:
        c_val = np.sqrt(gammas[gas] * R_specific[gas] * T_val)
        row += f"{c_val:10.1f}"
    print(row)