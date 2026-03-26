"""
Estimate heat output (BTU/hr) from temperature change in a closed box.

Model:
dT/dt = P/C - k(T - T_room)

Where
P = heat input rate (BTU/hr)
C = total heat capacity of the box system (BTU / °F)
k = heat loss coefficient (1/hr)
T = internal box temperature (°F)
T_room = ambient room temperature (°F)

This script:
1) Generates synthetic temperature data
2) Estimates P from that data
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# PARAMETERS (EDIT THESE FOR YOUR REAL EXPERIMENT)
# ---------------------------------------------------------------------

T_room = 70.0
# Ambient room temperature (°F)

T_initial = 70.0
# Initial temperature inside the box (°F)

C_system = 0.35
# Total heat capacity of the system (BTU / °F)
# Includes air + box walls + objects

k_loss = 0.08
# Heat loss coefficient (1/hr)
# Larger values = more heat leaking out of the box

P_true = 6.0
# Heat pack output (BTU/hr)
# Used only to generate synthetic data

minutes = 240
# Total simulation time (minutes)

dt_minutes = 1
# Time step (minutes)

# ---------------------------------------------------------------------
# TIME VECTOR
# ---------------------------------------------------------------------

time = np.arange(0, minutes, dt_minutes)

# Convert timestep to hours because P is in BTU/hr
dt_hours = dt_minutes / 60.0

# ---------------------------------------------------------------------
# GENERATE SYNTHETIC TEMPERATURE DATA
# ---------------------------------------------------------------------

T = np.zeros(len(time))
T[0] = T_initial

for i in range(1, len(time)):

    dTdt = (P_true / C_system) - k_loss * (T[i-1] - T_room)

    T[i] = T[i-1] + dTdt * dt_hours

# Add small measurement noise
T = T + np.random.normal(0, 0.05, size=len(T))


# ---------------------------------------------------------------------
# ESTIMATE HEAT OUTPUT FROM TEMPERATURE DATA
# ---------------------------------------------------------------------

# Compute temperature derivative
dTdt_est = np.gradient(T, dt_hours)

# Rearranged model equation
# P = C*(dT/dt + k(T - T_room))

P_est = C_system * (dTdt_est + k_loss * (T - T_room))

# Average estimated heat output
P_mean = np.mean(P_est)

print("True Heat Output (synthetic):", round(P_true,2), "BTU/hr")
print("Estimated Heat Output:", round(P_mean,2), "BTU/hr")


# ---------------------------------------------------------------------
# PLOT RESULTS
# ---------------------------------------------------------------------

plt.figure()

plt.plot(time, T)

plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°F)")
plt.title("Synthetic Box Temperature")

plt.show()


plt.figure()

plt.plot(time, P_est)

plt.xlabel("Time (minutes)")
plt.ylabel("Estimated Heat Output (BTU/hr)")
plt.title("Estimated Heat Output Over Time")

plt.show()