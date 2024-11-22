import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

'''
ODE => RC*(dUout(t)/dt) + Uout(t) = Uin(t)
'''

'''
Numerical Solution
'''
#ODE: dUout/dt = (Uin - Uout) / RC
def ODE(Uout, Uin, RC):
    return (Uin - Uout) / RC

def euler_method(f, U0, t_interval, Uin, RC, h):
    Uout_values = np.empty(len(t_interval))  # Array to store Uout values
    Uout_values[0] = U0  # Initial condition

    # Perform Euler's method
    for i in range(1, len(t_interval)):
        Uout_values[i] = Uout_values[i - 1] + h * f(Uout_values[i - 1], Uin[i - 1], RC)

    return Uout_values

# Parameters
U0 = 0              # Initial output
RC = 0.1            # Tau
t_start = 0
t_end = 1
h = 0.01            # Step

# Time interval
t_interval = np.arange(t_start, t_end + h, h)
Uin = np.where(t_interval <= 0.5, 1, 0)   # Input, Piecewise Function for when  [0, 0.5] => 1, [0.5, 1] => 0
Uout_values = euler_method(ODE, U0, t_interval, Uin, RC, h)


'''
Analytical Solution 
'''

# Define symbols
t_sym = sp.Symbol('t')         # Time variable
Uout = sp.Function('Uout') # Output voltage as a function of time
RC_sym = sp.Symbol('RC')       # Time constant
t_first =  np.arange(0, 0.5, h) # First Half
t_second = np.arange(0.5, 1 + h, h) # Second Half
ODE = sp.Eq(RC_sym * Uout(t_sym).diff(t_sym) + Uout(t_sym), Uin)
Uin = sp.Piecewise((1, t_sym <= 0.5), (0, t_sym > 0.5))
for t in t_first:
    solution_1 = sp.dsolve(ODE, Uout(t_sym), ics={Uout(0): U0}).subs({RC_sym: RC, t_sym: t, Uout(0.5): 1})
# Define the ODE
'''
solution_1 = sp.dsolve(ODE, Uout(t), ics={Uout(0): U0}).subs({RC_sym: RC, t: 0.5, Uout(0.5): 1})

solution_2 = sp.dsolve(ODE.subs(Uin, 0), Uout(t), ics={Uout(0.5): solution_1.rhs.subs(t, 0.5)})
solution = sp.lambdify(t, sp.Piecewise((solution_1.rhs, t <= 0.5), (solution_2.rhs, t > 0.5)))
print(solution_1)
'''





# Plot the results
plt.plot(t_interval, Uout_values, label="Euler's Method (RC Circuit)", color='blue')
plt.xlabel('Time (t) [seconds]')
plt.ylabel('Output Voltage (Uout) [V]')
plt.title('RC Circuit: Output Voltage vs Time')
plt.grid(True)
plt.legend()
#plt.show()
