import os
os.makedirs("results", exist_ok=True)

from component.compressor import compressor
from component.combustor import combustor
from component.turbine import turbine
from component.nozzle import nozzle

import matplotlib.pyplot as plt

# -----------------------
# INPUTS
# -----------------------
T1 = 288              # Inlet temperature (K)
P1 = 101325           # Inlet pressure (Pa)
pressure_ratio = 10
efficiency = 0.85     # Compressor efficiency
turb_eff = 0.9        # Turbine efficiency
T3 = 1400             # Turbine inlet temperature (K)

m_dot = 50            # Mass flow rate (kg/s)
V_inlet = 0
T_ambient = 288       # Ambient temp (K)

# -----------------------
# SINGLE RUN (BASE CASE)
# -----------------------

# Compressor
T2, P2, comp_work = compressor(T1, P1, pressure_ratio, efficiency)

# Combustor
T3, q_in = combustor(T2, T3)

# Turbine
T4, turb_work = turbine(T3, comp_work, turb_eff)

# Nozzle
V_exit = nozzle(T4, T_ambient)

# Thrust
thrust = m_dot * (V_exit - V_inlet)

# Efficiency
thermal_eff = (turb_work - comp_work) / q_in

# -----------------------
# PRINT RESULTS
# -----------------------

print("Compressor Results:")
print(f"T2: {T2:.2f} K")
print(f"P2: {P2:.2f} Pa")
print(f"Work: {comp_work:.2f} J/kg")

print("\nCombustor Results:")
print(f"T3: {T3:.2f} K")
print(f"Heat Added: {q_in:.2f} J/kg")

print("\nTurbine Results:")
print(f"T4: {T4:.2f} K")
print(f"Turbine Work: {turb_work:.2f} J/kg")

print("\nNozzle Results:")
print(f"Exit Velocity: {V_exit:.2f} m/s")

print("\nThrust:")
print(f"Thrust: {thrust:.2f} N")

print("\nEfficiency:")
print(f"Thermal Efficiency: {thermal_eff:.4f}")

# -----------------------
# PARAMETRIC ANALYSIS
# -----------------------

ratios = range(2, 25)

thrust_values = []
eff_values = []

for r in ratios:
    T2, P2, comp_work = compressor(T1, P1, r, efficiency)
    T3, q_in = combustor(T2, 1400)
    T4, turb_work = turbine(T3, comp_work, turb_eff)
    V_exit = nozzle(T4, T_ambient)

    thrust = m_dot * (V_exit - V_inlet)
    thrust_values.append(thrust)

    eff = (turb_work - comp_work) / q_in
    eff_values.append(eff)

# -----------------------
# PLOTTING
# -----------------------

# Thrust vs Pressure Ratio
plt.figure()
plt.plot(ratios, thrust_values)
plt.xlabel("Pressure Ratio")
plt.ylabel("Thrust (N)")
plt.title("Thrust vs Pressure Ratio")
plt.grid()
plt.savefig("results/thrust_vs_pr.png")

plt.figure()
plt.plot(ratios, eff_values)
plt.xlabel("Pressure Ratio")
plt.ylabel("Thermal Efficiency")
plt.title("Efficiency vs Pressure Ratio")
plt.grid()
plt.savefig("results/efficiency_vs_pr.png")

plt.show()