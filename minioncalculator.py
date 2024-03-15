from tkinter import *

mainWindow = Tk()
mainWindow.title("Slave Profits Calculator")

title = Label(mainWindow, text="Slave Profits Calculator")
title.pack(side = TOP)

# Add a grid
mainframe = Frame(mainWindow)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create Tkinter variables
tkvar = StringVar(mainWindow)
tkvar2 = StringVar(mainWindow)

# Dictionary with options
choices = { 'Clay','Redstone','Tarantula','Red Sand','Mycellium'}
tkvar.set('Clay') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a minion, cuck.").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column = 1)

choices2 = { '1','11'}
tkvar2.set('1') # set the default option

minionNumber = Entry(mainWindow)
minionNumber.pack(side = RIGHT)

def getMinionNumber():
    if minionNumber.get() == "":
        return 0
    else:
        return int(minionNumber.get())

popupMenu1 = OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text="Choose a minion level, cuck.").grid(row = 1, column = 2)
popupMenu1.grid(row = 2, column = 2)

def calculate(minionValue):
    if tkvar.get() == 'Clay':
        if tkvar2.get() == '1':
            return minionValue * 16200
        elif tkvar2.get() == '11':
            return minionValue * 32400
    elif tkvar.get() == 'Redstone':
        if tkvar2.get() == '1':
            return minionValue * 10160 
        elif tkvar2.get() == '11':
            return minionValue * 16541
    elif tkvar.get() == 'Tarantula':
        if tkvar2.get() == '1':
            return minionValue * 91748
        elif tkvar2.get() == '11':
            return minionValue * 267366 
    elif tkvar.get() == 'Red Sand':
        if tkvar2.get() == '1':
            return minionValue * 85113
        elif tkvar2.get() == '11':
            return minionValue * 170226
    elif tkvar.get() == 'Mycellium':
        if tkvar2.get() == '1':
            return minionValue * 75944
        elif tkvar2.get() == '11':
            return minionValue * 151888
    else:
        return "FORTNITE"


def display():
    myLabel = Label(mainWindow, text = calculate(getMinionNumber()))
    myLabel.pack(side = TOP)
    print(calculate(getMinionNumber()))
    print(tkvar.get())
    print(tkvar2.get())

# Create a button
myButton = Button(mainWindow, text = "Click me!", command = display)
myButton.pack(side = TOP)

mainWindow.mainloop()