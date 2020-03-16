from tkinter import *
from tkinter import ttk
from pubsub import *

class View:
    def __init__(self, parent):
        self.root = parent
        # Lists for addit to Set A
        self.count_a = 0
        self.combobox_list_a = []
        self.label_list_a = []
        self.entry_list_a = []
        # Lists for adding to Set B
        self.count_b = 0
        self.combobox_list_b = []
        self.label_list_b = []
        self.entry_list_b = []
        return

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # Set A
        self.label_set_a = Label(self.root, text="Set A")
        self.button_remove_a = Button(self.root, text="-", command=self.remove_die_a)
        self.button_remove_a.config(width=2, height=1)
        self.button_add_a = Button(self.root, text="+", command=self.add_die_a)
        self.button_add_a.config(width=2, height=1)
        self.combobox_die_a0 = ttk.Combobox(self.root, width=2, state='readonly')
        self.combobox_die_a0['values'] = (4, 6, 8, 10, 12, 20, 100)
        self.label_plus_a0 = Label(self.root, text="+")
        self.entry_modifier_a0 = Entry(self.root, width=5)

        # Space between sets
        self.label_space = Label(self.root, text="               ")

        # Set B
        self.label_set_b = Label(self.root, text="Set B")
        self.button_remove_b = Button(self.root, text="-", command=self.remove_die_b)
        self.button_remove_b.config(width=2, height=1)
        self.button_add_b = Button(self.root, text="+", command=self.add_die_b)
        self.button_add_b.config(width=2, height=1)
        self.label_plus_b0 = Label(self.root, text="+")
        self.combobox_die_b0 = ttk.Combobox(self.root, width=2, state='readonly')
        self.combobox_die_b0['values'] = (4, 6, 8, 10, 12, 20, 100)
        self.entry_modifier_b0 = Entry(self.root, width=5)

        # Compare button
        self.button_compare = Button(self.root, text="Compare!", command=self.compare)

    def setup_layout(self):
        # Set A
        self.label_set_a.grid(row=0, column=1)
        self.button_remove_a.grid(row=0, column=0)
        self.button_add_a.grid(row=0, column=2)
        self.combobox_die_a0.grid(row=2, column=0)
        self.label_plus_a0.grid(row=2, column=1)
        self.entry_modifier_a0.grid(row=2, column=2)

        #Space between sets
        self.label_space.grid(row=2, column=4)

        # Set B
        self.label_set_b.grid(row=0, column=6)
        self.button_remove_b.grid(row=0, column=5)
        self.button_add_b.grid(row=0, column=7)
        self.combobox_die_b0.grid(row=2, column=5)
        self.label_plus_b0.grid(row=2, column=6)
        self.entry_modifier_b0.grid(row=2, column=7)

        # Compare button
        self.button_compare.grid(row=0, column=4)

    def add_die(self, count, combobox_list, label_list, entry_list, root, combobox_column):
        print(count)
        combobox_list.append(ttk.Combobox(root, width=2, state='readonly'))
        combobox_list[count]['values'] = (4, 6, 8, 10, 12, 20, 100)
        combobox_list[count].grid(row=count + 3, column=combobox_column)

        label_list.append(Label(root, text="+"))
        label_list[count].grid(row=count + 3, column=combobox_column + 1)

        entry_list.append(Entry(root, width=5))
        entry_list[count].grid(row=count + 3, column=combobox_column + 2)
        count += 1

    def remove_die(self, count, combobox_list, label_list, entry_list):
        if count != 0:
            combobox_list[count - 1].grid_forget()
            label_list[count - 1].grid_forget()
            entry_list[count - 1].grid_forget()
            count -= 1

    def remove_die_a(self):
        print("remove a")
        pub.sendMessage("Remove a button pressed")
        # if self.count_a != 0:
        #     self.combobox_list_a[self.count_a - 1].grid_forget()
        #     self.label_list_a[self.count_a - 1].grid_forget()
        #     self.entry_list_a[self.count_a - 1].grid_forget()
        #     self.count_a -= 1

    def add_die_a(self):
        print("add a")
        pub.sendMessage("Add a button pressed")
        # self.combobox_list_a.append(ttk.Combobox(root, width=2, state='readonly'))
        # self.combobox_list_a[self.count_a]['values'] = (4, 6, 8, 10, 12, 20, 100)
        # self.combobox_list_a[self.count_a].grid(row=self.count_a + 3, column=0)
        #
        # self.label_list_a.append(Label(self.root, text="+"))
        # self.label_list_a[self.count_a].grid(row=self.count_a + 3, column=1)
        #
        # self.entry_list_a.append(Entry(self.root, width=5))
        # self.entry_list_a[self.count_a].grid(row=self.count_a + 3, column=2)
        self.count_a += 1

    def remove_die_b(self):
        print("remove b")
        pub.sendMessage("Remove b button pressed")
        # if self.count_b != 0:
        #     self.combobox_list_b[self.count_b - 1].grid_forget()
        #     self.label_list_b[self.count_b - 1].grid_forget()
        #     self.entry_list_b[self.count_b - 1].grid_forget()
        #     self.count_b -= 1

    def add_die_b(self):
        print("add b")
        pub.sendMessage("Add b button pressed")
        # self.combobox_list_b.append(ttk.Combobox(root, width=2, state='readonly'))
        # self.combobox_list_b[self.count_b]['values'] = (4, 6, 8, 10, 12, 20, 100)
        # self.combobox_list_b[self.count_b].grid(row=self.count_b + 3, column=5)
        #
        # self.label_list_b.append(Label(self.root, text="+"))
        # self.label_list_b[self.count_b].grid(row=self.count_b + 3, column=6)
        #
        # self.entry_list_b.append(Entry(self.root, width=5))
        # self.entry_list_b[self.count_b].grid(row=self.count_b + 3, column=7)
        # self.count_b += 1

    def compare(self):
        print("comparing")
        pub.sendMessage("Compare button pressed")

#testing
if __name__ == "__main__":
    print("running view")
    root = Tk()
    view = View(root)
    view.setup()
    root.mainloop()


