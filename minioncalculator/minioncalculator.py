from tkinter import *

mainWindow = Tk()
mainWindow.title("Slave Profits Calculator")

displayWindow = Tk()
displayWindow.title('information display')

displayTitle = Label(displayWindow, text="data")

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
Label(mainframe, text="Choose a minion").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column = 1)

choices2 = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'}
tkvar2.set('1') # set the default option

minionNumber = Entry(mainWindow)
minionNumber.pack(side = RIGHT)

def getMinionNumber():
    if minionNumber.get() == "":
        return 0
    else:
        return int(minionNumber.get())

popupMenu1 = OptionMenu(mainframe, tkvar2, *choices2)
Label(mainframe, text="Choose a minion level").grid(row = 1, column = 2)
popupMenu1.grid(row = 2, column = 2)

claylist = [16200, 16800, 17280, 18000, 18851, 20200, 21600, 23400, 25920, 29540, 32400]
redstonelist = [6704, 6900, 7200, 7450, 7776, 8100, 8453, 8800, 9258, 10000, 10800]
spiderlist = [92263, 97400, 102977, 109400, 116374, 123400, 141053, 163400, 184760, 230000, 269028]
redsandlist = [85757, 88400, 93845, 97400, 102376, 106400, 111483, 119400, 127010, 163400, 171513]
mycelliumlist = [76035, 79400, 82827, 86400, 90356, 94400, 98845, 105400, 111347, 136400, 152069]


def calculate(minionValue):
    if tkvar.get() == 'Clay':
        return minionValue * claylist[int(tkvar2.get())-1]
    elif tkvar.get() == 'Redstone':
        return minionValue * redstonelist[int(tkvar2.get())-1]
    elif tkvar.get() == 'Tarantula':
        return minionValue * spiderlist[int(tkvar2.get())-1]
    elif tkvar.get() == 'Red Sand':
        return minionValue * redsandlist[int(tkvar2.get())-1]
    elif tkvar.get() == 'Mycellium':
        return minionValue * mycelliumlist[int(tkvar2.get())-1]
    else:
        return "FORTNITE"


totalProfitsPerDay = 0
profits = 0

label0 = Label(displayWindow, text = "profits:")
label0.pack(side= LEFT)
myLabel = Label(displayWindow, text = profits)
myLabel.pack(side = LEFT)
totalProfitLabel = Label(displayWindow, text=str(totalProfitsPerDay))
totalProfitLabel.pack(side = RIGHT)
label1 = Label(displayWindow, text = "total profits per day:")
label1.pack(side= RIGHT)

def display():
    global myLabel
    global totalProfitLabel
    global profits
    global totalProfitsPerDay

    profits = calculate(getMinionNumber())
    totalProfitsPerDay += profits

    myLabel.config(text=profits)
    totalProfitLabel.config(text=totalProfitsPerDay)

# Create a button
myButton = Button(mainWindow, text = "Click me!", command = display)
myButton.pack(side = TOP)

displayWindow.mainloop()
mainWindow.mainloop()