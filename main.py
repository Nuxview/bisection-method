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

# Import libraries for calculation and chart plotting
import numpy as np
import matplotlib.pyplot as plt

# Define the equation to solve
def f(x):
    return x**3 - x - 2


def bisection_method(f, a, b, tol, iterations=1):
    # Check if f(a) and f(b) are of different signs
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Scalars a and b do not bound a root.")

    # Calculate the midpoint of a and b
    midpoint = (a + b) / 2

    # Counter to track number of iterations
    iterations += 1

    # Case where the midpoint is the root
    if np.abs(f(midpoint)) < tol:
        return midpoint, iterations

    # Make the midpoint a or b depending on the sign
    if np.sign(f(a)) == np.sign(f(midpoint)):
        return bisection_method(f, midpoint, b, tol, iterations)
    else:
        return bisection_method(f, a, midpoint, tol, iterations)

# Calculate values (x,y)
def draw_chart(f):
    y_values = []
    for i in range(0, 5):
        y_values.append(f(i))

    # Plot the chart using calculated (x,y) values
    plt.plot([0, 1, 2, 3, 4], y_values)
    plt.ylabel("Y-axis")
    plt.xlabel("X-axis")
    plt.show()


def main():
    # Pass in values to get approximate root
    root, iterations = bisection_method(f, 1, 2, 1e-6)
    print("Root =", round(root, 6), "\nIterations =", iterations)

    # Draw the chart
    draw_chart(f)


if __name__ == "__main__":
    main()
