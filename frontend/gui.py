import sys

from backend.tasks import *
from .error_window import *


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.error_window = None
        self.diff_task = None
        self.int_task = None

        self.diff_domain = [MathInterval(-sys.float_info.max, -2, False, False),
                            MathInterval(-2 / math.sqrt(3), 0, True, False),
                            MathInterval(2 / math.sqrt(3), 2, True, False)]

        self.int_domain = [MathInterval(0, sys.float_info.max, False, False)]

        self.setWindowTitle("Программирование: курсовая")
        self.grid = QGridLayout()

        self.diffLabel = QLabel("Дифференцирование")
        self.diffStepLabel = QLabel("Введите шаг")
        self.diffStepField = QLineEdit()
        self.diffIntervalStartLabel = QLabel("Введите начало промежутка")
        self.diffIntervalStartField = QLineEdit()
        self.diffIntervalEndLabel = QLabel("Введите конец промежутка")
        self.diffIntervalEndField = QLineEdit()
        self.diffTaskButton = QPushButton("Рассчитать")
        self.diffTaskButton.clicked.connect(self.try_diff_task)
        self.diffTaskGraphButton = QPushButton("Графики")
        self.diffTaskGraphButton.clicked.connect(self.try_diff_graphs)
        self.diffTaskErrorsButton = QPushButton("Погрешности")
        self.diffTaskErrorsButton.clicked.connect(self.try_diff_errors)

        self.intLabel = QLabel("Интегрирование")
        self.intStepLabel = QLabel("Введите шаг")
        self.intStepField = QLineEdit()
        self.intIntervalStartLabel = QLabel("Введите начало промежутка")
        self.intIntervalStartField = QLineEdit()
        self.intIntervalEndLabel = QLabel("Введите конец промежутка")
        self.intIntervalEndField = QLineEdit()
        self.intResultLabel = QLabel("Результат интегрирования:")
        self.intResultField = QTextEdit()
        self.intResultField.setReadOnly(True)
        self.intTaskButton = QPushButton("Выполнить")
        self.intTaskButton.clicked.connect(self.try_int_task)

        self.grid.addWidget(self.diffLabel, 0, 0)
        self.grid.addWidget(self.diffStepLabel, 1, 0)
        self.grid.addWidget(self.diffStepField, 1, 1)
        self.grid.addWidget(self.diffIntervalStartLabel, 2, 0)
        self.grid.addWidget(self.diffIntervalStartField, 2, 1)
        self.grid.addWidget(self.diffIntervalEndLabel, 3, 0)
        self.grid.addWidget(self.diffIntervalEndField, 3, 1)
        self.grid.addWidget(self.diffTaskButton, 4, 0)
        self.grid.addWidget(self.diffTaskGraphButton, 4, 1)
        self.grid.addWidget(self.diffTaskErrorsButton, 4, 2)
        self.grid.addWidget(self.intLabel, 6, 0)
        self.grid.addWidget(self.intStepLabel, 7, 0)
        self.grid.addWidget(self.intStepField, 7, 1)
        self.grid.addWidget(self.intIntervalStartLabel, 8, 0)
        self.grid.addWidget(self.intIntervalStartField, 8, 1)
        self.grid.addWidget(self.intIntervalEndLabel, 9, 0)
        self.grid.addWidget(self.intIntervalEndField, 9, 1)
        self.grid.addWidget(self.intTaskButton, 10, 0)
        self.grid.addWidget(self.intResultLabel, 11, 0)
        self.grid.addWidget(self.intResultField, 12, 0)

        self.setLayout(self.grid)

    def show_error(self,
                   message: str):
        self.error_window = ErrorWindow(message)

    def diff_step_check(self):
        step = 0
        try:
            step = float(self.diffStepField.text())
        except:
            self.show_error("Шаг не является числом")
            return False

        if step <= 0:
            self.show_error("Шаг должен быть положительным числом")
            return False

        return True

    def int_step_check(self):
        step = 0
        try:
            step = float(self.intStepField.text())
        except ValueError:
            self.show_error("Шаг не является числом")
            return False

        if step <= 0:
            self.show_error("Шаг должен быть положительным числом")
            return False

        return True

    def diff_start_check(self):
        start = 0
        try:
            start = float(self.diffIntervalStartField.text())
        except ValueError:
            self.show_error("Начало промежутка не является числом")
            return False

        return True

    def int_start_check(self):
        start = 0
        try:
            start = float(self.intIntervalStartField.text())
        except ValueError:
            self.show_error("Начало промежутка не является числом")
            return False

        inside = False
        for interval in self.int_domain:
            if interval.number_inside(start):
                inside = True
                break

        if not inside:
            self.show_error("Начало промежутка не принадлежит области определения")
            return False

        return True

    def diff_end_check(self):
        end = 0
        try:
            end = float(self.diffIntervalEndField.text())
        except ValueError:
            self.show_error("Конец промежутка не является числом")
            return False

        return True

    def int_end_check(self):
        end = 0
        try:
            end = float(self.intIntervalEndField.text())
        except ValueError:
            self.show_error("Конец промежутка не является числом")
            return False

        inside = False
        for interval in self.int_domain:
            if interval.number_inside(end):
                inside = True
                break

        if not inside:
            self.show_error("Конец промежутка не принадлежит области определения")
            return False

        return True

    def start_end_order_check(self,
                              start: float,
                              end: float):
        if start >= end:
            self.show_error("Начало промежутка должно быть левее конца промежутка")
            return False
        return True

    # TODO: remove
    def test(self):
        print("test")

    def try_diff_task(self):
        if not self.diff_step_check():
            return

        if not self.diff_start_check():
            return

        if not self.diff_end_check():
            return

        step = float(self.diffStepField.text())
        start = float(self.diffIntervalStartField.text())
        end = float(self.diffIntervalEndField.text())

        if not self.start_end_order_check(start, end):
            return

        try:
            self.diff_task = DerivativeTask(
                MathFunction(lambda x: math.log(math.pow((4 - 3 * x ** 2) / (x ** 3 - 4 * x), 0.2)),
                             MathInterval(start, end),
                             self.diff_domain,
                             step),
                MathFunction(
                    lambda x: (x ** 3 - 4 * x) * (-6 * x * (x ** 3 - 4 * x) - (4 - 3 * x ** 2) * (3 * x ** 2 - 4)) / (
                            5 * (4 - 3 * x ** 2) * (x ** 3 - 4 * x) ** 2),
                    MathInterval(start, end),
                    self.diff_domain,
                    step),
                MathInterval(start, end))
        except Exception as e:
            self.show_error(str(e))
            return

    def try_diff_graphs(self):
        if self.diff_task is None:
            self.show_error("Рассчёты не готовы. Воспользуйтесь соответствующей кнопкой")
            return

        self.diff_task.show_graphs()

    def try_diff_errors(self):
        if self.diff_task is None:
            self.show_error("Рассчёты не готовы. Воспользуйтесь соответствующей кнопкой")
            return

        self.diff_task.show_graphs_errors()

    def try_int_task(self):
        if not self.int_step_check():
            return

        if not self.int_start_check():
            return

        if not self.int_end_check():
            return

        step = float(self.intStepField.text())
        start = float(self.intIntervalStartField.text())
        end = float(self.intIntervalEndField.text())

        if not self.start_end_order_check(start, end):
            return
        try:
            self.int_task = IntegralTask(MathFunction(lambda x: (6 + math.sqrt(x ** 3) + math.sqrt(x)) / (math.sqrt(x)),
                                                      MathInterval(start, end),
                                                      self.int_domain,
                                                      step),
                                         MathFunction(lambda x: 12 * math.sqrt(x) + x ** 2 / 2 + x,
                                                      MathInterval(start, end),
                                                      self.int_domain,
                                                      step),
                                         MathInterval(start, end))
            res = self.int_task.run_task()
            self.intResultField.setText(res)
        except Exception as e:
            self.error_window(str(e))
            return
