import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional
from keras.models import load_model
import pickle
import statistics
from statistics import mode

class ModelsPredict :
    def __init__(self , days):
      self.days = days
      

    def WeatherResults (self) :
      np_days = self.days
      temp_days = np.array(np_days)
      temp_days = np.reshape(temp_days, (1, temp_days.shape[0], 10))
      tempreature = load_model('modelsPerDays/modeltraingtempdays.h5')
      predicted_Tempreature_details = tempreature.predict(temp_days)
      predicted_Tempreature = self.average(predicted_Tempreature_details)

      humd_days = np.array(np_days)
      humd_days = np.reshape(humd_days, (1, humd_days.shape[0], 10))
      humidity = load_model('modelsPerDays/modeltrainghumiditydays.h5')
      predicted_Humidity_details = humidity.predict(humd_days)
      predicted_Humidity = self.average(predicted_Humidity_details)

      load_days = np.array(np_days)
      load_days = np.reshape(load_days, (1, load_days.shape[0], 10))
      load_cover = load_model('modelsPerDays/modeltraingLoadCoverperdays.h5')
      predicted_LoadCover_details = load_cover.predict(load_days)
      predicted_LoadCover = self.calc_mode(predicted_LoadCover_details)


      wind_days = np_days[:, 5:7]
      wind_days = np.array(wind_days)
      wind_days = np.reshape(wind_days, (1, wind_days.shape[0], 2))
      wind = load_model('modelsPerDays/modelwindtraingperdays.h5')
      predicted_Wind_details = wind.predict(wind_days)
      predicted_Wind = self.average(predicted_Wind_details)

      summaryarray = [[0] * 4 for i in range(5)]
      for i in range(5):
        summaryarray[i][0] = predicted_Tempreature[i]
        summaryarray[i][1] = predicted_Humidity[i]
        summaryarray[i][2] = predicted_Wind[i]
        summaryarray[i][3] = predicted_LoadCover[i]

      summary_model = pickle.load(open('modelsPerDays/summary.h5', 'rb'))
      summaryResult = summary_model.predict(summaryarray)

      weatherResults = [[0] * 5 for i in range(5)]
      for i in range(5):
        weatherResults[i][0] = predicted_Tempreature[i]
        weatherResults[i][1] = predicted_Humidity[i]
        weatherResults[i][2] = predicted_Wind[i]
        weatherResults[i][3] = predicted_LoadCover[i]
        weatherResults[i][4] = summaryResult[i]

      return weatherResults , predicted_Tempreature_details , predicted_Humidity_details , predicted_LoadCover_details , predicted_Wind_details
    
    def average (self , predicted_weather):
      index_start=0
      index_call = 24
      predicted_days =[]
      for i in range (1 , 6) :
          Sum = sum(predicted_weather[0][index_start:index_call])
          predicted_days.append(Sum/24)
          index_start = index_call
          index_call = index_call + 24
      
      return predicted_days


    def calc_mode (self , load_cover_array):
      index_start=0
      index_call = 24
      predicted_days =[]
      for i in range (1 , 6) :
          loadcover_mode = statistics.mode(load_cover_array[0][index_start:index_call])
          predicted_days.append(loadcover_mode)
          index_start = index_call
          index_call = index_call + 24
      
      return predicted_days
