from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class UserScreen(Screen):
    """ TODO set screen for each user"""

    def set_user_info(self, name, email):
        print("dela")
