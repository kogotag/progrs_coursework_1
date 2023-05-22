from frontend.gui import *

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())
