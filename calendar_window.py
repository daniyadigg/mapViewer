import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget

class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Календарь')
        self.setGeometry(200, 200, 400, 300)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())