from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


class ScreenOne(BoxLayout):
    screen_one_sequence = ObjectProperty()

    """ update problem sequence text"""

    def update_sequence(self, value):
        """Check if user has not clicked on the wall yet. This is to make sure that the popup does not contain default
        wall sequence text"""
        if "Add" in self.screen_one_sequence.text or self.screen_one_sequence.text == "":
            self.screen_one_sequence.text = value
        else:
            self.screen_one_sequence.text = self.screen_one_sequence.text + ", " + value

    """ delete last added hold from sequence text"""

    def delete_sequence(self):
        sequence_to_array = self.screen_one_sequence.text.split(',')
        sequence_to_array.pop()

        self.screen_one_sequence.text = ",".join(sequence_to_array)
        if self.screen_one_sequence.text == "":
            self.screen_one_sequence.text = "Add sequence by clicking on the holds!"
