import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plot_functions(func1_str, func2_str, x_range=(-100, 100), num_points=1000):

    func1_str = func1_str.replace("^", "**")
    func1_str = func1_str.replace("log10", "np.log10")
    func1_str = func1_str.replace("sqrt", "np.sqrt")
    func2_str = func2_str.replace("^", "**")
    func2_str = func2_str.replace("log10", "np.log10")
    func2_str = func2_str.replace("sqrt", "np.sqrt")

    func1 = lambda x: eval(func1_str)
    func2 = lambda x: eval(func2_str)

    def difference(x):
        return func1(x) - func2(x)

    try:
        x_solution = fsolve(difference, 0)[0] 
        y_solution = func1(x_solution)  
    except Exception as e:
        print(f"Failed to find intersection: {e}")
        return

    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y1_values = func1(x_values)
    y2_values = func2(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y1_values, label=f"y = {func1_str}")
    plt.plot(x_values, y2_values, label=f"y = {func2_str}")

    plt.plot(x_solution, y_solution, 'ro', label="Intersection")
    plt.annotate(
        f"({x_solution:.2f}, {y_solution:.2f})",
        (x_solution, y_solution),
        textcoords="offset points",
        xytext=(10, 10),
        ha='center',
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of Two Functions")
    plt.legend()
    plt.grid(True)
    plt.show()
