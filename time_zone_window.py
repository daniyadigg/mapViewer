import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from datetime import datetime
import pytz
from PyQt5.QtCore import QTimer

class TimeZonesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Время мировых столиц')
        self.setGeometry(200, 200, 400, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)

        self.cities = [
            ("Москва", "Europe/Moscow"),
            ("Лондон", "Europe/London"),
            ("Нью-Йорк", "America/New_York"),
            ("Токио", "Asia/Tokyo"),
            ("Сидней", "Australia/Sydney")
        ]

        self.labels = []
        for city, _ in self.cities:
            label = QLabel(f"{city}:")
            self.layout.addWidget(label)
            self.labels.append(label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_times)
        self.timer.start(1000) # Обновляем каждую секунду

        self.update_times() # Первоначальное обновление

    def update_times(self):
        for i, (city, tz) in enumerate(self.cities):
            time_zone = pytz.timezone(tz)
            city_time = datetime.now(time_zone).strftime('%Y-%m-%d %H:%M:%S')
            self.labels[i].setText(f"{city}: {city_time}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeZonesWindow()
    window.show()
    sys.exit(app.exec_())