import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from helpers.api_prod_helper import send_request, http_error_code, emoji

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 400, 400)
        self.setWindowTitle("Current Weather App")
        self.ask_city = QLabel("Enter city name: ", self)
        self.pick_city = QLineEdit(self)
        self.load_weather = QPushButton("Click to load weather", self)
        self.load_temperature = QLabel(self)
        self.weather_emoji = QLabel(self)
        self.weather_description = QLabel(self)
        self.api = "dc4ac3bc9b1ec918e08d17e2ae161e06"       # should apply your API KEY

        self.format()

    def format(self):
        vertical = QVBoxLayout()
        vertical.addWidget(self.ask_city)
        vertical.addWidget(self.pick_city)
        vertical.addWidget(self.load_weather)
        vertical.addWidget(self.load_temperature)
        vertical.addWidget(self.weather_emoji)
        vertical.addWidget(self.weather_description)
        self.setLayout(vertical)

        self.ask_city.setAlignment(Qt.AlignCenter)
        self.pick_city.setAlignment(Qt.AlignCenter)
        self.load_temperature.setAlignment(Qt.AlignCenter)
        self.weather_emoji.setAlignment(Qt.AlignCenter)
        self.weather_description.setAlignment(Qt.AlignCenter)

        self.ask_city.setObjectName("AskCity")
        self.pick_city.setObjectName("PickCity")
        self.load_weather.setObjectName("GetSky")
        self.load_temperature.setObjectName("GetTemp")
        self.weather_emoji.setObjectName("SkyEmoji")
        self.weather_description.setObjectName("SkyWord")

        self.setStyleSheet("""
                            QLabel, QPushButton{
                                    font-family: Helvetica;            }
                            QLabel#AskCity{
                                    font-size: 40px;
                                    font-style: italic;                }
                            QLineEdit#PickCity{
                                    font-size: 25px; 
                                    border: 2px dashed lightgray;
                                    border-radius: 8px;                }
                            QPushButton#GetSky{
                                    font-size: 25px;
                                    color: darkgreen;
                                    font-weight: bold;                 }
                            QPushButton#GetSky:hover{
                                    background-color: lightyellow;            }
                            QLabel#GetTemp{
                                    font-size: 75px;                   }
                            QLabel#SkyEmoji{
                                    font-size: 100px;
                                    font-family: Apple Color Emoji;    }                  
                            QLabel#SkyWord{
                                    font-size: 50px;                   }
                                                                                                """)

        self.load_weather.clicked.connect(self.city_api_status)        # no need declare at the beginning as it is connected to temporary def

    def city_api_status(self):
        city = self.pick_city.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api}"

        try:
            get_response = send_request("GET", url, None)
            get_response.raise_for_status()
            get_data = get_response.json()
            self.good_display(get_data)

        except requests.exceptions.HTTPError:
            error_code = http_error_code(get_response)
            self.bad_display(error_code)

    def good_display(self, get_data):
        kelvin = get_data["main"]["temp"]
        celsius = kelvin - 273.15
        self.load_temperature.setStyleSheet("font-size: 75px")              # remain style from previous invalid input
        self.load_temperature.setText(f"{round(celsius, 0):.0f}°C")

        emoji_code = get_data["weather"][0]["id"]
        emoji_icon = emoji(emoji_code)
        self.weather_emoji.setText(emoji_icon)

        emoji_describe = get_data["weather"][0]["description"]
        self.weather_description.setText(emoji_describe)

    def bad_display(self, error_code):
        self.load_temperature.setStyleSheet("font-size: 30px")
        self.load_temperature.setText(error_code)
        self.weather_emoji.clear()
        self.weather_description.clear()

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
