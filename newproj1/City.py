class City:

    def __init__(self, city_name, temperature, weather_type, precipitation_chance, humidity, wind_speed):
        self.city_name = city_name
        self.temperature = temperature
        self.weather_type = weather_type
        self.precipitation_chance = precipitation_chance
        self.humidity = humidity
        self.wind_speed = wind_speed

    def print_summary(self):
        print(
            'Weather forecasts for {} - {}\nTemperature: {}°\nChance of precipitation: {}%\nHumidity: {}%\nWind speed: {} km/h\n'
            .format(self.city_name, self.weather_type, self.temperature, int(self.precipitation_chance * 100),
                    int(self.humidity * 100), self.wind_speed))

#london = City('London', 21, 'Sunny', 0.1, 0.63, 10)
#london.print_summary()

#Eindhoven = City('Eindhoven',13, 'Sunny', 0, 0.53, 8)
#Eindhoven.print_summary()