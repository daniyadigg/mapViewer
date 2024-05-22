import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from datetime import datetime
import pytz

class TimeZonesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Время мировых столиц')
        self.setGeometry(200, 200, 400, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        cities = [
            ("Москва", "Europe/Moscow"),
            ("Лондон", "Europe/London"),
            ("Нью-Йорк", "America/New_York"),
            ("Токио", "Asia/Tokyo"),
            ("Сидней", "Australia/Sydney")
        ]

        for city, tz in cities:
            time_zone = pytz.timezone(tz)
            city_time = datetime.now(time_zone).strftime('%Y-%m-%d %H:%M:%S')
            label = QLabel(f"{city}: {city_time}")
            layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeZonesWindow()
    window.show()
    sys.exit(app.exec_())