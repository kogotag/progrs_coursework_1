from typing import Callable

from exceptions import *

import matplotlib.pyplot as plt
import math
import numpy as np

PYTHON_ARITHMETIC_ERROR = 0.0001


class MathInterval:
    def __init__(self,
                 start: float,
                 end: float,
                 include_start: bool = True,
                 include_end: bool = True):
        self.start = start

        if end <= start:
            raise MathIntervalBoundsError

        self.end = end
        self.include_start = include_start
        self.include_end = include_end

    def get_elements_with_step(self,
                               step: float):
        a = self.start

        if not self.include_start:
            a = self.start + step

        if self.start + step > self.end:
            raise MathIntervalStepError

        b = self.end

        if not self.include_end:
            b = self.end - step

        result = [a + PYTHON_ARITHMETIC_ERROR]
        i = a + step
        while i <= b - step:
            result.append(i)
            i += step
        result.append(b - PYTHON_ARITHMETIC_ERROR)

        return result

    def inside(self,
               another=None):
        if not isinstance(another, self.__class__):
            return False
        return another.number_inside(self.start) and another.number_inside(self.end)

    def number_inside(self,
                      number: float):
        return (self.include_start and number == self.start) \
            or (self.start + PYTHON_ARITHMETIC_ERROR < number < self.end - PYTHON_ARITHMETIC_ERROR) \
            or (self.include_end and number == self.end)


class MathFunction:
    def __init__(self,
                 function: Callable[[float], float],
                 desired_segment: MathInterval = MathInterval(0, 1),
                 domain=None,
                 step: float = 0.1):
        if domain is None:
            domain = [MathInterval(0, 1)]

        self.desired_segment = desired_segment
        self.domain = domain
        self.function = function
        self.step = step

        x_list = []
        y_list = []

        for i in desired_segment.get_elements_with_step(step):
            if not self.inside_domain(i):
                continue
            x_list.append(i)
            y_list.append(function(i))

        self.x = x_list
        self.y = y_list

    def get_value(self,
                  x: float):
        return self.function(x)

    def inside_domain(self,
                      x: float):
        for interval in self.domain:
            if interval.number_inside(x):
                return True
        return False

    def plot(self,
             label: str = "",
             color: str = "#000000"):
        j = 0
        for interval in self.domain:
            x_list = []
            y_list = []
            for i in interval.get_elements_with_step(self.step):
                x_list.append(i)
                y_list.append(self.function(i))

            if j == 0:
                plt.plot(x_list, y_list, color=color, label=label)
            else:
                plt.plot(x_list, y_list, color=color)
            j += 1

    def plot_derivative_left(self,
                             color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(1, len(interval_x)):
                x_list.append(interval_x[i])
                derivative_list.append((interval_y[i] - interval_y[i - 1]) / self.step)

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="left-sided derivative")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_left_error(self,
                                   derivative_analytic: Callable[[float], float],
                                   color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(1, len(interval_x)):
                x_list.append(interval_x[i])
                derivative_list.append(
                    (interval_y[i] - interval_y[i - 1]) / self.step - derivative_analytic(interval_x[i]))

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="left-sided derivative error")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_right(self,
                              color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(0, len(interval_x) - 1):
                x_list.append(interval_x[i])
                derivative_list.append((interval_y[i + 1] - interval_y[i]) / self.step)

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="right-sided derivative")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_right_error(self,
                                    derivative_analytic: Callable[[float], float],
                                    color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(0, len(interval_x) - 1):
                x_list.append(interval_x[i])
                derivative_list.append(
                    (interval_y[i + 1] - interval_y[i]) / self.step - derivative_analytic(interval_x[i]))

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="right-sided derivative error")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_two_sided(self,
                                  color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(1, len(interval_x) - 1):
                x_list.append(interval_x[i])
                derivative_list.append((interval_y[i + 1] - interval_y[i - 1]) / 2 / self.step)

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="two-sided derivative")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_two_sided_error(self,
                                        derivative_analytic: Callable[[float], float],
                                        color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(1, len(interval_x) - 1):
                x_list.append(interval_x[i])
                derivative_list.append(
                    (interval_y[i + 1] - interval_y[i - 1]) / 2 / self.step - derivative_analytic(interval_x[i]))

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="two-sided derivative error")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_lagrange(self,
                                 color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(0, math.floor(len(interval_x) / 3) * 3, 3):
                x_list.append(interval_x[i])
                x_list.append(interval_x[i + 1])
                x_list.append(interval_x[i + 2])
                derivative_list.append((-3 * interval_y[i] + 4 * interval_y[i + 1] - interval_y[i + 2]) / 2 / self.step)
                derivative_list.append((interval_y[i + 2] - interval_y[i]) / 2 / self.step)
                derivative_list.append((interval_y[i] - 4 * interval_y[i + 1] + 3 * interval_y[i + 2]) / 2 / self.step)

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="lagrange derivative")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def plot_derivative_lagrange_error(self,
                                       derivative_analytic: Callable[[float], float],
                                       color: str = "#000000"):
        j = 0
        for interval in self.domain:
            interval_x = interval.get_elements_with_step(self.step)
            interval_y = np.array([self.function(i) for i in interval_x])
            x_list = []
            derivative_list = []
            for i in range(0, math.floor(len(interval_x) / 3) * 3, 3):
                x_list.append(interval_x[i])
                x_list.append(interval_x[i + 1])
                x_list.append(interval_x[i + 2])
                derivative_list.append((-3 * interval_y[i] + 4 * interval_y[i + 1] - interval_y[
                    i + 2]) / 2 / self.step - derivative_analytic(interval_x[i]))
                derivative_list.append(
                    (interval_y[i + 2] - interval_y[i]) / 2 / self.step - derivative_analytic(interval_x[i + 1]))
                derivative_list.append((interval_y[i] - 4 * interval_y[i + 1] + 3 * interval_y[
                    i + 2]) / 2 / self.step - derivative_analytic(interval_x[i + 2]))

            if j == 0:
                plt.plot(x_list, derivative_list, color=color, label="lagrange derivative error")
            else:
                plt.plot(x_list, derivative_list, color=color)
            j += 1

    def integral_rectangle(self,
                           segment: MathInterval):
        x_list = segment.get_elements_with_step(self.step)
        y_list = np.array([self.function(x) for x in x_list])
        integral_sum = 0
        for i in range(0, len(x_list) - 1):
            integral_sum += self.step * y_list[i]
        return integral_sum

    def integral_parabolic(self,
                           segment: MathInterval):
        x_list = segment.get_elements_with_step(self.step)
        y_list = np.array([self.function(x) for x in x_list])
        integral_sum = 0
        for i in range(0, len(x_list) - 1):
            integral_sum += (y_list[i] + y_list[i + 1] + 4 * self.function(x_list[i] + self.step / 2)) * self.step / 6
        return integral_sum

    def integral_trapezium(self,
                           segment: MathInterval):
        x_list = segment.get_elements_with_step(self.step)
        y_list = np.array([self.function(x) for x in x_list])
        integral_sum = 0
        for i in range(0, len(x_list) - 1):
            integral_sum += (y_list[i] + y_list[i + 1]) / 2 * self.step
        return integral_sum
