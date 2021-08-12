from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from datetime import datetime
from kivy.clock import Clock

KV = """
CustomGrid:
    rows: 2
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        MDToolbar:
            id: bar
            title: 'Welcome'
            elevation: 10
        Widget:
        
    MDFloatLayout:
        MDLabel:
            id: txt
            text: ''
            size_hint_x: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            
        MDFillRoundFlatButton:
            id: btn1
            text: 'press me'
            size_hint_y: None
            pos_hint: {'center_x': 0.2, 'center_y': 0.5}
            on_press: root.wel()
            
        MDFillRoundFlatButton:
            text: 'Date'
            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_press: root.date()
        
        MDFillRoundFlatButton:
            text: 'Increment'
            size_hint_y: None
            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            on_press: root.add()
            
            
"""


class CustomGrid(MDGridLayout):

    def wel(self):
        self.ids.txt.text = 'Hello World'

    def date_(self, value):
        now = datetime.now()
        self.ids.bar.title = now.strftime("%Y-%m-%d %H:%M:%S")

    def date(self):
        Clock.schedule_interval(self.date_, 0)

    def add(self):
        if self.ids.txt.text == 'Hello World':
            self.ids.txt.text = '0'

        self.ids.txt.text = str(int(self.ids.txt.text) + 1)


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    TestApp().run()
