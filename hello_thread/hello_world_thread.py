from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.gridlayout import MDGridLayout
from datetime import datetime
from kivy.clock import Clock
import time
import threading
import re
from kivymd.uix.button import MDFillRoundFlatButton

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
            size_hint: None, None
            # color: 1, 0.5, 0.4, 1
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
        
        MyToggleButton:
            id: btn3
            size_hint_y: None
            pos_hint: {'center_x': 0.8, 'center_y': 0.5}
            on_press: root.add()
"""


class CustomGrid(MDGridLayout):
    stop = None
    loop = None

    # function to display Hello World
    def wel(self):
        self.ids.btn3.text = 'Off'
        self.ids.btn3.state = 'down'
        self.ids.txt.font_name = "DS-DIGIB"
        self.ids.txt.font_style = 'H4'
        self.ids.txt.color = 0, 0, 0, 1
        self.ids.txt.text = 'Hello World'
        self.ids.txt.font_name = "DS-DIGIB"

    # show current date
    def date_(self, value):
        now = datetime.now()
        self.ids.bar.title = now.strftime("%Y-%m-%d %H:%M")

    # Schedule execution by using Clock module
    def date(self):
        Clock.schedule_interval(self.date_, 0)

    # add_ function increment automatically after every 5 second
    def add_(self):
        if self.ids.btn3.state == 'normal':
            self.ids.txt.font_style = 'H2'
            self.ids.txt.color = 0.5, 0.3, 0.7, 1
            self.ids.txt.font_name = "DS-DIGIB"
            self.ids.btn3.text = 'On'
            if self.ids.txt.text == 'Hello World':
                self.ids.txt.text = '0'

            elif self.ids.txt.text == '':
                self.ids.txt.text = '0'

            while not self.stop:
                if self.ids.btn3.state == 'down':
                    # self.ids.txt.text = '0'
                    self.stop = True
                    self.ids.btn3.text = 'Off'
                    break
                time.sleep(5)
                if self.check(self.ids.txt.text):
                    self.ids.txt.text = str(int(self.ids.txt.text) + 1)

    # This function executes threading operation
    def add(self):
        if self.ids.btn3.state == 'normal':
            self.stop = False
        thread_add = threading.Thread(target=self.add_, args=())
        thread_add.daemon = True
        thread_add.start()

    def check(self, value):
        """
        args:
        value: str
        return: Boolean, whether the input value is string-numeric or string-text
        """
        v = re.search('[0-9]', value)
        if v is not None:
            return True
        return False


class MyToggleButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light
        self.state = 'down'
        self.text = 'Off'


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    TestApp().run()
