from tkinter import *
from tkinter import font
import tkinter.messagebox
import fileinput
import random
import time
import subprocess
import pygame.mixer


global name
global nameInput 
global passInput
global newnameInput
global newpassInput
global score
name = " "
flag = 0
k = 0

random.seed()
pygame.mixer.init()
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'A', 'J', 'Q', 'K']
suits = ["clubs", "hearts", "spades", "diamonds"]
buttons = {}
deck1 = []
deck2 = []
center = {"d1":[], "d2":[]}

x=0
y=50
x2 = 0
y2 = 400

'''
login:
'''

def Login():
    
    global nameInput 
    global passInput
    Login = Toplevel(root)
    Login.geometry("750x750+200+0")
    
    Login.configure(background = 'peach puff')
    
    
    
    LoginLabel = Label(Login,text = "LOGIN:")
    LoginLabel.grid(row=0,column = 2)
    nameInput = Entry(Login)
    passInput = Entry(Login)
    
    
    
    nameLabel = Label(Login,text = "name:")
    nameLabel.grid(row=3,column = 1,sticky = E)
    nameInput.grid(row=3,column = 2)
    
    passLabel = Label(Login,text = "password:")
    passLabel.grid(row=4,column = 1,sticky = E)
    passInput.grid(row=4,column = 2)
    
    check = Checkbutton(Login,text = "Keep me logged in")
    check.grid(row = 5,column = 2)
    
    
    OK = Button(Login,text = "Login",fg = "purple",command=lambda:[CheckLogin(),Login.destroy()])
    OK.grid(row = 4,column = 4)
    
    SignUp = Button(Login,text = "sign-up",fg = "black", command = SignU)
    SignUp.grid(row = 4,column = 6)

def SignU():#sign-up window
    global newnameInput
    global newpassInput
    SignU = Toplevel(root)
    SignU.geometry("750x750+200+0")
    SignU.configure(background = 'SkyBlue1')
    
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
    
    
    Sign = Button(SignU,text = "Sign-up",fg = "purple",command=CSign)
    Sign.grid(row = 1,column = 3)

    BackB = Button(SignU, text="Back", command=lambda:[SignU.destroy(),Login()])
    BackB.grid(row = 7,column = 4)

def CSign():#update data base


    global newnameInput
    global newpassInput
    
    flag = 0
    
    if newnameInput.get() == '':
        tkinter.messagebox.showinfo(' ','no input')
        SignU()
        flag = 3
        
    if flag != 3:
        flag = CSing_c('champs.txt',newnameInput.get())
    
    
    if flag == 0:
        CSign_f("players.txt","champs.txt",newnameInput.get(),newpassInput.get())
        tkinter.messagebox.showinfo(' ','signed up succsesfuly!!')
        Login()
    if flag == 1:
        tkinter.messagebox.showinfo('error','already signed up')
        Login()

def CSign_f(file1,file2,namef,passw):
    file = open(file1,"a")
    file.write(namef)
    file.write(" ")
    file.write(passw)
    file.write("\n")
    file.close()
    
    
    filec = open(file2,"a")
    filec.write(namef)
    filec.write(" ")
    filec.write("0")
    filec.write("\n")
    filec.close()
    
def CSing_c(filef,name):
    
    with open(filef) as f:
        for i, l in enumerate(f):
            pass
    i += 1
    
    with open(filef) as f:
            lines = f.readlines()

    for k in range(i):
        newline = str(lines[k]).split()
        if name==newline[0]:
            return 1
    return 0

def CheckLogin():#login check
    global name
    global flag
    flag = 0    
    name = nameInput.get()
    
    if CheckLogin_f("admin.txt",name,passInput.get()):
        flag = 1
    
    if CheckLogin_f("workers.txt",name,passInput.get()):
        flag = 2
    
    if CheckLogin_f("players.txt",name,passInput.get()):
        flag = 3
    
                   
    if flag == 1:
        AdminM()
    if flag == 2:
        WorkerM()
    if flag == 3:
        PlayerM()
    if flag == 0:
        tkinter.messagebox.showinfo('bad log-in','invalid user name or password')#show message box if pass or user incorrect
        Login()        

