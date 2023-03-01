"""
Final Implementation of WeatherData.  Complete all the TODOs
"""


class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temperature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    """
    Takes all temperature attributes and stores them in a list to be able to show stats like the average, highest, and lowest
    """
    # The StatisticsDisplay class should keep track of the min/average/max
    # measurements and display them.
    def __init__(self, weatherData):
        self.temperature_list = []
        self.humidity_list = []
        self.pressure_list = []

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temperature_list.append(temperature)
        self.humidity_list.append(humidity)
        self.pressure_list.append(pressure)
        self.display()

    def display(self):
        print("Temperature: Min:", min(self.temperature_list),
              "Avg:", sum(self.temperature_list) / len(self.temperature_list),
              "Max:", max(self.temperature_list), '\n')
        print("Humidity: Min:", min(self.humidity_list),
              "Avg:", sum(self.humidity_list) / len(self.humidity_list),
              "Max:", max(self.humidity_list), '\n')
        print("Pressure: Min:", min(self.pressure_list),
              "Avg:", sum(self.pressure_list) / len(self.pressure_list),
              "Max:", max(self.pressure_list), '\n')


class ForecastDisplay(Observer):
    # The ForecastDisplay class shows the weather forecast based on the current
    # temperature, humidity and pressure. Use the following formulas :
    # forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
    # forecast_humidity = humidity - 0.9 * humidity
    # forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
    def __init__(self, weatherData):
        self.forecast_temperature = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0

        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.forecast_temperature = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humidity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("Weather forecast: Temperature:", self.forecast_temperature,
              "Humidity:", self.forecast_humidity,
              "Pressure:", self.forecast_pressure)

#Where the Subject and the observer meet
class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        # TODO: Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concrete instance
        # of the Subject class so the they get the measurements' updates.
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)



if __name__ == "__main__":
    w = WeatherStation()
    w.main()
