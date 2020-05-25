from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class RegisterScreen(Screen):
    new_user_name = ObjectProperty()
    new_user_email = ObjectProperty()
    new_user_password = ObjectProperty()

    def check_credentials(self):
        name = self.new_user_name.text
        email = self.new_user_email.text
        password = self.new_user_password.text
        if name == "" or email == "" or password == "":
            MDApp.get_running_app().show_user_alert("All fields must be filled out.")
        else:
            MDApp.get_running_app().sign_up(name, email, password)
