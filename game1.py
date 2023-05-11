from tkinter import *
from random import randint

win = Tk()

select = {
    1: "rock",
    2: "scissors",
    3: "paper"
}

lblResultUser = None  # Initialize lblResultUser
lblResultComputer = None  # Initialize lblResultComputer

def stone():
    global lblResultUser, lblResultComputer  # Use the global variables inside the function
    comp = randint(1,3)
    lbl["text"] = "computer choose: " + select[comp]
    if comp == 2:
        lblResultUser["text"] = str(int(lblResultUser["text"]) + 1)  # Update lblResultUser
    elif comp == 3:
        lblResultComputer["text"] = str(int(lblResultComputer["text"]) + 1)  # Update lblResultComputer

def scissors():
    global lblResultUser, lblResultComputer  # Use the global variables inside the function
    comp = randint(1,3)
    lbl["text"] = "computer choose: " + select[comp]
    if comp == 3:
        lblResultUser["text"] = str(int(lblResultUser["text"]) + 1)  # Update lblResultUser
    elif comp == 1:
        lblResultComputer["text"] = str(int(lblResultComputer["text"]) + 1)  # Update lblResultComputer
  

def paper():
    global lblResultUser, lblResultComputer  # Use the global variables inside the function
    comp = randint(1, 3)
    lbl["text"] = "computer choose: " + select[comp]
    if comp == 1:
        lblResultUser["text"] = str(int(lblResultUser["text"]) + 1)  # Update lblResultUser
    elif comp == 2:
        lblResultComputer["text"] = str(int(lblResultComputer["text"]) + 1)  # Update lblResultComputer

win.title("rock-scissor-paper")

# Rest of your code...
#win.minsize(300,400)

win.rowconfigure([0,1] , weight=1)
win.columnconfigure(0 , weight=1)
lbl = Label(master=win,text="your choose:",bg="#fff",height=2,font=("None",18,"bold"))
lbl.grid(row=0,column=0,sticky="nwe")

frmBtn = Frame(master=win,height=100,bg="red")
frmBtn.rowconfigure(0, weight=1)
frmBtn.columnconfigure([0,1,2] ,weight=1)
stoneBtn = Button(master=frmBtn,text="rock",height=3,
    font=("None",18,"bold"),command=stone).grid(row=0 ,column=0 ,sticky="nwes",padx=2,pady=3)
scissorsBtn = Button(master=frmBtn,text="scissors",height=3,
    font=("None",18,"bold"),command=scissors).grid(row=0 ,column=1 ,sticky="nwes",padx=2,pady=3)
paperBtn = Button(master=frmBtn,text="paper",height=3,
    font=("None",18,"bold"),command=paper).grid(row=0 ,column=2 ,sticky="nwes",padx=2,pady=3)
frmBtn.grid(row=1,column=0,sticky="wen")

frmResult = Frame(master=win, height=200)
frmResult.rowconfigure([0,1] , weight=1)
frmResult.columnconfigure([0,1], weight=1)

lblResultNameUser = Label(master=frmResult , text="your point:",
    relief="ridge").grid(row=0 ,column=0 ,sticky="nswe")
lblResultNameComputer = Label(master=frmResult , text="computer's point:",
    relief="ridge").grid(row=0 ,column=1 ,sticky="nswe")

lblResultUser = Label(master=frmResult,text="0",bg="yellow",fg="#fff",height=3,font=("None",40,"bold"))
lblResultUser.grid(
    row=1,column=0,sticky="nswe"
)
lblResultComputer = Label(master=frmResult, text="0",bg="green",fg="#fff",height=3,font=("None",40,"bold"))
lblResultComputer.grid(
    row=1,column=1,sticky="nswe"
)
frmResult.grid(row=2 ,column=0 ,sticky="nswe")

btnReset = Button(master=win,text="restart",font=("None",18,"bold"),
    borderwidth=4,relief="ridge",).grid(row=3 ,column=0, sticky="nswe")

win.mainloop()

