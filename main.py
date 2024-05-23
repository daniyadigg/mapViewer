import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from time_zone_window import TimeZonesWindow


class MapViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Выбор источника карты')
        self.setGeometry(100, 100, 1600, 1500)

        # Создание главного виджета и макета
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # Создание виджета веб-карты
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.windy.com/"))
        layout.addWidget(self.web_view, 3)  # Добавляем виджет карты, занимая большую часть

        # Создание боковой панели с кнопками
        button_panel = QVBoxLayout()

        self.windy_button = QPushButton('Windy')
        self.windy_button.clicked.connect(self.show_windy)
        button_panel.addWidget(self.windy_button)

        self.flightradar_button = QPushButton('Flightradar24')
        self.flightradar_button.clicked.connect(self.show_flightradar)
        button_panel.addWidget(self.flightradar_button)

        self.osm_button = QPushButton('OpenStreetMap')
        self.osm_button.clicked.connect(self.show_osm)
        button_panel.addWidget(self.osm_button)

        self.time_zone_button = QPushButton('Часовые пояса')
        self.time_zone_button.clicked.connect(self.show_time_zones)
        button_panel.addWidget(self.time_zone_button)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_panel.addItem(spacer)

        self.calendar_button = QPushButton('Календарь')
        #self.calendar_button.clicked.connect(self.show_calendar)
        button_panel.addWidget(self.calendar_button)

        layout.addLayout(button_panel)  # Добавляем панель кнопок

    def show_windy(self):
        self.web_view.setUrl(QUrl("https://www.windy.com/"))

    def show_flightradar(self):
        self.web_view.setUrl(QUrl("https://www.flightradar24.com/"))

    def show_osm(self):
        self.web_view.setUrl(QUrl("https://www.openstreetmap.org/"))

    def show_time_zones(self):
        self.time_zones_window = TimeZonesWindow()
        self.time_zones_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapViewer()
    window.show()
    sys.exit(app.exec_())
