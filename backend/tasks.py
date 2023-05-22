from .classes import *


class DerivativeTask:
    def __init__(self,
                 math_function: MathFunction,
                 derivative_analytic: MathFunction,
                 desired_interval: MathInterval):
        self.math_function = math_function
        self.derivative_analytic = derivative_analytic
        self.desired_interval = desired_interval

    def show_graphs(self):
        self.math_function.plot(label="function")
        self.derivative_analytic.plot(color="#ff0000", label="analytic derivative")
        self.math_function.plot_derivative_left("#9900ff")
        self.math_function.plot_derivative_right("#ff0099")
        self.math_function.plot_derivative_two_sided("#00ff00")
        self.math_function.plot_derivative_lagrange("#0000ff")
        plt.legend()
        plt.show()

    def show_graphs_errors(self):
        a = self.desired_interval.start
        b = self.desired_interval.end
        plt.plot([a, b], [0, 0], color="#000000")
        self.math_function.plot_derivative_left_error(self.derivative_analytic.function, "#9900ff")
        self.math_function.plot_derivative_right_error(self.derivative_analytic.function, "#ff0099")
        self.math_function.plot_derivative_two_sided_error(self.derivative_analytic.function, "#00ff00")
        self.math_function.plot_derivative_lagrange_error(self.derivative_analytic.function, "#0000ff")
        plt.legend()
        plt.show()


class IntegralTask:
    def __init__(self,
                 math_function: MathFunction,
                 antiderivative: MathFunction,
                 desired_interval: MathInterval):
        self.math_function = math_function
        self.antiderivative = antiderivative
        self.desired_interval = desired_interval

    def run_task(self):
        c = self.desired_interval.start
        d = self.desired_interval.end
        step = self.math_function.step

        self.math_function.plot(label="y=y(x)")
        plt.show()

        integral_analytic = self.antiderivative.get_value(d) - self.antiderivative.get_value(c)

        integral_rectangle = self.math_function.integral_rectangle(self.desired_interval)
        integral_parabolic = self.math_function.integral_parabolic(self.desired_interval)
        integral_trapezium = self.math_function.integral_trapezium(self.desired_interval)

        integral_rectangle_error_absolute = math.fabs(integral_rectangle - integral_analytic)
        integral_rectangle_error_relative = round(
            math.fabs(integral_rectangle_error_absolute / integral_analytic * 100), 1)
        integral_parabolic_error_absolute = math.fabs(integral_parabolic - integral_analytic)
        integral_parabolic_error_relative = round(
            math.fabs(integral_parabolic_error_absolute / integral_analytic * 100), 1)
        integral_trapezium_error_absolute = math.fabs(integral_trapezium - integral_analytic)
        integral_trapezium_error_relative = round(
            math.fabs(integral_trapezium_error_absolute / integral_analytic * 100), 1)

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
