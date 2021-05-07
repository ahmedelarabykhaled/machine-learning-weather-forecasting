

import dataDays 
import weatherInterface 

days = dataDays.Includes()
days = days.getDays()
first_day_weather = weatherInterface.WeatherInterfaceUser(days)
first_day_weather = first_day_weather.AllDaysWeather()

print(first_day_weather)














