# Instructions

# Each group is required to implement the assigned numerical method using Python. The
# objective is to demonstrate an understanding of the algorithm, its implementation, and
# interpretation of the results.

# Each group should submit a report containing the following:
# 1. A brief introduction to the assigned numerical method.
# 2. The mathematical formulation of the method.
# 3. The algorithm or pseudocode.
# 4. A well-documented Python program implementing the method.
# 5. Screenshots of the program execution.
# 6. A table showing the iterations (where applicable).
# 7. Appropriate plots illustrating the results (e.g., convergence plots, interpolation
# curves, function plots, etc.).
# 8. Interpretation and discussion of the obtained results.
# 9. The advantages and limitations of the numerical method.
# 10. A comparison of the obtained solution with the exact solution or Python built-in
# numerical functions (where applicable).
# 11. A brief conclusion.

# Bisection Method
# Write a Python program to approximate the root of
# f (x) = x^3 − x − 2
# on the interval [1, 2]. Use a tolerance of 10−6 . Report the approximate root, the number
# of iterations, and plot the function.

import numpy as np
# import matplotlib as plt


def bisection_method(f, a, b, tol):

    # Check if f(a) and f(b) are of different signs
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Scalars a and b do not bound a root.")

    # Calculate the midpoint of a and b
    midpoint = (a + b) / 2

    # Case where the midpoint is the root
    if np.abs(f(midpoint)) < tol:
        return midpoint

    # Make the midpoint a or b depending on the sign
    elif np.sign(f(a)) == np.sign(f(midpoint)):
        return bisection_method(f, midpoint, b, tol)
    elif np.sign(f(b)) == np.sign(f(midpoint)):
        return bisection_method(f, a, midpoint, tol)


def main():
    f = lambda x: x**3 - x - 2
    r1 = bisection_method(f, 1, 2, 0.1)
    print("r1 = ", r1)
    r01 = bisection_method(f, 1, 2, 0.01)
    print("r01 = ", r01)

    print("f(r1) = ", f(r1))
    print("f(r01) = ", f(r01))


if __name__ == "__main__":
    main()