def CheckLogin_f(testfile,name,passw):
    flag = 0 
    file = open(testfile, "r")
    for line in file.readlines(): # Read data base
        login_info = line.split()  
        
        if name == login_info[0] and passw == login_info[1]:
            flag = 1
    
    file.close()
    return flag
    
'''
player:
'''


def PlayerM():#player menu
      
    global name
    global flag
    PlayerM = Toplevel(root)
    PlayerM.geometry("750x750+200+0")
    display = Label(PlayerM, text="Player Menu:")
    display.grid(row = 0,column = 0)
    PlayerM.configure(background = 'purple3')
    
    TopB = Button(PlayerM,text = "Top 10 Players:",fg = "green", command=lambda:[TopM(),PlayerM.destroy()])
    TopB.grid(row = 3,column = 5)
    
    WarB = Button(PlayerM,text = "WAR",fg = "green", command=lambda:[create_deck(),PlayerM.destroy()])
    RowsB = Button(PlayerM,text = "4-ROW",fg = "green", command=lambda:[Rows(),PlayerM.destroy()])
    
    feed = Button(PlayerM, text="Leave a feedback", command=lambda:[Feeds(),PlayerM.destroy()])
    feed.grid(row=12, column=0)
    
    
    
    WarB.grid(row = 6,column = 0) 
    RowsB.grid(row = 6,column = 13) 


    if flag==3:
        BackB = Button(PlayerM, text="Quit", command=lambda:[Login(),PlayerM.destroy()])
        BackB.grid(row = 13,column = 0)
    if flag==1:
        BackB = Button(PlayerM, text="Quit", command=lambda:[AdminM(),PlayerM.destroy()])
        BackB.grid(row = 13,column = 0)
    if flag==2:
        BackB = Button(PlayerM, text="Quit", command=lambda:[WorkerM(),PlayerM.destroy()])
        BackB.grid(row = 13,column = 0)

def Feeds():
    global name
    global feedInput
    Feeds = Toplevel(root)
    Feeds.geometry("750x750+200+0")
    Feeds.configure(background = 'green')
    
    feedInput = Entry(Feeds)
    feedInput.grid(row=1,column = 1)
    
    
    OK = Button(Feeds,text = "OK",fg = "black",command = lambda:[FeedsUp(),Feeds.destroy(),PlayerM()])
    OK.grid(row = 1,column = 3)

    BackB = Button(Feeds, text="Back", command = lambda:[Feeds.destroy(),PlayerM()])
    BackB.grid(row = 7,column = 4)

def FeedsUp():
    global name
    global feedInput
    FeedsUp_f("feeds.txt",feedInput.get(),name)
    tkinter.messagebox.showinfo(' ','feed back have sent!!')

def FeedsUp_f(filename,feed,namef):
    file = open(filename,"a")
    file.write(namef)
    file.write(': ')
    file.write(feed)
    file.write("\n")
    file.close()

