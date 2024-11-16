import numpy as np
import matplotlib.pyplot as plt
'''
dv2(t)/R = dv2(t)/dt C
v2 = 0
v2(h) = (v1-v2(0))/RC*h + v2(0)
v(2h) = (v1-v2(h))/RC*h + v2(h)

Init Conditions=>
v2(0) = 0 ; t = [0, 0.5] ; v1 = 1
v2(0.5) = 1 ; t = [0.5, 1] ; v1=0
RC= 0.1
'''
import numpy as np
import matplotlib.pyplot as plt

# Parameters
RC = 0.1
h = 0.001  # Smaller step size for Euler's method
t = np.arange(0, 1, h)
v1_values = [(0, 0.5, 1), (0.5, 1, 0)]  # Intervals and corresponding v1 values
v2_initial = 0  # Initial condition

# Numerical solution using Euler's method
v2_num = [v2_initial]
for time_start, time_end, v1 in v1_values:
    t_range = np.arange(time_start, time_end, h)
    for i in range(len(t_range) - 1):
        dv2_dt = (v1 - v2_num[-1]) / RC
        v2_next = v2_num[-1] + h * dv2_dt
        v2_num.append(v2_next)

# Analytical solution
v2_analytic = []
for time in t:
    if time < 0.5:
        v2_a = 1 * (1 - np.exp(-time / RC))
    else:
        v2_a = 1 * np.exp(- (time - 0.5) / RC)
    v2_analytic.append(v2_a)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t, v2_num, label="Numerical Solution (Euler's Method)", linestyle='--')
plt.plot(t, v2_analytic, label="Analytical Solution", color='red')
plt.xlabel("Time (s)")
plt.ylabel("Voltage $v_2(t)$")
plt.title("Comparison of Numerical and Analytical Solutions")
plt.legend()
plt.grid()
plt.show()
