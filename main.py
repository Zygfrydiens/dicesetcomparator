from tkinter import *
from tkinter import ttk
from numpy import mean
from random import randint
from tkinter import messagebox
import matplotlib.pyplot as plt
import pygal

#Creating Die class with rolling ability
class Die():
    def __init__(self, num_sides):
        self.num_sides =  num_sides

    def roll(self):
        outcome = randint(1, self.num_sides)
        if outcome == self.num_sides:
            outcome = outcome + self.roll()
        return outcome

def valuecheckA():
    for c in range(countA):
        try:
            is_num = int(entry_listA[c].get())
        except ValueError:
            return 0
    try:
        is_num = int(entry_modifierA0.get())
    except ValueError:
        return 0
    return 1

def valuecheckB():
    for c in range(countB):
        try:
            is_num = int(entry_listB[c].get())
        except ValueError:
            return 0
    try:
        is_num = int(entry_modifierB0.get())
    except ValueError:
        return 0
    return 1

def valueerror():
    messagebox.showerror("Error!", "Modifiers accept numbers only!")

def buildhistogramA():
    plt.plot(outcomesA)
    plt.show()

def buildhistogramB():
    plt.plot(outcomesB)
    plt.show()

def buildhistogram_compare():
    plt.title("Average rolls of sets", fontsize=24)
    plt.xlabel("Set", fontsize=14)
    plt.ylabel("Average value", fontsize=14)
    plt.bar([1, 2], [meanA, meanB] )
    plt.xticks([1, 2], ("Set A", "Set B"))
    plt.show()

outcomesA = []

def rollA():
    global meanA
    if valuecheckA():
        outcomesA.clear()
        for roll_num in range(10000):
            outcome_optional = 0
            for c in range(countA):
                outcome_optional = Die(int(combobox_listA[c].get())).roll() + int(entry_listA[c].get()) + outcome_optional
            outcome = Die(int(combobox_dieA0.get())).roll() + int(entry_modifierA0.get()) + outcome_optional
            outcomesA.append(outcome)
        meanA = mean(outcomesA)
    else:
        valueerror()

outcomesB = []
def rollB():
    global meanB
    if valuecheckB():
        outcomesB.clear()
        for roll_num in range(10000):
            outcome_optional = 0
            for c in range(countB):
                outcome_optional = Die(int(combobox_listB[c].get())).roll() + int(entry_listB[c].get()) + outcome_optional
            outcome = Die(int(combobox_dieB0.get())).roll() + int(entry_modifierB0.get()) + outcome_optional
            outcomesB.append(outcome)
        meanB = mean(outcomesB)
    else:
        valueerror()

def compare():
    rollA()
    rollB()
    buildhistogram_compare()


#Set A - creating and deleting dies function
countA = 0
combobox_listA = []
entry_listA = []
label_listA = []
def addDieA():
    global countA
    global combobox_listA
    global label_listA
    global entry_listA

    combobox_listA.append(ttk.Combobox(root, width=2, state='readonly'))
    combobox_listA[countA]['values'] = (4, 6, 8, 10, 12, 20, 100)
    combobox_listA[countA].grid(row=countA+3, column=0)

    label_listA.append(Label(root, text="+"))
    label_listA[countA].grid(row=countA+3, column=1)

    entry_listA.append(Entry(root, width=5))
    entry_listA[countA].grid(row=countA+3, column=2)
    countA += 1

def removeDieA():
    global countA
    global combobox_listA
    global label_listA
    global entry_listA

    if countA != 0:
        combobox_listA[countA-1].grid_forget()
        combobox_listA.pop
        label_listA[countA-1].grid_forget()
        label_listA.pop
        entry_listA[countA-1].grid_forget()
        entry_listA.pop

        countA -= 1

#Set B - creating and deleting dies function
countB = 0
combobox_listB = []
entry_listB = []
label_listB = []
def addDieB():
    global countB
    global combobox_listB
    global label_listB
    global entry_listB

    combobox_listB.append(ttk.Combobox(root, width=2, state='readonly'))
    combobox_listB[countB]['values'] = (4, 6, 8, 10, 12, 20, 100)
    combobox_listB[countB].grid(row=countB+3, column=5)

    label_listB.append(Label(root, text="+"))
    label_listB[countB].grid(row=countB+3, column=6)

    entry_listB.append(Entry(root, width=5))
    entry_listB[countB].grid(row=countB+3, column=7)
    countB += 1

def removeDieB():
    global countB
    global combobox_listB
    global label_listB
    global entry_listB

    if countB != 0:
        combobox_listB[countB-1].grid_forget()
        combobox_listB.pop
        label_listB[countB-1].grid_forget()
        label_listB.pop
        entry_listB[countB-1].grid_forget()
        entry_listB.pop

        countB -= 1

#Rolling Set A 1000 times


#GUI
root = Tk()



#Creating labels
label_firstchoice = Label(root, text="Set A")
label_firstchoice.grid(row=0, column=1)

label_secondchoice = Label(root, text="Set B")
label_secondchoice.grid(row=0, column=6)

#Set A - Creating "Add Die" and "Remove Die" buttons
button_removeA = Button(root, text="-", command=removeDieA)
button_removeA.config(width=2, height=1)
button_removeA.grid(row=0, column=0)

button_addA = Button(root, text="+", command=addDieA)
button_addA.config(width=2, height=1)
button_addA.grid(row=0, column=2)

#Set B - Creating "Add Die" and "Remove Die" buttons
button_removeB = Button(root, text="-", command=removeDieB)
button_removeB.config(width=2, height=1)
button_removeB.grid(row=0, column=5)

button_addB = Button(root, text="+", command=addDieB)
button_addB.config(width=2, height=1)
button_addB.grid(row=0, column=7)


#Default entry for "Set A"
combobox_dieA0 = ttk.Combobox(root, width=2, state='readonly')
combobox_dieA0['values'] = (4, 6, 8, 10, 12, 20, 100)
combobox_dieA0.grid(row=2, column=0)

label_plusA0 = Label(root, text="+")
label_plusA0.grid(row=2, column=1)

entry_modifierA0 = Entry(root, width=5)
entry_modifierA0.grid(row=2, column=2)

# SPACE
label_space = Label(root, text="               ")
label_space.grid(row=2, column=4)

#Default entry for "Set B"
combobox_dieB0 = ttk.Combobox(root, width=2, state='readonly')
combobox_dieB0['values'] = (4, 6, 8, 10, 12, 20, 100)
combobox_dieB0.grid(row=2, column=5)

label_plusB0 = Label(root, text="+")
label_plusB0.grid(row=2, column=6)

entry_modifierB0 = Entry(root, width=5)
entry_modifierB0.grid(row=2, column=7)

button_compare = Button(root, text= "Compare!", command=compare)
button_compare.grid(row=0, column=4)


root.mainloop()