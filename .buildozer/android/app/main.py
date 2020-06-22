import random
import re
from kivy.animation import Animation
from math import sin
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics.vertex_instructions import Ellipse, Line
import sqlite3
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ListProperty
from kivy.uix.layout import Layout
from kivy.graphics import Rectangle, Color
import socket

from kivymd.font_definitions import theme_font_styles
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDIconButton, MDFlatButton, MDRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem, ThreeLineIconListItem, ThreeLineListItem, \
    IRightBodyTouch, OneLineAvatarIconListItem, ThreeLineRightIconListItem
from kivy.core.window import Window
from kivymd.uix.selectioncontrol import MDCheckbox

__version__ = "1.0.3"
"""SCREEN IMPORTS"""
from screens.screenone import ScreenOne
from screens.screentwo import ScreenTwo
from screens.LoginScreen import LoginScreen
from screens.RegisterScreen import RegisterScreen
from screens.MainScreen import MainScreen
from screens.screenthree import ScreenThree
from screens.UserScreen import UserScreen

"""Set screen size for tablet"""
Window.size = (800, 1280)

""" Main framework of the application START"""


class Controller(BoxLayout):

    def btn(self):
        host = '127.0.0.1'  # The server's hostname or IP address
        port = 8888  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(self.message.text.encode())
            data = s.recv(1024)

        print('Received', repr(data))
        self.message.text = "You pressed the button!"

    def update_sequence(self):
        self.root.ids.screen_one_sequence.text = "Dela"
        self.screen_one_sequence.text = "dela"


""" Main framework of the application END"""

"""SIDE MENU FRAMEWORK"""


class ContentNavigationDrawer(BoxLayout):
    user_name = ObjectProperty()

    def navigate_to_user_screen(self):
        self.parent.set_state("close")
        MDApp.get_running_app().navigate_to_user_screen(self.user_name.text, "test")


"""SIDE MENU FRAMEWORK"""


class LoginLayout(BoxLayout):
    pass


class WindowManager(ScreenManager):
    pass


"""CLIMBING GRID FRAMEWORK"""


class ClimbingGrid(GridLayout):
    all_hold_coordinates = []  # array holding all hold coordinates
    last_hold_coordinates = []  # array for storing last selected hold coordinates ( for drawing lines on the wall)
    line_objects = []  # array of drawings - Lines between holds

    """ Draw single line on canvas"""

    def draw_line(self, next_hold_coordinates):
        group_of_lines = InstructionGroup()
        group_of_lines.add(Line(width=2., points=(
            self.last_hold_coordinates[0], self.last_hold_coordinates[1],
            next_hold_coordinates[0], next_hold_coordinates[1])))
        self.line_objects.append(group_of_lines)
        self.canvas.add(group_of_lines)

    """ remove all lines from canvas"""

    def remove_lines(self):
        for line in self.line_objects:
            self.canvas.remove(line)
        self.line_objects = []

    """ remove single line from canvas"""

    def remove_line_single(self):
        if len(self.line_objects) > 0:
            self.canvas.remove(self.line_objects[len(self.line_objects) - 1])
            self.line_objects.pop()
            self.all_hold_coordinates.pop()
            self.last_hold_coordinates = self.all_hold_coordinates[len(self.all_hold_coordinates) - 1]


"""CLIMBING GRID FRAMEWORK"""

"""ALERT MESSAGE FRAMEWORK"""


class AlertMessage(ModalView):
    alert_message = ObjectProperty()

    def __init__(self, alert_message_content, **kwargs):
        super(AlertMessage, self).__init__(**kwargs)
        self.alert_message.text = alert_message_content


"""ALERT MESSAGE FRAMEWORK"""

"""POPUP FRAMEWORK"""


class AddProblemPopUp(Popup):
    sequence_label = ObjectProperty()
    problem_name = ObjectProperty()
    setter_name = ObjectProperty()
    comment = ObjectProperty()
    sequence = StringProperty()
    grade = ObjectProperty()

    def __init__(self, sequence, **kwargs):
        super(AddProblemPopUp, self).__init__(**kwargs)
        self.sequence = sequence

    def close(self):

        if self.problem_name.text == "" or self.sequence_label.text == "" or self.setter_name.text == "" or "Add" in self.sequence_label.text or self.grade.text == "Select problem grade":
            print("napaka")
        else:
            self.dismiss()
            conn = sqlite3.connect('problems.db')
            c = conn.cursor()
            c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
                  VALUES (?, ?, ?, ?, ?)",
                      (self.problem_name.text, self.grade.text, self.sequence_label.text, self.setter_name.text,
                       self.comment.text))
            conn.commit()
            MDApp.get_running_app().problem_list_add_problem(
                [self.problem_name.text, self.grade.text,
                 self.sequence_label.text,
                 self.setter_name.text,
                 self.comment.text])