def TopM():#window of champions players
    TopM = Toplevel(root)
    TopM.geometry("750x750+200+0")
    TopM.configure(background = 'gold2')
    
    with open("champs.txt") as f:
        lines = f.readlines()
    
    with open("champs.txt") as f:
        for i, l in enumerate(f):
            pass
    i += 1
    
    for k in range(i):
        lines[k] = str(lines[k]).split()
    
    display = Label(TopM, text="Top Players:")
    display.grid(row = 0,column = 0)
    
    namel = Label(TopM, text="name:")
    namel.grid(row = 1,column = 1)
    placel = Label(TopM, text="place:")
    placel.grid(row = 1,column = 0)
    scorel = Label(TopM, text="score:")
    scorel.grid(row = 1,column = 2)
    
    place1 = Label(TopM, text='#1')
    place2 = Label(TopM, text='#2')
    place3 = Label(TopM, text='#3')
    place4 = Label(TopM, text='#4')
    place5 = Label(TopM, text='#5')
    
    name1 = Label(TopM, text=lines[0][0])
    name2 = Label(TopM, text=lines[1][0])
    name3 = Label(TopM, text=lines[2][0])
    name4 = Label(TopM, text=lines[3][0])
    name5 = Label(TopM, text=lines[4][0])
    
    score1 = Label(TopM, text=lines[0][1])
    score2 = Label(TopM, text=lines[1][1])
    score3 = Label(TopM, text=lines[2][1])
    score4 = Label(TopM, text=lines[3][1])
    score5 = Label(TopM, text=lines[4][1])
    
    name1.grid(row = 2,column = 1)
    name2.grid(row = 3,column = 1)
    name3.grid(row = 4,column = 1)
    name4.grid(row = 5,column = 1)
    name5.grid(row = 6,column = 1)
    
    score1.grid(row = 2,column = 2)
    score2.grid(row = 3,column = 2)
    score3.grid(row = 4,column = 2)
    score4.grid(row = 5,column = 2)
    score5.grid(row = 6,column = 2)
    
    place1.grid(row = 2,column = 0)
    place2.grid(row = 3,column = 0)
    place3.grid(row = 4,column = 0)
    place4.grid(row = 5,column = 0)
    place5.grid(row = 6,column = 0)
    
    
    
    
    BackB = Button(TopM, text="Quit", command=lambda:[TopM.destroy(),PlayerM()])
    BackB.grid(row = 10,column = 4)  

def Score_f(file,namef):
    for line in fileinput.input(file, inplace=1):
        split = line.split()
        x = int(split[1])
        x += 1
        x = split[0]+' '+str(x)+'\n'
        if namef==split[0]:
            line = line.replace(line,x)
        sys.stdout.write(line)


def Score():
    global name
    
    Score_f("champs.txt",name)
    UpdateScore("champs.txt")

def UpdateScore(file):
    

    with open(file) as f:
        lines = f.readlines()
    
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    i += 1
    
    for k in range(i):
        lines[k] = str(lines[k]).split()
    
    lines.sort(key=custom_sort,reverse = True)
    
    k = 0
    for line in fileinput.input(file, inplace=1):
        newline = lines[k][0]+' '+lines[k][1]+'\n'
        k += 1
        line = line.replace(line,newline)
        sys.stdout.write(line)

def custom_sort(t):
    return t[1]

'''
worker:
'''

def WorkerM(): #worker menu
    global GamesM
    WorkerM = Toplevel(root)
    WorkerM.geometry("750x750+200+0")
    display = Label(WorkerM, text="Worker Menu:")
    display.grid(row = 0,column = 1)
    WorkerM.configure(background = 'LemonChiffon3')
    
    ReportsB =  Button(WorkerM,text = "Reports",fg = "red", command=lambda:[ReportsM(),WorkerM.destroy()])  
    ReportsB.grid(row = 1,column = 0)
    
    SendM =  Button(WorkerM,text = "send massage to boss",fg = "red", command=lambda:[SendMSG(),WorkerM.destroy()])  
    SendM.grid(row = 2,column = 0)
    
    GamesB = Button(WorkerM,text = "Games menu",fg = "black", command=lambda:[PlayerM(),WorkerM.destroy()])
    GamesB.grid(row = 3,column = 0)  
    
    BackB = Button(WorkerM, text="Quit", command=lambda:[Login(),WorkerM.destroy()])
    BackB.grid(row = 4,column = 4)

def ReportsM():#reports button
    
    global k    
    ReportsM = Toplevel(root)
    ReportsM.geometry("750x750+200+0")
    ReportsM.configure(background = 'LemonChiffon3')
    
    display = Label(ReportsM, text="feedback:")
    
    display.grid(row = 0,column = 0)

    with open("feeds.txt") as f:
        lines = f.readlines()
    
    with open("feeds.txt") as f:
        for i, l in enumerate(f):
            pass
    i += 1
    k = 0
    flag=0
    
    
    nextfeed = Label(ReportsM, text=lines[k])
        
    
    def ShowFeed():
        global k
        nextfeed.config(text=lines[k])
        k += 1
            
    
    Next = Button(ReportsM, text="Next feedback", command =  ShowFeed)
    
    Next.grid(row = 5,column = 0) 
        
        
        
    nextfeed.grid(row = 0,column = 2) 
    
    
    BackB = Button(ReportsM, text="Quit", command=lambda:[ReportsM.destroy(),WorkerM()])
    BackB.grid(row = 7,column = 0)  

