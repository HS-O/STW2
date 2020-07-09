import kivy
import names
import kivymd
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle
from kivy.graphics.instructions import Canvas
from kivy.uix.scrollview import ScrollView
from kivymd.list import BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.theming import ThemeManager
from kivy.core.window import Window

Builder.load_file("new.kv")


class MainWindow(Screen):
    pass


class ProfileWindow(Screen):
    pass


class LogIn(Screen):
    ema = ObjectProperty(None)
    pw = ObjectProperty(None)


class RegisterWindow(Screen):
    ema = ObjectProperty(None)
    pw = ObjectProperty(None)
    def username(self):
        user = names.get_full_name()
        print("your username:" + user)


class PostingWindow(Screen):
    def _init_(self, **kwargs):
        super(PostScreen, self)._init_(**kwargs)


class PostScreen(Screen):
    pass

class Setting(Screen):
    pass



sm = ScreenManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(ProfileWindow(name='profile'))
sm.add_widget(LogIn(name='login'))
sm.add_widget(RegisterWindow(name='register'))
sm.add_widget(PostingWindow(name='post'))
sm.add_widget(Setting(name='settings'))


class NewApp(App):
    def build(self):
        return sm



if __name__ == "__main__":
    NewApp().run()
