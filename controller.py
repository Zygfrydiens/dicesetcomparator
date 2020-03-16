from view import *
from model import *
from tkinter import *
from pubsub import pub


class Controller:
    def __init__(self, parent):
        self.parent = parent
        # self.model = Model()
        self.view = View(parent)
        self.view.setup()

        pub.subscribe(self.add_a_button_pressed, "Add a button pressed")
        pub.subscribe(self.add_b_button_pressed, "Add b button pressed")
        pub.subscribe(self.remove_a_button_pressed, "Remove a button pressed")
        pub.subscribe(self.remove_b_button_pressed, "Remove b button pressed")
        pub.subscribe(self.compare_button_pressed, "Compare button pressed")

    def add_a_button_pressed(self):
        print("controller - add a button pressed")
        self.view.add_die(self.view.count_a, self.view.combobox_list_a, self.view.label_list_a, self.view.entry_list_a,
                          self.view.root, 0)
        # self.view.count_a += 1
        # I have no idea why it works without that line

    def add_b_button_pressed(self):
        print("controller - add b button pressed")
        self.view.add_die(self.view.count_b, self.view.combobox_list_b, self.view.label_list_b, self.view.entry_list_b,
                          self.view.root, 5)
        self.view.count_b += 1 # I have no idea why it needs this line, when adding to set A works just fine


    def remove_a_button_pressed(self):
        print("controller - remove a button pressed")
        if self.view.count_a != 0: # I have no idea why this line has to be here not in function remove_die
            self.view.remove_die(self.view.count_a, self.view.combobox_list_a,
                                 self.view.label_list_a, self.view.entry_list_a)
            self.view.count_a -= 1 # I have no idea why this line has to be here not in function remove_die


    def remove_b_button_pressed(self):
        print("controller - remove a button pressed")
        if self.view.count_a != 0: # I have no idea why this line has to be here not in function remove_die
            self.view.remove_die(self.view.count_b, self.view.combobox_list_b,
                                 self.view.label_list_b, self.view.entry_list_b)
            self.view.count_b -= 1 # I have no idea why this line has to be here not in function remove_die


    def compare_button_pressed(self):
        print("controller - compare button pressed")


if __name__ == "__main__":
    root = Tk()
    app = Controller(root)
    root.mainloop()