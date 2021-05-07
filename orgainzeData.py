import getWeatherData

class OraginzeData :
    def __init__(self , dataTemp , dataHumd , dataWind):
       self.dataTemp = dataTemp
       self.dataHumd = dataHumd
       self.dataWind = dataWind
        
    
    def getData (self , day_number):
        dataOrganized = []
        n= day_number
        start = (n-1) *24
        end = n*24
        hour = 0
        for i in range(start , end) :
            k = str(hour)
            res = k + ":00:00 " + "temprature is " + str(self.dataTemp[0][i]) + " humidity is " +str(self.dataHumd[0][i]) + " wind speed is " +str(self.dataWind[0][i]) 
            dataOrganized.append(res)
            hour = hour + 1 
        
        return dataOrganized 



        
        
        
