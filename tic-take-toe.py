from tkinter import *
from winsound import *

gui = Tk()
gui.title("tic-tac-toe")

label = Label(gui,text = ("tic-tiac-toe"),font="Arial 15")
label.grid(row=3,column=0)

playerX=True
playerO=False
#

# Player Turn
def changePlayer(choice):
    global playerX
    global playerO
    # Player X Turn
    #filled cant change
    if choice['text']== " " and playerX == True:
        choice["text"] = "X"
        # change turns
        playerX = False
        playerO = True
    #Player O Turn
    elif choice['text']== " " and playerO == True:
        choice["text"] = "O"
        # change turns
        playerX = True
        playerO = False

def checktie():
    if (Butt["text"] != (" ") and Butt2["text"] != (" ")  and Butt3["text"] and
            Butt4["text"]!=  (" ") and Butt5["text"]!= (" ") and Butt6["text"]!= (" ") and
        Butt7["text"]!=  (" ") and Butt8["text"]!= (" ") and Butt9["text"]!=(" ")):
        print ("Draw")
        winner["text"]="draw"






def checkWin():
    #Check for X
    if (Butt["text"] == "X" and Butt2["text"] == "X" and Butt3["text"] == "X" or
        Butt4["text"] == "X" and Butt5["text"] == "X" and Butt6["text"] == "X" or
        Butt7["text"] == "X" and Butt8["text"] == "X" and Butt9["text"] == "X" or
        Butt["text"] == "X" and Butt4["text"] == "X" and Butt7["text"] == "X" or
        Butt2["text"] == "X" and Butt5["text"] == "X" and Butt8["text"] == "X" or
        Butt3["text"] == "X" and Butt6["text"] == "X" and Butt9["text"] == "X" or
        Butt["text"] == "X" and Butt5["text"] == "X" and Butt9["text"] == "X" or
        Butt3["text"] == "X" and Butt5["text"] == "X" and Butt7["text"] == "X"):
        print("playerX wins")
        winner["text"]="PlayerX wins"
    #Check for O
    elif (Butt["text"] == "O" and Butt2["text"] == "O" and Butt3["text"] == "O" or
        Butt4["text"] == "O" and Butt5["text"] == "O" and Butt6["text"] == "O" or
        Butt7["text"] == "O" and Butt8["text"] == "O" and Butt9["text"] == "O" or
        Butt["text"] == "O" and Butt4["text"] == "O" and Butt7["text"] == "O" or
        Butt2["text"] == "O" and Butt5["text"] == "O" and Butt8["text"] == "O" or
        Butt3["text"] == "O" and Butt6["text"] == "O" and Butt9["text"] == "O" or
        Butt["text"] == "O" and Butt5["text"] == "O" and Butt9["text"] == "O" or
        Butt3["text"] == "O" and Butt5["text"] == "O" and Butt7["text"] == "O"):
        print("playerO wins")
        winner["text"]="player O wins"
    else:
        checktie()
    #if


def controller(choice):
    Beep(1000, 120)
    changePlayer(choice)
    checkWin()



"""""
    if Butt == True:
        Butt["text"] =  "X"
    if Butt2 == True:
        Butt2["text"] = "O"
    if Butt3 == True:
        Butt3["text"] = "X"
    if Butt4 == True:
        Butt4["text"] = "O"
    if Butt5 == True:
        Butt5["text"] = "X"
    if Butt6 == True:
        Butt6["text"] = "O"
    if Butt7 == True:
        Butt7["text"] = "X"
    if Butt8 == True:
        Butt8["text"] = "O"
    if Butt9 == True:
        Butt9["text"] = "X"
"""


Butt = Button(gui, text=" ",width=25,height=13, command=lambda:controller(Butt))
Butt.grid(row=0,column=0)
Butt2 = Button(gui, text=" ",width=25,height=13, command=lambda:controller(Butt2))
Butt2.grid(row=0,column=1)
Butt3 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt3))
Butt3.grid(row=0,column=2)
Butt4 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt4))
Butt4.grid(row=1,column=0)
Butt5 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt5))
Butt5.grid(row=1,column=1)
Butt6 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt6))
Butt6.grid(row=1,column=2)
Butt7 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt7))
Butt7.grid(row=2,column=0)
Butt8 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt8))
Butt8.grid(row=2,column=1)
Butt9 = Button(gui, text=" ",width=25, height=13, command=lambda:controller(Butt9))
Butt9.grid(row=2,column=2)


Butt10 = Button(gui, text="restart ",width=10, height=5)
Butt10.grid(row=3,column=2)

winner = Label(gui, text="winner ",width=10, height=5)
winner.grid(row=3,column=1)









gui.mainloop()
