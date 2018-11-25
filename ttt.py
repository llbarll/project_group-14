import sys
from tkinter import *
import tkinter.messagebox
#the program will use a database txt file named "accountfile.txt"

#Login window
Login = Tk()
Login.geometry("500x500+120+120")

global nameInput
global passInput
global newnameInput
global newpassInput

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

def UpdateR():#window for updating data (for administrator)
    UpdateR = Toplevel(Login)
    UpdateR.geometry("500x500+120+120")
    display = Label(UpdateR, text="Update data menu:")
    display.grid(row = 0,column = 1)
    
    BackB = Button(UpdateR, text="Back", command=UpdateR.destroy)
    BackB.grid(row = 7,column = 4)  

def ReportsM():#reports button
    ReportsM = Toplevel(Login)
    ReportsM.geometry("500x500+120+120")
    display = Label(ReportsM, text="Reports:")
    display.grid(row = 0,column = 1)
    
    BackB = Button(ReportsM, text="Quit", command=ReportsM.destroy)
    BackB.grid(row = 7,column = 4)  

def TopM():#window of champions players
    TopM = Toplevel(Login)
    TopM.geometry("500x500+120+120")
    display = Label(TopM, text="Top Players:")
    display.grid(row = 0,column = 1)
    
    BackB = Button(TopM, text="Quit", command=TopM.destroy)
    BackB.grid(row = 7,column = 4)  
    
def War():#war game
    War = Toplevel(Login)
    War.geometry("500x500+120+120")
    display = Label(War, text="War game:")
    display.grid(row = 0,column = 1)
    
    BackB = Button(War, text="Quit", command=War.destroy)
    BackB.grid(row = 7,column = 4)  
    
def Rows():#4-row game
    Rows = Toplevel(Login)
    Rows.geometry("500x500+120+120")
    display = Label(Rows, text="4-ROW game:")
    display.grid(row = 0,column = 1) 
    
    BackB = Button(Rows, text="Back", command=Rows.destroy)
    BackB.grid(row = 7,column = 4)  

def GamesM():#games menu
    GamesM = Toplevel(Login)
    GamesM.geometry("500x500+120+120")
    display = Label(GamesM, text="Games Players:")
    display.grid(row = 0,column = 0)
    
    WarB = Button(GamesM,text = "WAR",fg = "green", command = War)
    RowsB = Button(GamesM,text = "4-ROW",fg = "green", command = Rows)
    
    WarB.grid(row = 3,column = 0) 
    RowsB.grid(row = 3,column = 10) 
    
    BackB = Button(GamesM, text="Back", command=GamesM.destroy)
    BackB.grid(row = 7,column = 4)

def AdminM(): #admin menu
    AdminM = Toplevel(Login)
    AdminM.geometry("500x500+120+120")
    display = Label(AdminM, text="Admin Menu:")
    display.grid(row = 0,column = 1) 
    
    UpdateB =  Button(AdminM,text = "Update",fg = "black", command = UpdateR) 
    UpdateB.grid(row = 1,column = 0)
    
    ReportsB =  Button(AdminM,text = "Reports",fg = "black", command = ReportsM)  
    ReportsB.grid(row = 1,column = 1)
    
    GamesB = Button(AdminM,text = "Games menu",fg = "black", command = GamesM)
    GamesB.grid(row = 1,column = 2)  
    
    BackB = Button(AdminM, text="Quit", command=AdminM.destroy)
    BackB.grid(row = 7,column = 4)

def WorkerM(): #worker menu
    WorkerM = Toplevel(Login)
    WorkerM.geometry("500x500+120+120")
    display = Label(WorkerM, text="Worker Menu:")
    display.grid(row = 0,column = 1)
    
    ReportsB =  Button(WorkerM,text = "Reports",fg = "red", command = ReportsM)  
    ReportsB.grid(row = 1,column = 0)
    
    GamesB = Button(WorkerM,text = "Games menu",fg = "red", command = GamesM)
    GamesB.grid(row = 1,column = 1)
    
    BackB = Button(WorkerM, text="Quit", command=WorkerM.destroy)
    BackB.grid(row = 7,column = 4)
    
def PlayerM():#player menu
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

def CheckLogin():#login check
    flag = 0  
         
    for line in open("admin.txt","r").readlines(): # Read data base
        login_info = line.split()  
        if nameInput.get() == login_info[0] and passInput.get() == login_info[1]:
            flag = 1
            
    for line in open("workers.txt","r").readlines(): # Read data base
        login_info = line.split() 
        if nameInput.get() == login_info[0] and passInput.get() == login_info[1]:
            flag = 2
            
    for line in open("accountfile.txt","r").readlines(): 
        login_info = line.split() 
        if nameInput.get() == login_info[0] and passInput.get() == login_info[1]:
            flag = 3
                   
    if flag == 1:
        AdminM()
    if flag == 2:
        WorkerM()
    if flag == 3:
        PlayerM()
    if flag == 0:
        tkinter.messagebox.showinfo('bad log-in','invalid user name or password')#show message box if pass or user incorrect
            
           
                
def CSign():#update data base
    global newnameInput
    global newpassInput
    file = open("accountfile.txt","a")
    file.write(newnameInput.get())
    file.write(" ")
    file.write(newpassInput.get())
    file.write("\n")
    file.close()
    
def SignU():#sign-up window
    global newnameInput
    global newpassInput
    SignU = Toplevel(Login)
    SignU.geometry("500x500+120+120")
    display = Label(SignU, text="SignUp:")
    display.grid(row = 0,column = 1)
    
    newnameInput = Entry(SignU)
    newpassInput = Entry(SignU)
    
   
    
    
    newnameLabel = Label(SignU,text = "choose a name:")
    newnameLabel.grid(row=1,column = 0,sticky = E)
    newnameInput.grid(row=1,column = 1)

    newpassLabel = Label(SignU,text = "choose a password:")
    newpassLabel.grid(row=2,column = 0,sticky = E)
    newpassInput.grid(row=2,column = 1)
    

    
    
    
    
    
    
    Sign = Button(SignU,text = "Sign-up",fg = "purple",command = CSign)
    Sign.grid(row = 1,column = 3)

    BackB = Button(SignU, text="Back", command=SignU.destroy)
    BackB.grid(row = 7,column = 4)


SignUp = Button(Login,text = "sign-up",fg = "black", command = SignU)
SignUp.grid(row = 6,column = 0)



OK = Button(Login,text = "Login",fg = "purple",command = CheckLogin)
OK.grid(row = 1,column = 3)


Login.mainloop()
