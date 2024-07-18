# Creates a class for city forecasts containing the city name, its temperature, condition, and humidity
class CityForecast:
    # constructor for the class protected variables
    def __init__(self, city, temperature, condition, humidity):
        self._city_name = city
        self._temperature = temperature
        self._condition = condition
        self._humidity = humidity

    # getters for all the class variables
    def get_city_name(self):
        return self._city_name

    def get_temperature(self):
        return self._temperature

    def get_condition(self):
        return self._condition

    def get_humidity(self):
        return self._humidity
    
    # setters for the class variables
    def set_city_name(self, city):
        self._city_name = city

    def set_temperature(self, new_temperature):
        self._temperature = new_temperature

    def set_condition(self, new_condition):
        self.condition = new_condition

    def set_humidity(self, new_humidity):
        self.humidity = new_humidity

    # function for displaying the city forecast
    def display_forecast(self):
        print(f"Weather in {self._city_name}: {self._temperature} degrees, {self._condition}, Humidity: {self._humidity}%")