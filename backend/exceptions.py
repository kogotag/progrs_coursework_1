class MathIntervalBoundsError(Exception):
    """Класс исключения для границ промежутка"""

    def __str__(self):
        return "interval.start больше либо равен interval.end"


class MathIntervalStepError(Exception):
    """Класс исключения для шага в методах, возвращающих список элементов промежутка"""

    def __str__(self):
        return "step больше длины промежутка"
