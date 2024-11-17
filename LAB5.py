import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Function, Eq, dsolve
import sympy as sp
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

# Parameters for numerical solution
RC = 0.1
dt = 0.01  # Time step for Euler's method
# Define time intervals and initial conditions
t_start, t_mid, t_end = 0, 0.5, 1  # Time intervals
time_intervals = [np.arange(t_start, t_mid, dt), np.arange(t_mid, t_end + dt, dt)]

U_in_numeric = [1, 0]  # Input voltages for each interval
U_out_initial = [0, 1] # Initial output voltages for each interval

# Symbolic variables
'''
Symbolic solution derivative to solve
RC*(dU_out(t)/dt) + U_out(t) = U_in(t)
'''
def differential(U_out, t, U_in):
    return RC * sp.Derivative(U_out, t) + U_out - U_in

t = sp.symbols('t')
U_out = sp.Function('U_out')(t) # U_out as a function of time
U_in = sp.Piecewise((1, t < 0.5), (0, t >= 0.5))  # U_in as a piecewise function
sym_solution = sp.dsolve(differential(U_out, t, U_in), U_out)
print(sym_solution)
'''
# Interval 1: t ∈ [0, 0.5], U_in = 1
eq1 = Eq(RC * Uout.diff(t) + Uout, 1)
sol1 = dsolve(eq1, Uout).rhs.subs({Uout.subs(t, 0): 0})  # Apply initial condition U_out(0) = 0

# Interval 2: t ∈ [0.5, 1], U_in = 0
eq2 = Eq(RC * Uout.diff(t) + Uout, 0)
sol2 = dsolve(eq2, Uout).rhs.subs({Uout.subs(t, t_mid): 1})  # Apply initial condition U_out(0.5) = 1

# Generate analytical solutions
analytical_interval_1 = [float(sol1.subs(t, val)) for val in time_intervals[0]]
analytical_interval_2 = [float(sol2.subs(t, val)) for val in time_intervals[1]]

analytical_combined = np.concatenate([analytical_interval_1, analytical_interval_2])

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t_combined, numerical_combined, '-', label='Numerical Solution (Euler)', markersize=4)
#plt.plot(t_combined, analytical_combined, '-', label='Analytical Solution', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Output Voltage $U_{out}(t)$')
plt.title('Comparison of Numerical and Analytical Solutions')
plt.legend()
plt.grid()
plt.show()
'''











'''
import numpy as np
import matplotlib.pyplot as plt

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
'''

