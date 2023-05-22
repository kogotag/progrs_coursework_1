from .classes import *


def derivative_task(step, a, b):
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


def integral_task(step, c, d):
    f = MathFunction(lambda x: (6 + math.sqrt(x ** 3) + math.sqrt(x)) / (math.sqrt(x)),
                     MathInterval(1, 5),
                     [MathInterval(1, 5)],
                     step)

    f.plot(label="y=y(x)")
    plt.legend()
    plt.show()

    antiderivative_f = MathFunction(lambda x: 12 * math.sqrt(x) + x ** 2 / 2 + x,
                                    MathInterval(c, d),
                                    [MathInterval(c, d)],
                                    step)

    integral_analytic = antiderivative_f.get_value(d) - antiderivative_f.get_value(c)

    integral_rectangle = f.integral_rectangle(MathInterval(c, d))
    integral_parabolic = f.integral_parabolic(MathInterval(c, d))
    integral_trapezium = f.integral_trapezium(MathInterval(c, d))

    integral_rectangle_error_absolute = math.fabs(integral_rectangle - integral_analytic)
    integral_rectangle_error_relative = round(math.fabs(integral_rectangle_error_absolute / integral_analytic * 100), 1)
    integral_parabolic_error_absolute = math.fabs(integral_parabolic - integral_analytic)
    integral_parabolic_error_relative = round(math.fabs(integral_parabolic_error_absolute / integral_analytic * 100), 1)
    integral_trapezium_error_absolute = math.fabs(integral_trapezium - integral_analytic)
    integral_trapezium_error_relative = round(math.fabs(integral_trapezium_error_absolute / integral_analytic * 100), 1)

    res = "Результаты интегрирования функции f(x) на отрезке [" + str(c) + "; " + str(d) + "] с шагом " + str(
        step) + "\nАналитическое решение: " + str(
        integral_analytic) + "\n\nИнтегрирование методом прямоугольников: " + str(
        integral_rectangle) + "\nПогрешность: " + str(integral_rectangle_error_absolute) + " ( " + str(
        integral_rectangle_error_relative) + "% )" + "\n\nИнтегрирование методом парабол: " + str(
        integral_parabolic) + "\nПогрешность: " + str(integral_parabolic_error_absolute) + " ( " + str(
        integral_parabolic_error_relative) + "% )" + "\n\nИнтегрирование методом трапеций: " + str(
        integral_trapezium) + "\nПогрешность: " + str(integral_trapezium_error_absolute) + " ( " + str(
        integral_trapezium_error_relative) + "% )"

    return res