def SendMSG():
    global name
    SendMSG = Toplevel(root)
    SendMSG.geometry("750x750+200+0")
    SendMSG.configure(background = 'LemonChiffon3')
    global msgInput
    msgInput = Entry(SendMSG)
    msgInput.grid(row=0,column = 1)
    
    LoginLabel = Label(SendMSG,text = "enter a massage:")
    LoginLabel.grid(row=0,column = 0)
    
    
    
    SEND = Button(SendMSG,text = "SEND",fg = "black",command = lambda:[MsgUp(),SendMSG.destroy(),WorkerM()])
    SEND.grid(row = 0,column = 2)
    
    

    BackB = Button(SendMSG, text="Back", command=lambda:[WorkerM(),SendMSG.destroy()])
    BackB.grid(row = 7,column = 0)    

def MsgUp():
    global name
    global msgInput
    file = open("msgs.txt","a")
    file.write(name)
    file.write(': ')
    file.write(msgInput.get())
    file.write('\n')
    
    file.close()
    tkinter.messagebox.showinfo(' ','massage  have sent!!')

'''
admin:
'''

def AdminM(): #admin menu
    AdminM = Toplevel(root)
    AdminM.geometry("750x750+200+0")
    display = Label(AdminM, text="Admin Menu:")
    display.grid(row = 0,column = 2) 
    AdminM.configure(background = 'grey20')
    
    SingUPW =  Button(AdminM,text = "Sing-Up new worker",fg = "black", command=lambda:[SingUpWorker(),AdminM.destroy()]) 
    SingUPW.grid(row = 1,column = 2)
    
    MassegesB =  Button(AdminM,text = "see massages",fg = "black", command=lambda:[Msger(),AdminM.destroy()])  
    MassegesB.grid(row = 3,column = 2)
    
    GamesB = Button(AdminM,text = "Games menu",fg = "black", command=lambda:[PlayerM(),AdminM.destroy()])
    GamesB.grid(row = 5,column = 2)  
    
    ReportsB =  Button(AdminM,text = "Reports",fg = "red", command=lambda:[ReportsM2(),AdminM.destroy()])  
    ReportsB.grid(row = 7,column = 2)
    
    BackB = Button(AdminM, text="Quit", command=lambda:[Login(),AdminM.destroy()])
    BackB.grid(row = 7,column = 0)

def ReportsM2():#reports button
    
    global k    
    ReportsM2 = Toplevel(root)
    ReportsM2.geometry("750x750+200+0")
    ReportsM2.configure(background = 'grey3')
    
    display = Label(ReportsM2, text="feedback:")
    
    display.grid(row = 0,column = 0)

    with open("feeds.txt") as f:
        lines = f.readlines()
    
    with open("feeds.txt") as f:
        for i, l in enumerate(f):
            pass
    i += 1
    k = 0
    flag=0
    nextfeed = Label(ReportsM2, text=lines[k])
    def ShowFeed():
        global k
        nextfeed.config(text=lines[k])
        k += 1
            
    
    Next = Button(ReportsM2, text="Next feedback", command =  ShowFeed)
    
    Next.grid(row = 5,column = 0) 
        
        
        
    nextfeed.grid(row = 0,column = 2) 
    
    
    
    
    BackB = Button(ReportsM2, text="Quit", command=lambda:[ReportsM2.destroy(),AdminM()()])
    BackB.grid(row = 7,column = 0)  

