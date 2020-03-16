from tkinter import *
from tkinter import ttk
from numpy import mean
from random import randint
from tkinter import messagebox
import matplotlib.pyplot as plt


# Creating Die class with rolling ability

class Die:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        outcome = randint(1, self.num_sides)
        if outcome == self.num_sides:
            outcome = outcome + self.roll()
        return outcome


# Defining functions
outcomes_a = []
mean_a = 0

m = 0



def roll_a():
    global mean_a
    if value_check_a():
        outcomes_a.clear()
        for roll_num in range(10000):
            outcome_optional = 0
            for c in range(count_a):
                outcome_optional = Die(int(combobox_list_a[c].get())).roll() + int(
                    entry_list_a[c].get()) + outcome_optional
            outcome = Die(int(combobox_die_a0.get())).roll() + int(entry_modifier_a0.get()) + outcome_optional
            outcomes_a.append(outcome)
        mean_a = mean(outcomes_a)
    else:
        error_modifier()


outcomes_b = []
mean_b = 0


def roll_b():
    global mean_b
    if value_check_b():
        outcomes_b.clear()
        for roll_num in range(10000):
            outcome_optional = 0
            for c in range(count_b):
                outcome_optional = Die(int(combobox_list_b[c].get())).roll() + int(
                    entry_list_b[c].get()) + outcome_optional
            outcome = Die(int(combobox_die_b0.get())).roll() + int(entry_modifier_b0.get()) + outcome_optional
            outcomes_b.append(outcome)
        mean_b = mean(outcomes_b)
    else:
        error_modifier()


def build_histogram():
    plt.title("Average rolls of sets", fontsize=24)
    plt.xlabel("Set", fontsize=14)
    plt.ylabel("Average value", fontsize=14)
    plt.bar([1, 2], [mean_a, mean_b])
    plt.xticks([1, 2], ("Set A", "Set B"))
    plt.show()


def compare():
    roll_a()
    roll_b()
    build_histogram()


def value_check_a():
    for c in range(count_a):
        try:
            int(entry_list_a[c].get())
        except ValueError:
            return 0
    try:
        int(entry_modifier_a0.get())
    except ValueError:
        return 0
    return 1


def value_check_b():
    for c in range(count_b):
        try:
            int(entry_list_b[c].get())
        except ValueError:
            return 0
    try:
        int(entry_modifier_b0.get())
    except ValueError:
        return 0
    return 1


def error_modifier():
    messagebox.showerror("Error!", "Modifiers accept numbers only!")


# Set A - creating and deleting dies function
count_a = 0
combobox_list_a = []
entry_list_a = []
label_list_a = []


def add_die_a():
    global count_a
    global combobox_list_a
    global label_list_a
    global entry_list_a

    combobox_list_a.append(ttk.Combobox(root, width=2, state='readonly'))
    combobox_list_a[count_a]['values'] = (4, 6, 8, 10, 12, 20, 100)
    combobox_list_a[count_a].grid(row=count_a + 3, column=0)

    label_list_a.append(Label(root, text="+"))
    label_list_a[count_a].grid(row=count_a + 3, column=1)

    entry_list_a.append(Entry(root, width=5))
    entry_list_a[count_a].grid(row=count_a + 3, column=2)
    count_a += 1


def remove_die_a():
    global count_a
    global combobox_list_a
    global label_list_a
    global entry_list_a

    if count_a != 0:
        combobox_list_a[count_a - 1].grid_forget()
        label_list_a[count_a - 1].grid_forget()
        entry_list_a[count_a - 1].grid_forget()
        count_a -= 1


# Set B - creating and deleting dies function
count_b = 0
combobox_list_b = []
entry_list_b = []
label_list_b = []


def add_die_b():
    global count_b
    global combobox_list_b
    global label_list_b
    global entry_list_b

    combobox_list_b.append(ttk.Combobox(root, width=2, state='readonly'))
    combobox_list_b[count_b]['values'] = (4, 6, 8, 10, 12, 20, 100)
    combobox_list_b[count_b].grid(row=count_b + 3, column=5)

    label_list_b.append(Label(root, text="+"))
    label_list_b[count_b].grid(row=count_b + 3, column=6)

    entry_list_b.append(Entry(root, width=5))
    entry_list_b[count_b].grid(row=count_b + 3, column=7)
    count_b += 1


def remove_die_b():
    global count_b
    global combobox_list_b
    global label_list_b
    global entry_list_b

    if count_b != 0:
        combobox_list_b[count_b - 1].grid_forget()
        label_list_b[count_b - 1].grid_forget()
        entry_list_b[count_b - 1].grid_forget()
        count_b -= 1


# Rolling Set A 1000 times


# GUI
root = Tk()

# Creating labels
label_first_choice = Label(root, text="Set A")
label_first_choice.grid(row=0, column=1)

label_second_choice = Label(root, text="Set B")
label_second_choice.grid(row=0, column=6)

# Set A - Creating "Add Die" and "Remove Die" buttons
button_remove_a = Button(root, text="-", command=remove_die_a)
button_remove_a.config(width=2, height=1)
button_remove_a.grid(row=0, column=0)

button_add_a = Button(root, text="+", command=add_die_a)
button_add_a.config(width=2, height=1)
button_add_a.grid(row=0, column=2)

# Set B - Creating "Add Die" and "Remove Die" buttons
button_remove_b = Button(root, text="-", command=remove_die_b)
button_remove_b.config(width=2, height=1)
button_remove_b.grid(row=0, column=5)

button_add_b = Button(root, text="+", command=add_die_b)
button_add_b.config(width=2, height=1)
button_add_b.grid(row=0, column=7)

# Default entry for "Set A"
combobox_die_a0 = ttk.Combobox(root, width=2, state='readonly')
combobox_die_a0['values'] = (4, 6, 8, 10, 12, 20, 100)
combobox_die_a0.grid(row=2, column=0)

label_plus_a0 = Label(root, text="+")
label_plus_a0.grid(row=2, column=1)

entry_modifier_a0 = Entry(root, width=5)
entry_modifier_a0.grid(row=2, column=2)

# SPACE
label_space = Label(root, text="               ")
label_space.grid(row=2, column=4)

# Default entry for "Set B"
combobox_die_b0 = ttk.Combobox(root, width=2, state='readonly')
combobox_die_b0['values'] = (4, 6, 8, 10, 12, 20, 100)
combobox_die_b0.grid(row=2, column=5)

label_plus_b0 = Label(root, text="+")
label_plus_b0.grid(row=2, column=6)

entry_modifier_b0 = Entry(root, width=5)
entry_modifier_b0.grid(row=2, column=7)

button_compare = Button(root, text="Compare!", command=compare)
button_compare.grid(row=0, column=4)

root.mainloop()