"""POPUP FRAMEWORK"""

""" Single climbing hold layout START"""


class HoldLayout(AnchorLayout):
    id = StringProperty()
    color_state = False
    objects = []
    button_objects = []
    first_point_of_line = []

    """FUNCTION FOR DRAWING ELLIPSE AROUND CLICKED CLIMBING HOLD"""

    def clicked(self):
        group_of_drawings = InstructionGroup()

        if self.id not in self.button_objects:
            self.button_objects.append(self.id)
        if not self.color_state:
            """Call ScreenOne and update the sequence"""
            self.parent.parent.update_sequence(self.id)
            """Call ScreenOne and update the sequence"""
            self.color_state = True
            if "11" in self.id:
                group_of_drawings.add(Color(rgba=(255, 0, 0, 1)))
            elif "1" in self.id and "0" not in self.id:
                group_of_drawings.add(Color(rgba=(0, 255, 0, 1)))
            else:
                group_of_drawings.add(Color(rgba=(0, 0, 255, 1)))
            group_of_drawings.add(Line(width=2., ellipse=(self.x + 5, self.y + 5, self.width - 10, self.height - 10)))

            if len(self.objects) == 0:
                self.parent.last_hold_coordinates = [self.x + 5 + (self.width - 10) / 2,
                                                     self.y + 5 + (self.height - 10) / 2]
            else:
                self.parent.draw_line([self.x + 5 + (self.width - 10) / 2, self.y + 5 + (self.height - 10) / 2])
                self.parent.last_hold_coordinates = [self.x + 5 + (self.width - 10) / 2,
                                                     self.y + 5 + (self.height - 10) / 2]
            self.objects.append(group_of_drawings)
            self.canvas.add(group_of_drawings)
            self.parent.all_hold_coordinates.append(
                [self.x + 5 + (self.width - 10) / 2, self.y + 5 + (self.height - 10) / 2])
        else:
            """ Remove selected ellipse"""
            index = self.button_objects.index(self.id)
            self.color_state = False
            self.canvas.remove(self.objects[index])
            self.objects.pop(index)
            self.button_objects.pop(index)
            """ Remove the last added element in sequence """
            self.parent.parent.delete_sequence()
            """ Remove last drawn line """
            self.parent.remove_line_single()

    """ completely reset climbing grid"""

    def reset_wall(self):
        MDApp.get_running_app().reset_wall(self.button_objects, self.objects)  # call the MainApp function to reset_wall


""" Single climbing hold layout END"""

""" SIDE MENU START """


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):

    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        if instance_item.text == "Add New Problem":
            self.parent.parent.parent.set_state("close")
            popup = AddProblemPopUp(MDApp.get_running_app().root.ids.screen_one_sequence.text)
            popup.open()
        elif instance_item.text == "Reset Wall":
            print(self.parent.parent.parent)
            self.parent.parent.parent.set_state("close")
            MDApp.get_running_app().root.ids.screen_one_sequence.text = "Add sequence by clicking on the holds!"
            MDApp.get_running_app().root.ids.screen_one_problem_name.text = "No problem has been loaded yet"
            MDApp.get_running_app().hold_container.reset_wall()  # call TestLayout
        elif instance_item.text == "Load Problem":
            self.parent.parent.parent.set_state("close")
            all_entries = len(MDApp.get_running_app().root.ids.problem_list.children)
            num1 = random.randint(0, all_entries - 1)
            MDApp.get_running_app().root.ids.screen_one_sequence.text = "Add sequence by clicking on the holds!"
            MDApp.get_running_app().root.ids.screen_one_problem_name.text = \
                MDApp.get_running_app().root.ids.problem_list.children[num1].name
            MDApp.get_running_app().hold_container.reset_wall()  # call TestLayout
            MDApp.get_running_app().load_problem(
                MDApp.get_running_app().root.ids.problem_list.children[num1].sequence)  # call TestLayout
        elif instance_item.text == "Sign Out":
            self.parent.parent.parent.set_state("close")
            MDApp.get_running_app().change_window("login_window", "right")


