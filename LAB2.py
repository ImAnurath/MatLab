import numpy as np
import matplotlib.pyplot as plt

def func_approx():
    # Clear all variables and close all figures
    plt.close('all')

    # Number of points (N) for interpolation
    N = 21  # You can vary N; increasing it increases the approximation error
    x = np.linspace(-1, 1, N)
    yN = f1(x)

    # Find the Lagrange polynomial coefficients
    l = lagranp(x, yN)

    # To get a smoother curve, use 100 points for evaluation
    xx = np.linspace(-1, 1, 100)
    yl = np.polyval(l[::-1], xx)  # Reverse coefficients for np.polyval

    # Plot the interpolation
    plt.plot(x, yN, '*', label='Data Points')
    plt.plot(xx, yl, label='Lagrange Polynomial')
    plt.plot(xx, f1(xx), label='Original Function')
    plt.grid()
    plt.legend()
    plt.show()


def f1(x):
    """Original function."""
    return 1 / (1 + 8 * x**2)


def lagranp(x, y):
    """
    Compute the Lagrange interpolating polynomial.

    Parameters:
    - x: array of x values
    - y: array of corresponding y values

    Returns:
    - l: coefficients of the Lagrange polynomial
    """
    N = len(x) - 1  # Degree of the polynomial
    l = np.zeros(N + 1)
    L = []

    for m in range(N + 1):
        P = np.array([1.0])
        for k in range(N + 1):
            if k != m:
                # Polynomial multiplication using convolution
                P = np.convolve(P, [1, -x[k]]) / (x[m] - x[k])
        L.append(P)
        l += y[m] * P

    return l


# Run the function approximation
if __name__ == "__main__":
    func_approx()
