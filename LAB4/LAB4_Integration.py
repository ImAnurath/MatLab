import numpy as np
from scipy.integrate import quad, trapezoid, simpson
def integrand_1(x):
    return x**3 - 2*x
def integrand_2(x):
    return np.sin(x)
def integrand_3(x):
    return np.exp(-x)
'''
Rombergs method is depricated from Scipy and is used as a base for quad. For all interval size 4 and 8 it is giving out same result. 
So I didn't included it on the for loop downbelow because it is using different abrevations 
'''
result_1 = 0
result_2 = 1
result_3 = 0.63212055883
rombergs_1, rombergs_error_1 = quad(integrand_1, 0, 2, limit = 4)
rombergs_2, rombergs_error_2 = quad(integrand_2, 0, np.pi/2, limit = 4)
rombergs_3, rombergs_error_3 = quad(integrand_3, 0, 1, limit = 4)

print(f"Exact result for integrand 1: {rombergs_1} (Error estimate: {rombergs_error_1})")
print(f"Exact result for integrand 2: {rombergs_2} (Error estimate: {rombergs_error_2})")
print(f"Exact result for integrand 3: {rombergs_3} (Error estimate: {rombergs_error_3})")



for N in [4, 8]:
    x_points = np.linspace(0, 2, N+1)  # For integrand 1 (0 to 2)
    x_points_2 = np.linspace(0, np.pi/2, N+1)  # For integrand 2 (0 to pi/2)
    x_points_3 = np.linspace(0, 1, N+1)  # For integrand 3 (0 to 1)

    for i, (integrand, x_pts, exact_result) in enumerate([(integrand_1, x_points, result_1),
                                                           (integrand_2, x_points_2, result_2),
                                                           (integrand_3, x_points_3, result_3)], start=1):
        y_values = integrand(x_pts)
        trapezoidal = trapezoid(y_values, x_pts)
        simpsons = simpson(y_values, x=x_pts)
        print(f"Variant {i}:")
        print(f"  Trapezoidal Method: {trapezoidal} - Error: {abs(trapezoidal - exact_result)} - N: {N}")
        print(f"  Simpson's Method: {simpsons} - Error: {abs(simpsons - exact_result)} - N: {N}")
        print()