def Msger():#massages sending button
    
    global k    
    Msger = Toplevel(root)
    Msger.geometry("750x750+200+0")
    Msger.configure(background = 'grey25')
    
    
    display = Label(Msger, text="workers massages:")
    display.grid(row = 0,column = 1)
    
    workername = Entry(Msger)
    workername.grid(row=1,column = 1)
    
    newLabel = Label(Msger,text = "choose a name:")
    newLabel.grid(row=1,column = 0,sticky = E)
    
    with open("msgs.txt") as f:
        lines = f.readlines()
    
    with open("msgs.txt") as f:
        for i, l in enumerate(f):
            pass
    i += 1
    k = 0
    nextmsg = Label(Msger, text=":...")
    
    def NextMSG():
        global k
        while not (lines[k].startswith(workername.get())):
            k += 1
        
        nextmsg.config(text=lines[k])
        k += 1
    
    def ShowMSG():
        
        global k
        k=0
        with open("msgs.txt") as f:
            lines = f.readlines()
        
        while not (lines[k].startswith(workername.get())):
            k += 1
        
        nextmsg.config(text=lines[k])
        k += 1   
    
    Next = Button(Msger, text="Next massage", command =  NextMSG)
    
    Next.grid(row = 4,column = 0)
    
    Show = Button(Msger, text="Show massages", command =  ShowMSG)
    
    Show.grid(row = 1,column = 2)
        
        
        
    nextmsg.grid(row = 3,column = 0) 
    
    
    
    
    BackB = Button(Msger, text="Quit", command=lambda:[AdminM(),Msger.destroy()])
    BackB.grid(row = 6,column = 4) 

def SingUpWorker():#window for updating data (for administrator)
    SingUpWorker = Toplevel(root)
    SingUpWorker.geometry("750x750+200+0")
    SingUpWorker.configure(background = 'grey30')
    display = Label(SingUpWorker, text="Enter details of new worker:")
    display.grid(row = 0,column = 1)
    
    newnameInput = Entry(SingUpWorker)
    newpassInput = Entry(SingUpWorker)
    
   
    
    
    newnameLabel = Label(SingUpWorker,text = "choose a name:")
    newnameLabel.grid(row=1,column = 0,sticky = E)
    newnameInput.grid(row=1,column = 1)

    newpassLabel = Label(SingUpWorker,text = "choose a password:")
    newpassLabel.grid(row=2,column = 0,sticky = E)
    newpassInput.grid(row=2,column = 1)
    
    Sign = Button(SingUpWorker,text = "Sign-up",fg = "purple",command=lambda:[CSignW(newnameInput.get(),newpassInput.get()),SingUpWorker.destroy(),AdminM()])
    Sign.grid(row = 1,column = 3)

    BackB = Button(SingUpWorker, text="Back", command=lambda:[AdminM(),SingUpWorker.destroy()])
    BackB.grid(row = 4,column = 4)

def CSignW(newname,newpass):
    
    flag = 0
    
    
    
    if newname == '':
        tkinter.messagebox.showinfo(' ','no input')
        SignU()
        flag = 3
    
    if flag != 3:
        flag = CSing_c('champs.txt',newnameInput.get())
        
    if flag == 0:
        file = open('workers.txt',"a")
        file.write(newname)
        file.write(" ")
        file.write(newpass)
        file.write("\n")
        file.close()
    
    
        filec = open("champs.txt","a")
        filec.write(newname)
        filec.write(" ")
        filec.write("0")
        filec.write("\n")
        filec.close()
        tkinter.messagebox.showinfo('error','signed up succsesfuly!!')
    
    if flag == 1:
        tkinter.messagebox.showinfo('error','already signed up')    

'''
war game:
'''
def popup(root, header, text, windowHeight=500, windowWidth=500, winx=0, winy=0):
    def closePopup():
        window.destroy()
    window = Toplevel(root, height=windowHeight, width=windowWidth)
    window.wm_title(header)
    label = Label(window, text=text, relief = SUNKEN)
    label.place(x=winx, y=winy, height = 500, width = 500)
    button = Button(window, text="Close")
    button.config(command=closePopup)
    button.place(x=300, y=300)
       
def get_posscards():
    global posscards
    posscards = []
    for i in numbers:
        for j in suits:
            posscards.append(i+"_of_"+j+".gif")

def create_random_card(xpos, ypos, col=False):
    img = PhotoImage(file=random.choice(numbers)+"_of_"+random.choice(suits)+".gif")
    button = Label(root, image=img)
    button.img = img
    if col:
        button.grid(row=xpos, column=ypos)
    else:
        button.place_configure(x=xpos, y=ypos)
    buttons.append(button)
     
