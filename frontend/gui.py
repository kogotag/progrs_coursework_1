import sys
from PyQt5.QtWidgets import *
from backend.tasks import *
from error_window import *

error_window = None


def try_diff_task(step, start, end):
    global error_window
    try:
        step = float(step)
        start = float(start)
        end = float(end)
    except:
        error_window = ErrorWindow("Ошибка")
        return
    derivative_task(step, start, end)


def try_integral_task(step, start, end, text_field: QTextEdit):
    global error_window
    try:
        step = float(step)
        start = float(start)
        end = float(end)
    except:
        error_window = ErrorWindow("Ошибка")
        return
    res = integral_task(step, start, end)
    text_field.setText(res)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Программирование: курсовая")
grid = QGridLayout()

diffLabel = QLabel("Дифференцирование")
diffStepLabel = QLabel("Введите шаг")
diffStepField = QLineEdit()
diffIntervalStartLabel = QLabel("Введите начало промежутка")
diffIntervalStartField = QLineEdit()
diffIntervalEndLabel = QLabel("Введите конец промежутка")
diffIntervalEndField = QLineEdit()
diffTaskButton = QPushButton("Выполнить")
diffTaskButton.clicked.connect(lambda: try_diff_task(diffStepField.text(),
                                                     diffIntervalStartField.text(),
                                                     diffIntervalEndField.text()))

intLabel = QLabel("Интегрирование")
intStepLabel = QLabel("Введите шаг")
intStepField = QLineEdit()
intIntervalStartLabel = QLabel("Введите начало промежутка")
intIntervalStartField = QLineEdit()
intIntervalEndLabel = QLabel("Введите конец промежутка")
intIntervalEndField = QLineEdit()
intResultLabel = QLabel("Результат интегрирования:")
intResultField = QTextEdit()
intResultField.setReadOnly(True)
intTaskButton = QPushButton("Выполнить")
intTaskButton.clicked.connect(lambda: try_integral_task(intStepField.text(),
                                                        intIntervalStartField.text(),
                                                        intIntervalEndField.text(),
                                                        intResultField))

grid.addWidget(diffLabel, 0, 0)
grid.addWidget(diffStepLabel, 1, 0)
grid.addWidget(diffStepField, 1, 1)
grid.addWidget(diffIntervalStartLabel, 2, 0)
grid.addWidget(diffIntervalStartField, 2, 1)
grid.addWidget(diffIntervalEndLabel, 3, 0)
grid.addWidget(diffIntervalEndField, 3, 1)
grid.addWidget(diffTaskButton, 4, 0)
grid.addWidget(intLabel, 6, 0)
grid.addWidget(intStepLabel, 7, 0)
grid.addWidget(intStepField, 7, 1)
grid.addWidget(intIntervalStartLabel, 8, 0)
grid.addWidget(intIntervalStartField, 8, 1)
grid.addWidget(intIntervalEndLabel, 9, 0)
grid.addWidget(intIntervalEndField, 9, 1)
grid.addWidget(intTaskButton, 10, 0)
grid.addWidget(intResultLabel, 11, 0)
grid.addWidget(intResultField, 12, 0)

window.setLayout(grid)
window.show()

sys.exit(app.exec_())
