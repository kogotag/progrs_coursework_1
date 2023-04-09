from classes import *
import math
import numpy as np
import matplotlib.pyplot as plt

a = -10
b = 10


def task(step):
    f = MathFunction(lambda x: math.log(math.pow((4 - 3 * x ** 2) / (x ** 3 - 4 * x), 0.2)),
                     MathInterval(a, b),
                     [MathInterval(a, -2, True, False),
                      MathInterval(-2 / math.sqrt(3), 0, False, False),
                      MathInterval(2 / math.sqrt(3), 2, False, False)],
                     step)

    derivative_analytic = MathFunction(
        lambda x: (x ** 3 - 4 * x) * (-6 * x * (x ** 3 - 4 * x) - (4 - 3 * x ** 2) * (3 * x ** 2 - 4)) / (
                5 * (4 - 3 * x ** 2) * (x ** 3 - 4 * x) ** 2),
        MathInterval(a, b),
        [MathInterval(a, -2, True, False),
         MathInterval(-2 / math.sqrt(3), 0, False, False),
         MathInterval(2 / math.sqrt(3), 2, False, False)],
        step)

    f.plot(label="function")
    derivative_analytic.plot(color="#ff0000", label="analytic derivative")
    f.plot_derivative_left("#9900ff")
    f.plot_derivative_right("#ff0099")
    f.plot_derivative_two_sided("#00ff00")
    f.plot_derivative_lagrange("#0000ff")
    plt.legend()
    plt.show()

    plt.clf()

    plt.plot([a, b], [0, 0], color="#000000")

    f.plot_derivative_left_error(derivative_analytic.function, "#9900ff")
    f.plot_derivative_right_error(derivative_analytic.function, "#ff0099")
    f.plot_derivative_two_sided_error(derivative_analytic.function, "#00ff00")
    f.plot_derivative_lagrange_error(derivative_analytic.function, "#0000ff")
    plt.legend()
    plt.show()


task(0.2)
task(0.075)
task(0.01)