def create_card(name, undername, xpos, ypos, typ, col=False):
    img = PhotoImage(file="resources/"+name)
    button = Button(root, image=img)
    button.config(command=lambda undername=undername: flip(button, undername))
    button.img = img
    button.subimg = undername
    button.typ = typ
    button.name = name
    buttons[undername] = button
    if col:
        button.grid(row=xpos, column=ypos)
    else:
        button.place_configure(x=xpos, y=ypos)  
          
def create_deck():
    global buttons
    global center
    
  
    
    
    def destroycards():
        global buttons
        global center
        indx = 0
        
        cards = list(buttons.keys())
        while indx < len(cards):
            buttons[cards[indx]].destroy()
            indx += 1
        
        indx = 0
           
        while indx < len(center["d1"]):
            center["d1"][indx].destroy()
            indx += 1
        
        indx = 0
        
        while indx < len(center["d2"]):
            center["d2"][indx].destroy()
            indx += 1   
        
        indx = 0
       
        
        
    
    for i in deck1:
        deck1.remove(i)
    get_posscards()
    for i in range(30):
        random.shuffle(posscards)
        print("Shuffling...")
    subi = "back.gif"
    for i in range(0, len(posscards), 2):
        create_card(subi, posscards[i], x, y, "d1")
        create_card(subi, posscards[i+1], x2, y2, "d2")
        deck1.append(posscards[i])
        deck2.append(posscards[i+1])
    
    update()
    
    quit = Button(root, text="QUIT", command=lambda:[PlayerM(),info.destroy(),t.destroy(),quit.destroy(),feed.destroy(),destroycards()])
    quit.grid(row=1, column=15) 
      
def flip(button, name):


    if button.typ == "d1":
        if center["d1"] == []:
            if deck1[0]=="redo.gif":
                for button in center:
                    button.destroy()
                
                create_deck()
            else:
                img = PhotoImage(file="resources/"+name)
                button.place_configure(x=button.winfo_x()+210)
                button.config(image=img, command=null)
                button.img = img
                button.lift()
                deck1.remove(name)
                center["d1"] = [button]
    else:
        if center["d2"] == []:
            if deck2[0]=="redo.gif":
                for button in center:
                    button.destroy()
                
                create_deck()
            else:
                img = PhotoImage(file="resources/"+name)
                button.place_configure(x=button.winfo_x()+210)
                button.config(image=img, command=null)
                button.img = img
                button.lift()
                deck2.remove(name)
                center["d2"] = [button]
    update()
    root.update_idletasks()
    root.update()
    time.sleep(0.5)
    compare()
    update()    

def compare():
    if len(center["d1"])>0 and len(center["d2"])>0:
        #print(numbers.index(center["d1"][0].subimg[0]))
        if numbers.index(center["d1"][0].subimg[0])>\
           numbers.index(center["d2"][0].subimg[0]):
            deck1.insert(0, center["d1"][0].subimg)
            deck1.insert(0, center["d2"][0].subimg)
            center["d1"][0].destroy()
            center["d2"][0].destroy()
            center["d1"] = []
            center["d2"] = []
            popup(root, "YOU Won", "YOU won that battle!!!")
        elif numbers.index(center["d1"][0].subimg[0])<\
           numbers.index(center["d2"][0].subimg[0]):
            deck2.insert(0, center["d1"][0].subimg)
            deck2.insert(0, center["d2"][0].subimg)
            center["d1"][0].destroy()
            center["d2"][0].destroy()
            center["d1"] = []
            center["d2"] = []
            popup(root, "Guest Won", "Guest won that battle!!!")
        else:
            war()
    update()    

