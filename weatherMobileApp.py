import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
import dataDays
import getWeather

kivy.require("1.7.1")

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.idx = Index
    def build(self):

        Screen = BoxLayout()
        labels_layout = BoxLayout(orientation ="vertical")
        Tempreature_Label = Label(text = "Tempreature is " +str(WeatherResults [self.idx][0]) )
        Humidity_Label = Label(text = "humidity is " +str(WeatherResults[self.idx][1]))
        Wind_Label = Label(text="The wind is " +str(WeatherResults[self.idx][2]))
        LoadCover_Label = Label(text="The load Cover is "+str(WeatherResults[self.idx][3]))
        Summary_Label = Label(text="The day is "+ str(WeatherResults[self.idx][4]))
        labels_layout.add_widget(Tempreature_Label)
        labels_layout.add_widget(Humidity_Label)
        labels_layout.add_widget(Wind_Label)
        labels_layout.add_widget(LoadCover_Label)
        labels_layout.add_widget(Summary_Label)
        Screen.add_widget(labels_layout)
        buttons_layout = BoxLayout()
        Next_btn = Button (text = "Next day" ,
                           font_size="20sp",
                           background_color= [0 , 1 , 0 , 1],
                           color=(1, 1, 1, 1),
                           size=(32, 32),
                           size_hint=(.2, .2),
                           pos=(300, 250) ,
                           on_press=self.CallNext
                           )
        buttons_layout.add_widget(Next_btn)
        Prev_btn = Button (
            text="Previous day",
            font_size="20sp",
            background_color=[1, 0, 1, 0],
            color=(1, 1, 1, 1),
            size=(32, 32),
            size_hint=(.2, .2),
            pos=(300, 250) ,
            on_press = self.CallPrev
        )
        buttons_layout.add_widget(Prev_btn)
        Screen.add_widget(buttons_layout)
        return Screen

    def CallNext (self , event) :
        if (self.idx < 5):
            self.idx = self.idx + 1
        else:
            self.idx = 5
        self.build()

    def CallPrev(self , event):
        if(self.idx > -1) :
            self.idx = self.idx - 1
        else:
            self.idx = 0

        self.build()





if __name__ == '__main__':
    global WeatherResults
    global Index
    Index = 0
    days = dataDays.Includes()
    days = days.getDays()
    ModelWeather = getWeather.ModelsPredict(days, [])
    WeatherResults = ModelWeather.WeatherResults()
    app = MainApp()
    app.run()