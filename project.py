import sys
from tkinter import *


#Login window
Login = Tk()
Login.geometry("500x500+120+120")

global nameInput
global passInput

LoginLabel = Label(Login,text = "LOGIN:")
LoginLabel.grid(row=0,column = 0)
nameInput = Entry(Login)
passInput = Entry(Login)




nameLabel = Label(Login,text = "name:")
nameLabel.grid(row=1,column = 0,sticky = E)
nameInput.grid(row=1,column = 1)

passLabel = Label(Login,text = "password:")
passLabel.grid(row=2,column = 0,sticky = E)
passInput.grid(row=2,column = 1)

check = Checkbutton(Login,text = "Keep me logged in")
check.grid(row = 3,column = 1)

def PlayerM():
    PlayerM = Toplevel(Login)
    PlayerM.geometry("500x500+120+120")
    display = Label(PlayerM, text="Player Menu:")
    display.grid(row = 0,column = 1)
    
    TopB = Button(PlayerM,text = "Top Players:",fg = "green", command = TopM)
    GamesB = Button(PlayerM,text = "Games menu",fg = "green", command = GamesM)
    
    TopB.grid(row = 1,column = 0)
    GamesB.grid(row = 1,column = 2) 

    BackB = Button(PlayerM, text="Quit", command=PlayerM.destroy)
    BackB.grid(row = 7,column = 4)

def CheckLogin():
        if nameInput.get() == "david" and passInput.get() == "123456":
            AdminM()
        elif nameInput.get() == "sapir" or nameInput.get() == "bar" or nameInput.get() == "yair":
            WorkerM()
        else:
            PlayerM()

Login.mainloop()


