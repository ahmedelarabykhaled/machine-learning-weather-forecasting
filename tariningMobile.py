from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout


class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation ="vertical")
        label = Label(text=x,
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        layout.add_widget(label)
        label2 = Label(text="hello assem",
                       size_hint=(.1, .1),
                       pos_hint={'center_x': .1, 'center_y': .2})
        layout.add_widget(label2)
        # layout.clear_widgets()
        button = Button(text='Hello world', size_hint=(.1, .1),
                        pos_hint={'x': .1, 'y': .1})

        layout.add_widget(button)
        button2 = Button(text='Hello world', size_hint=(.1, .1),
                         pos_hint={'x': .1, 'y': .1})

        layout.add_widget(button2)

        return layout


if __name__ == '__main__':
    app = MainApp()
    app.run()
