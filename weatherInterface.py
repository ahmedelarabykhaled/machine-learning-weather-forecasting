import getWeatherData 
import orgainzeData

class WeatherInterfaceUser :
    getWeatherDataClass = None 
    all_days_Weather = None
    tempreatureWeatherDetails = None
    humidityeWeatherDetails = None
    loadCovereWeatherDetails = None
    windspeedWeatherDetails = None
    orgainzeDataClass = None

    def __init__ (self , days):
        self.days = days
        self.getWeatherDataClass = getWeatherData.ModelsPredict(self.days)
        self.all_days_Weather , self.tempreatureWeatherDetails , self.humidityeWeatherDetails , self.loadCovereWeatherDetails , self.windspeedWeatherDetails = self.getWeatherDataClass.WeatherResults()
        self.orgainzeDataClass = orgainzeData.OraginzeData(self.tempreatureWeatherDetails , self.humidityeWeatherDetails , self.windspeedWeatherDetails )

    def AllDaysWeather (self) :
        return self.all_days_Weather

    def FirstDayWeather (self) :
        first_day_weather = self.orgainzeDataClass.getData(1)
        return first_day_weather

    def SecondDayWeather (self) :
        second_day_weather = self.orgainzeDataClass.getData(2)
        return second_day_weather

    def ThirdDayWeather (self) :
        third_day_weather = self.orgainzeDataClass.getData(3)
        return third_day_weather

    def FourthDayWeather (self) :
        fourth_day_weather = self.orgainzeDataClass.getData(4)
        return fourth_day_weather

    def FivthDayWeather (self) :
        fivth_day_weather = self.orgainzeDataClass.getData(5)
        return fivth_day_weather
