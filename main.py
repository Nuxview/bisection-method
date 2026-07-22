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

# Ask for equation and interval from the user
# You can input your equation using standard Python math syntax.
# Examples:
# - Euler's number (e): np.exp(x) - 4*x
# - Trig functions: np.sin(x) + np.cos(x)
equation = input("Enter the equation: ")
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))

# Define the equation to solve
def f(x):
    return eval(equation)

def bisection_method(f, a, b, tol, iterations=1):
    # Check if f(a) and f(b) are of different signs
    if np.sign(f(a)) == np.sign(f(b)):
        print("Scalars a and b do not bound a root.")
        exit()

    # Calculate the midpoint of a and b
    midpoint = (a + b) / 2

    # Counter to track number of iterations
    iterations += 1

    # Check if midpoint is the root
    if np.abs(f(midpoint)) < tol:
        return midpoint, iterations

    # Make the midpoint a or b depending on the sign
    if np.sign(f(a)) == np.sign(f(midpoint)):
        return bisection_method(f, midpoint, b, tol, iterations)
    else:
        return bisection_method(f, a, midpoint, tol, iterations)

# Function to draw the chart
def draw_chart(f):
    # Calculate y-values for the function
    y_values = []
    for i in range(0, 5):
        y_values.append(f(i))

    # Plot the chart using calculated (x,y) values
    plt.plot([0, 1, 2, 3, 4], y_values)

    # Add title, grid and axis labels
    plt.title("Function Chart for " + str(f))
    plt.ylabel("Y-axis")
    plt.xlabel("X-axis")
    plt.grid(True)

    # Ask the user if they want to see the chart
    image_name = 'bisection_chart.png'
    if input("\nShow chart? (y/n): ").lower() == "n":
        print("Exiting...")
        exit()
    else:
        if input("Separate window or save to image? (window/image): ").lower() == "image":
            plt.savefig(image_name)
        else:
            plt.show()


def main():
    # Pass in values to get approximate root
    root, iterations = bisection_method(f, a=a, b=b, tol=1e-6)
    print("\nRoot =", round(root, 6), "\nIterations =", iterations)

    # Draw the chart
    draw_chart(f)

# Entry point of the program
if __name__ == "__main__":
    main()
