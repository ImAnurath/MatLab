from sympy import symbols, sin, exp, pi, diff
from scipy.integrate import solve_ivp, quad
import numpy as np
import matplotlib.pyplot as plt
import math
x = symbols('x')
ref_point1 = 1
ref_point2 = pi/3
ref_point3 = 0
def function_1(x): # First Derivative = 1 - Second Derivative 6
    f1 = x**3 - 2*x
    f_1_prime = diff(f1, x, 1).subs(x, ref_point1)
    return f1, f_1_prime
def function_2(x): # First Derivative = 0.5 - Second Derivative -0.8660254037
    f2 = sin(x)
    f_2_prime = diff(f2, x, 1).subs(x, ref_point2)
    return f2
def function_3(x): # First Derivative = 1 - Second Derivative 1
    f3 = exp(x)
    f_3_prime = diff(f3, x, 1).subs(x, ref_point3)
    return f3 
def function_derivative(func, order, value):
    if func == 1:
        return diff(function_1(x), x, order).subs(x, value)
    elif func == 2:
        return diff(function_2(x), x, order).subs(x, value)
    elif func == 3:
        return diff(function_3(x), x, order).subs(x, value)
    return
''' Function Parameters '''
h_1 = 0.1
h_2 = 0.01
# --------------------------------------------------------
''' F` Prime 
    1- (f1 - f_minus_1)(2 * h)
    2- (-f2 + 8*f1 - 8*f_minus_1 + f_minus_2) / 12h
'''
# Function 1 - (f1 - f_minus_1)(2 * h)
f_prime_column1 = []
for h in [h_1, h_2]:
    f1 = function_1(ref_point1 + h)
    f_minus_1 = function_1(ref_point1 - h)
    f_prime_column1.append((f1 - f_minus_1) / (2 * h))

# Function 2 - (-f2 + 8*f1 - 8*f_minus_1 + f_minus_2) / 12h
f_prime_column2 = []
for h in [h_1, h_2]:
    f2 = function_2(ref_point2 + h)
    f_minus_2 = function_2(ref_point2 - h)
    f1 = function_1(ref_point1 + h)
    f_minus_1 = function_1(ref_point1 - h)
    f_prime_column2.append((-f2 + 8*f1 - 8*f_minus_1 + f_minus_2) / (12 * h_1))

''' diff(f_1(x), x).subs(x, ref_point1) '''
#print(f"f'(x):\n h = {h_1}: {f_prime_column1[0]} Error: {1 - f_prime_column1[0]},\n h = {h_2}: {f_prime_column1[1]} Error: {1 - f_prime_column1[1]}\n")
# --------------------------------------------------------

'''
    F`` Prime
    1- (f1 - f0 + f_minus_1)(h**2)
    2- (-f2 + 16f1 - 30f0 + 16f_minus_1 - f_minus_2) / (12h)
    I am going to assume f0 is without +-h so it is on exactly reference point for f1 which is = 1
'''
f_double_prime_column1 = []
for h in [h_1, h_2]:
    f1 = function_1(ref_point1 + h)
    f0 = function_1(ref_point1)
    f_minus_1 = function_1(ref_point1 - h)
    f_double_prime_column1.append((f1 - f0 + f_minus_1) / (h**2))

f_double_prime_column2 = []
for h in [h_1, h_2]:
    f2 = function_2(ref_point2 + h)
    f0 = function_1(ref_point1)
    f_minus_2 = function_2(ref_point2 - h)
    f1 = function_1(ref_point1 + h)
    f_minus_1 = function_1(ref_point1 - h)
    f_double_prime_column2.append((-f2 + 16*f1 - 30*f0 + 16*f_minus_1 - f_minus_2) / (12 * h))

#print(f"f''(x):\n h = {h_1}: {f_double_prime_column1[0]} Error: {0},\n h = {h_2}: {f_double_prime_column1[1]} Error: {0}\n")
'''
def taylor_series_expansion(function, steps, h, value):
    f_pos = []
    f_neg = []
    for i in range(steps + 1): # [0, 1, 2 , 3 , steps-1]
        f_pos.append(np.sum((h**i)/math.factorial(i)*function_derivative(function, i, value))) # Formula from page 8
        f_neg.append(np.sum((-h**i)/math.factorial(i)*function_derivative(function, i, value)))
        
        
    return f_pos, f_neg
taylor_series_expansion(function= 1,steps= 3, h= h_1, value= ref_point1)
'''