def war():
    #Flip function, except will flip farther and ignores subcenter argubouncing
    for i in range(4):
        button = buttons[deck1[-1]]
        img = PhotoImage(file="resources/"+button.subimg)
        button.place_configure(x=button.winfo_x()+210 * (i+2))
        button.config(image=img, command=null)
        button.img = img
        button.lift()
        deck1.remove(button.subimg)
        center["d1"].append(button)
        update()
    for i in range(4):
        button = buttons[deck2[-1]]
        img = PhotoImage(file="resources/"+button.subimg)
        button.place_configure(x=button.winfo_x()+210 * (i+2))
        button.config(image=img, command=null)
        button.img = img
        button.lift()
        deck2.remove(button.subimg)
        center["d2"].append(button)
        update()
    directcompare(center["d1"][-1], center["d2"][-1])

def directcompare(c1, c2):
    time.sleep(0.5)
    #again ignores subcenter argubouncing and subaliasing; specified proarguments
    if numbers.index(c1.subimg[0])>\
       numbers.index(c2.subimg[0]):
        for i in center["d1"]:
            deck1.insert(0, i.subimg)
        for i in center["d2"]:
            deck1.insert(0, i.subimg)

        for i in center["d1"]:
            i.destroy()
        for i in center["d2"]:
            i.destroy()
        center["d1"] = []
        center["d2"] = []
        popup(root, "YOU Won", "YOU won that war!!!")
        
    elif numbers.index(c1.subimg[0])<\
       numbers.index(c2.subimg[0]):
        for i in center["d1"]:
            deck2.insert(0, i.subimg)
        for i in center["d2"]:
            deck2.insert(0, i.subimg)

        for i in center["d1"]:
            i.destroy()
        for i in center["d2"]:
            i.destroy()
        center["d1"] = []
        center["d2"] = []
        popup(root, "Guest Won", "Guest won that war!!!")
    else:
        war()
    update()
        
def update():
    root.update_idletasks()
    root.update()
    for i in buttons.values():
        if not (i in center["d1"]) and (not (i in center["d2"])):
            i.destroy()
    for i in range(0, len(deck1), 1):
        create_card("back.gif", deck1[i], x, y, "d1")
    for i in range(0, len(deck2), 1):
        create_card("back.gif", deck2[i], x2, y2, "d2")  
              
def null(): 
    pass

def War():#not courently in use
    War = Toplevel(root)
    War.geometry("750x750+200+0")
    display = Label(War, text="War game:")
    display.grid(row = 0,column = 1)
    
    BackB = Button(War, text="Quit", command=War.destroy)
    BackB.grid(row = 7,column = 4)  
    
    Rows = Toplevel(Login)
    Rows.geometry("750x750+200+0")
    display = Label(Rows, text="4-ROW game:")
    display.grid(row = 0,column = 1) 
    
    BackB = Button(Rows, text="Back", command=Rows.destroy)
    BackB.grid(row = 7,column = 4)  

'''
4-row game:
'''

def Rows():
    global info
    global name
    global feed
    global new
    global quit

    
    
    
    info = Info(root)
    info.grid(row=0, column=0)
    
    t = Terrain(root)
    t.grid(row=1, column=0) 
    
   
    new = Button(root, text="NEW GAME", command=Rows)
    new.grid(row=0, column=1)
    quit = Button(root, text="QUIT", command=lambda:[PlayerM(),info.destroy(),t.destroy(),quit.destroy(),new.destroy()])
    quit.grid(row=2, column=3)
    
class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        police = font.Font(self, size=20, family='Arial')
        self.t = Label(self, text="Guest turn", font=police)
        self.t.grid(sticky=NSEW, pady=20)