""" SIDE MENU END """

""" DATABASE LIST START """


class Container(IRightBodyTouch, BoxLayout):
    adaptive_width = True


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    """Custom right container."""


class Problem(ThreeLineRightIconListItem):
    sequence = StringProperty()
    name = StringProperty()

    def __init__(self, **kwargs):
        super(Problem, self).__init__(**kwargs)


class ProblemList(ThemableBehavior, MDList):

    def select_problem(self, instance_item):
        """Called when tap on a menu item. """
        MDApp.get_running_app().root.ids.screen_one_sequence.text = "Add sequence by clicking on the holds!"
        MDApp.get_running_app().root.ids.screen_one_problem_name.text = instance_item.name
        MDApp.get_running_app().hold_container.reset_wall()  # call TestLayout
        MDApp.get_running_app().load_problem(instance_item.sequence)  # call TestLayout

    def add_problem_to_personal_list(self, instance_item):
        print(instance_item)


""" DATABASE LIST END """


class MainApp(MDApp):
    """
    # CREATE TABLE IN DATABASE
    conn = sqlite3.connect('problems.db')
    conn.execute('''CREATE TABLE PROBLEMS
             (
             NAME           TEXT     NOT NULL,
             GRADE          TEXT     NOT NULL,
             SEQUENCE       TEXT     NOT NULL,
             SETTER         TEXT     NOT NULL,
             COMMENT        TEXT     NOT NULL
             );''')
    conn.close()
    """
    hold_container = HoldLayout()  # used for calling class HoldLayout()
    climbing_grid = ClimbingGrid()  # used for calling class ClimbingGrid()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # to check if EMAIL is valid

    def __init__(self, **kwargs):
        self.title = "WayUp"
        self.users = sqlite3.connect('users.db')
        self.problems = sqlite3.connect('problems.db')
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "Red"
        LabelBase.register(
            name="JetBrainsMono",
            fn_regular="JetBrainsMono-Regular.ttf")
        theme_font_styles.append('JetBrainsMono')
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]
        return Controller()

    def on_start(self):
        self.animate_background()
        self.animate_card()
        counter = 0

        wall_user_options = {
            "checkerboard-plus": "Add New Problem",
            "cloud-download-outline": "Load Problem",
            "engine-outline": "Generate Problem",
            "new-box": "Reset Wall",
            "home-lightbulb": "Show Problem",

        }

        wall_ids = {
            1: "A11", 2: "B11", 3: "C11", 4: "D11", 5: "E11", 6: "F11", 7: "G11", 8: "H11", 9: "I11", 10: "J11",
            11: "K11",
            13: "A10", 14: "B10", 15: "C10", 16: "D10", 17: "E10", 18: "F10", 19: "G10", 20: "H10", 21: "I10",
            22: "J10", 23: "K10",
            25: "A9", 26: "B9", 27: "C9", 28: "D9", 29: "E9", 30: "F9", 31: "G9", 32: "H9", 33: "I9", 34: "J9",
            35: "K9",
            37: "A8", 38: "B8", 39: "C8", 40: "D8", 41: "E8", 42: "F8", 43: "G8", 44: "H8", 45: "I8", 46: "J8",
            47: "K8",
            49: "A7", 50: "B7", 51: "C7", 52: "D7", 53: "E7", 54: "F7", 55: "G7", 56: "H7", 57: "I7", 58: "J7",
            59: "K7",
            61: "A6", 62: "B6", 63: "C6", 64: "D6", 65: "E6", 66: "F6", 67: "G6", 68: "H6", 69: "I6", 70: "J6",
            71: "K6",
            73: "A5", 74: "B5", 75: "C5", 76: "D5", 77: "E5", 78: "F5", 79: "G5", 80: "H5", 81: "I5", 82: "J5",
            83: "K5",
            85: "A4", 86: "B4", 87: "C4", 88: "D4", 89: "E4", 90: "F4", 91: "G4", 92: "H4", 93: "I4", 94: "J4",
            95: "K4",
            97: "A3", 98: "B3", 99: "C3", 100: "D3", 101: "E3", 102: "F3", 103: "G3", 104: "H3", 105: "I3", 106: "J3",
            107: "K3",
            109: "A2", 110: "B2", 111: "C2", 112: "D2", 113: "E2", 114: "F2", 115: "G2", 116: "H2", 117: "I2",
            118: "J2", 119: "K2",
            121: "A1", 122: "B1", 123: "C1", 124: "D1", 125: "E1", 126: "F1", 127: "G1", 128: "H1", 129: "I1",
            130: "J1", 131: "K1",
        }

        """ Fill Side Menu with items START"""
        for icon_name in wall_user_options.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=wall_user_options[icon_name])
            )
            """ serves as a seperator for two itemdrawers"""
        self.root.ids.content_drawer.ids.md_list.add_widget(
            OneLineListItem(text="")
        )
        """ Adds logout option in the drawer menu"""
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon="logout", text="Sign Out")
        )

        """ Fill Side Menu with items END"""

        """ Fill ClimbingGrid with holds START"""

        for i in range(0, 132):
            if i % 12 == 0 or i == 0:
                self.root.ids.wall_system.add_widget(
                    MDLabel(text=str(11 - counter), halign="center", size_hint_x=None, width=25,
                            theme_text_color="Custom",
                            text_color=(1, 1, 1, 1), font_style="H6", font_name="JetBrainsMono")
                )
                counter = counter + 1
            else:
                self.root.ids.wall_system.add_widget(
                    HoldLayout(id=wall_ids[i])
                )

        """Draw GRAPH"""

        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=25, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        self.root.ids.screen_three.add_widget(graph)
        self.initiate_problem_list()
        """ Fill ClimbingGrid with holds END"""

    def reset_wall(self, temp_button_objects, temp_objects):

        for obj in self.root.ids.wall_system.children:
            if isinstance(obj, HoldLayout) and obj.id in temp_button_objects:
                """CLEAR CANVAS OF SELECTED HOLDS"""
                index = temp_button_objects.index(obj.id)
                obj.canvas.remove(temp_objects[index])

                """RESET THE HOLD ARRAYS AND COLOR STATE"""
                obj.button_objects.remove(obj.id)
                obj.objects.remove(temp_objects[index])
                obj.color_state = False

        self.root.ids.wall_system.remove_lines()  # Call ClimbingGrid()

    """Fill Scrollview with problems from data on_start"""

    def initiate_problem_list(self):
        """ Fill Database_list with problems START"""

        dataset = []
        c = self.problems.cursor()
        """
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('Test1', '6a', 'A1, A2, A3, B4, B8', 'Anze', '/')")
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('Test2', '7a', 'B1, B5, A10, C9', 'Anze', '/')")
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('Test3', '8a', 'D1, G4, C5, A11', 'Anze', '/')")
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('Anze', '8a', 'D1, G4, C5, A11', 'Anze', '/')")
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('12355', '8a', 'D1, G4, C5, A11', 'Anze', '/')")
        c.execute("INSERT INTO PROBLEMS (NAME,GRADE,SEQUENCE,SETTER,COMMENT) \
              VALUES ('ales12', '8a', 'D1, G4, C5, A11', 'Anze', '/')")
        connection.commit()
        """
        for row in c.execute('SELECT * FROM problems ORDER BY NAME COLLATE NOCASE'):
            new_problem = Problem(sequence=row[2], name=row[0] + " - " + row[1])
            new_problem.text = row[0] + " - " + row[1]
            new_problem.secondary_text = "Setter: " + row[3]
            new_problem.tertiary_text = "Comment: " + row[4]

            self.root.ids.problem_list.add_widget(
                new_problem
            )

        self.problems.close()

        """ Fill Database_list with problems END"""

    """Update ScrollView with the last added problem - called by AddProblem"""

    def problem_list_add_problem(self, problem_data):

        new_problem = Problem(sequence=problem_data[2], name=problem_data[0] + " - " + problem_data[1])
        new_problem.text = problem_data[0] + " - " + problem_data[1]
        new_problem.secondary_text = "Setter: " + problem_data[3]
        new_problem.tertiary_text = "Comment: " + problem_data[4]

        self.root.ids.problem_list.add_widget(
            new_problem
        )

        self.problems.close()

    def filter_problem_list(self, problem_data):
        self.root.ids.problem_list.clear_widgets()
        for entry in problem_data:
            new_problem = Problem(sequence=entry[2], name=entry[0] + " - " + entry[1])
            new_problem.text = entry[0] + " - " + entry[1]
            new_problem.secondary_text = "Setter: " + entry[3]
            new_problem.tertiary_text = "Comment: " + entry[4]

            self.root.ids.problem_list.add_widget(
                new_problem
            )
        print("Problem list successfully updated!")

    def load_problem(self, sequence):
        sequence_array = sequence.split(", ")
        for obj in self.root.ids.wall_system.children:
            if isinstance(obj, HoldLayout) and obj.id in sequence_array:
                obj.clicked()

    """ LOGIN SCREEN ANIMATIONS START"""

    def animate_card(self):
        anim = Animation(pos_hint={"center_y": 0.6}, duration=2.)
        anim.start(self.root.ids.window_manager.get_screen("login_window").ids.login_card)

    def animate_background(self):
        anim = Animation(size_hint_y=0.6, duration=2.)
        anim.start(self.root.ids.window_manager.get_screen("login_window").ids.login_background)

    """ LOGIN SCREEN ANIMATIONS END"""

    """ REGISTER SCREEN ANIMATIONS START"""

    def animate_register_background(self):
        anim = Animation(size_hint_x=0.7, duration=2.)
        anim.start(self.root.ids.window_manager.get_screen("register_window").ids.register_background)

    def animate_register_card(self):
        anim = Animation(pos_hint={"center_x": 0.5}, duration=2.)
        anim.start(self.root.ids.window_manager.get_screen("register_window").ids.register_card)

    """ REGISTER SCREEN ANIMATIONS START"""

    def change_window(self, new_window, direction):
        self.root.ids.window_manager.transition.direction = direction
        self.root.ids.window_manager.current = new_window

    def sign_in(self, instance_item):
        c = self.users.cursor()
        if instance_item.parent.ids.email.text == "" and instance_item.parent.ids.password.text == "":
            self.change_window("main_window", "left")
        """ PRAVI DEL KODE (ŽE DELUJOČ), ZGORNJI DEL JE LE ZA TESTIRANJE
        for row in c.execute('SELECT * FROM USERS'):
            if row[1] == instance_item.parent.ids.email.text and row[2] == instance_item.parent.ids.password.text:
               self.change_window("main_window", "right")
        """

    def sign_up(self, name, email, password):
        c = self.users.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='USERS'")

        if c.fetchone()[0] == 1:
            print('Table exists.')

            c.execute("INSERT INTO USERS (NAME,EMAIL,PASSWORD) \
                  VALUES (?, ?, ?)",
                      (name, email,
                       password))
            self.change_window("login_window", "right")
        else:
            c.execute('''CREATE TABLE USERS
                     (
                     NAME           TEXT     NOT NULL,
                     EMAIL         TEXT     NOT NULL,
                     PASSWORD     TEXT     NOT NULL
                     );''')

            c.execute("INSERT INTO USERS (NAME,EMAIL,PASSWORD) \
                  VALUES (?, ?, ?)",
                      (name, email,
                       password))

            self.change_window("login_window", "right")
        self.users.commit()
        print("New user added!")

    def show_user_alert(self, content):

        dialog = AlertMessage(content)
        dialog.open()
        # anim = Animation(size=(500, 50))

        # Clock.schedule_once(lambda d: anim.start(dialog), 1)

    def check_email(self, instance_textfield):

        if re.search(self.regex, instance_textfield.text):
            instance_textfield.error = False

        else:
            instance_textfield.error = True
            instance_textfield.helper_text = "You need to enter a valid email. e.g. anze.peharc@gmail.com"

    def check_password(self, instance_textfield):

        if len(instance_textfield.text) < 6:
            instance_textfield.error = True
            instance_textfield.helper_text = "Password length should be at least 6 characters"

        elif not any(char.isdigit() for char in instance_textfield.text):
            instance_textfield.error = True
            instance_textfield.helper_text = "Password should have at least one numeral"

        else:
            instance_textfield.error = False

    def navigate_to_user_screen(self, name, email):
        self.change_window("user_window", "left")
        self.root.ids.window_manager.get_screen("user_window").set_user_info(name, email)


MainApp().run()