class Piont(object):
    def __init__(self, x, y, can, coul="white", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.coul = coul

        self.tour = 1
        
        self.r = 30
        self.piont = self.can.create_oval(self.x+10,self.y+10,self.x+61,self.y+61,fill=coul,outline="blue")
        
        

    def changeCouleur(self, coul):
        self.can.itemconfigure(self.piont, fill=coul)
        self.coul = coul

class Terrain(Canvas):
    global name
    
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="blue")

        self.joueur = 1
        self.coul = "yellow"
        self.p = []
        self.perm = True
        
        for i in range(0, 340, int(400/6)):
            liste_rangee = []
            for j in range(0, 440, int(500/7)):
                liste_rangee.append(Piont(j, i ,self))
                
            self.p.append(liste_rangee)
        
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x/71)
            lig = 0
            
            lig = 0
            while lig < len(self.p):            
                if self.p[0][col].coul == "red" or self.p[0][0].coul == "yellow":
                    break
                
                if self.p[lig][col].coul == "red" or self.p[lig][col].coul == "yellow":
                    self.p[lig-1][col].changeCouleur(self.coul)
                    break
                
                elif lig == len(self.p)-1:
                    self.p[lig][col].changeCouleur(self.coul)
                    break

                
                if self.p[lig][col].coul != "red" and self.p[lig][col].coul != "yellow":
                    lig+=1

            
            
            if self.joueur == 1:
                self.joueur = 2
                info.t.config(text="Your turn")
                self.coul = "red"

            elif self.joueur == 2:
                self.joueur = 1
                info.t.config(text="Guest turn")
                self.coul = "yellow"

            self.Horizontal()
            self.Vertical()
            self.Diagonal1()
            self.Diagonal2()

    def Horizontal(self):
        i = 0
        while(i < len(self.p)):
            j = 0
            while(j < 3):
                if(self.p[i][j].coul == self.p[i][j+1].coul == self.p[i][j+2].coul == self.p[i][j+3].coul == "red"):
                    info.t.config(text="YOU WON !!!")
                    self.perm = False
                    Score()
                    break
                elif(self.p[i][j].coul == self.p[i][j+1].coul == self.p[i][j+2].coul == self.p[i][j+3].coul == "yellow"):
                    info.t.config(text="Guest Won :(")
                    self.perm = False
                    break
                j +=1
            i += 1

    def Vertical(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < len(self.p[i])):
                if(self.p[i][j].coul == self.p[i+1][j].coul == self.p[i+2][j].coul == self.p[i+3][j].coul == "red"):
                    info.t.config(text="YOU WON !!!")
                    self.perm = False
                    Score()
                    break
                elif(self.p[i][j].coul == self.p[i+1][j].coul == self.p[i+2][j].coul == self.p[i+3][j].coul == "yellow"):
                    info.t.config(text="Guest Won :(")
                    self.perm = False
                    break
                j+=1
            i+=1

    def Diagonal1(self):
        i = 0
        while(i < 3):
            j = 0
            while(j < 3):
                if(self.p[i][j].coul == self.p[i+1][j+1].coul == self.p[i+2][j+2].coul == self.p[i+3][j+3].coul == "red"):
                    score()
                    info.t.config(text="YOU WON !!!")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i+1][j+1].coul == self.p[i+2][j+2].coul == self.p[i+3][j+3].coul == "yellow"):
                    info.t.config(text="Guest Won :(")
                    self.perm = False
                    break
                j += 1
            i += 1
                    
    def Diagonal2(self):
        i = 0
        while(i < 3):
            j = len(self.p[i])-1
            while(j > len(self.p)-4):
                if(self.p[i][j].coul == self.p[i+1][j-1].coul == self.p[i+2][j-2].coul == self.p[i+3][j-3].coul == "red"):
                    score()
                    info.t.config(text="YOU WON !!!")
                    self.perm = False
                    break
                elif(self.p[i][j].coul == self.p[i+1][j-1].coul == self.p[i+2][j-2].coul == self.p[i+3][j-3].coul == "yellow"):
                    info.t.config(text="Guest Won :(")
                    self.perm = False
                    break
                j -= 1
            i += 1


'''
main:
'''

root = Tk()
root.geometry("750x750+200+0")
root.title("4PLAY")
root.configure(background = 'light blue')

feed = Button(root, text="Leave a feedback", command=Feeds)
new = Button(root, text="NEW GAME", command=Rows)

quit = Button(root, text="QUIT", command=lambda:[PlayerM(),info.destroy(),t.destroy(),feed.destroy(),new.destroy()])


info = Info(root)
t = Terrain(root)

LOG = Button(root,text = "LOG-IN/SIGHN-UP",fg = "black",command=lambda:[Login(),LOG.destroy()])
LOG.grid(row = 0,column = 3)


root.mainloop()
