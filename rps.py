import tkinter as tk
import random
from tkinter import messagebox

# function for Rock button
def isRock():
    global count
    global p_score
    global c_score
    global p_choics_lbl
    global c_choice_lbl
    while(count<12):
        com_choice = random.choice(["rock","paper","scissor"])
        if(com_choice=="rock"):
            pass
        elif(com_choice=="paper"):
            global com_point
            com_point += 1
            c_score.config(text = com_point)
        else:
            global player_point
            player_point += 1
            p_score.config(text = player_point)

        p_choics_lbl.config(text = "rock")
        c_choice_lbl.config(text = com_choice)
        count += 1
        show_round_lbl.config(text = count)
        if(count==12):
            result()
        break

# function for paper button
def isPaper():
    global count
    global p_score
    global c_score
    global p_choics_lbl
    global c_choice_lbl
    while(count<12):
        com_choice = random.choice(["rock","paper","scissor"])
        if(com_choice=="paper"):
            pass
        elif(com_choice=="scissor"):
            global com_point
            com_point += 1
            c_score.config(text = com_point)
        else:
            global player_point
            player_point += 1
            p_score.config(text = player_point)

        p_choics_lbl.config(text = "paper")
        c_choice_lbl.config(text = com_choice)
        count += 1
        show_round_lbl.config(text = count)
        if(count==12):
            result()
        break

# function for scissor button
def isScissor():
    global count
    global p_score
    global c_score
    global p_choics_lbl
    global c_choice_lbl
    while(count<12):
        com_choice = random.choice(["rock","paper","scissor"])
        if(com_choice=="scissor"):
            pass
        elif(com_choice=="rock"):
            global com_point
            com_point += 1
            c_score.config(text = com_point)
        else:
            global player_point
            player_point += 1
            p_score.config(text = player_point)

        p_choics_lbl.config(text = "scissor")
        c_choice_lbl.config(text = com_choice)
        count += 1
        show_round_lbl.config(text = count)
        if(count==12):
            result()
        break

# result function
def result():
    global player_point
    global com_point
    if(player_point>com_point):
        show_res_lbl.config(text = "You Win :)")
    elif(player_point<com_point):
        show_res_lbl.config(text = "Computer Win!!")
    else:
        show_res_lbl.config(text = "Match Tie!!")

# function for reset button
def reset():
    msg_result = messagebox.askyesno("Reset Game","Do you want to reset game!!")
    if(msg_result==0):
        pass
    else:
        global player_point
        global com_point
        global count
        global p_score
        global c_score
        global show_round_lbl
        global show_res_lbl
        global p_choics_lbl
        global c_choice_lbl

        # reset labels
        player_point = 0
        com_point = 0
        count = 0

        # config of labels
        p_score.config(text = player_point)
        c_score.config(text = com_point)
        show_round_lbl.config(text = count)
        show_res_lbl.config(text = "")
        p_choics_lbl.config(text = "Player")
        c_choice_lbl.config(text = "Computer")

# show message function
def showMessage():
    messagebox.showinfo("How to play?","1.There are total 12 rounds.\n2.You play against computer.\n3.To choose Rock, Paper, Scissor click on respective button.\n4.Among both whose score is high will win.\n5.Best of Luck :)\n\n          Created by Mudit Choudhary")


# setup app window
app = tk.Tk()
app.geometry("450x650")
app.maxsize(450,650)
app.title("Rock Paper Scissor")
app.iconbitmap(r'D:\Python Projects\GuiRockPaperScisoor\Images\icon.ico')

# important variables
count = 0
player_point = 0
com_point = 0
# head label
tk.Label(
    app,
    text='Rock Paper Scissor',
    font=("Comic Sans MS",26,"bold"),
    fg='blue'
).pack()

# frame1
frame1 = tk.Frame(app)
frame1.pack(
    pady=(17,0)
)

#Player Score label
p_lbl = tk.Label(
    frame1,
    text="P : ",
    font=("Comic Sans MS",18),
    fg='black'
)
p_lbl.pack(
    side=tk.LEFT
)

# player score 
p_score = tk.Label(
    frame1,
    text=0,
    font=("Comic Sans MS",18),
    fg='red',
    borderwidth=1,
    relief="solid"

)
p_score.pack(
    side=tk.LEFT,
    padx=(0,135),
    ipadx=2,
    ipady=2
)

# computer score label
c_lbl = tk.Label(
    frame1,
    text="C : ",
    font=("Comic Sans MS",18),
    fg='black'
)
c_lbl.pack(
    side=tk.LEFT
)

# computer score
c_score = tk.Label(
    frame1,
    text=0,
    font=("Comic Sans MS",18),
    fg='red',
    borderwidth=1,
    relief="solid"
)
c_score.pack(
    side=tk.LEFT,
    ipadx=2,
    ipady=2
)

# frame 2
frame2 = tk.Frame(app)
frame2.pack(
    pady=(17,0)
)
# show player choices label
p_choics_lbl = tk.Label(
    frame2,
    text="Player",
    font=("Comic Sans MS",18)
)
p_choics_lbl.pack(
    side=tk.LEFT
)

# vs label
vs_lbl = tk.Label(
    frame2,
    text="VS",
    font=("Comic Sans MS",18,"bold")
)
vs_lbl.pack(
    side=tk.LEFT,
    padx=(30,30)
)

#show computer choices label
c_choice_lbl = tk.Label(
    frame2,
    text="Computer",
    font=("Comic Sans MS",18)
)
c_choice_lbl.pack(
    side=tk.LEFT
)

# frame3
frame3 = tk.Frame(app)
frame3.pack(
    pady=(17,0)
)

# rock button
rock_btn = tk.Button(
    frame3,
    text="Rock",
    font=("Comic Sans MS",15),
    fg="grey",
    command=isRock
)
rock_btn.pack(
    side=tk.LEFT,
    padx=(0,30)
)

# paper button
paper_btn = tk.Button(
    frame3,
    text="Paper",
    font=("Comic Sans MS",15),
    fg="cyan",
    command = isPaper
)
paper_btn.pack(
    side=tk.LEFT,
    padx=(0,30)
)

# scissor button
scissor_btn = tk.Button(
    frame3,
    text="Scissor",
    font=("Comic Sans MS",15),
    fg="green",
    command = isScissor
)
scissor_btn.pack(
    side=tk.LEFT
)

# frame 4
frame4 = tk.Frame(app)
frame4.pack(
    pady=(17,0)
)

# Result lbl
res_lbl = tk.Label(
    frame4,
    text="Result : ",
    font=("Comic Sans MS",15)
)
res_lbl.pack(
    side=tk.LEFT
)

# show result lablel
show_res_lbl = tk.Label(
    frame4,
    bg="white",
    text = "",
    width=25,
    borderwidth=1,
    relief="solid",
    font=("Comic Sans MS",15)
)
show_res_lbl.pack(
    side=tk.LEFT
)

# frame 5
frame5 = tk.Frame(app)
frame5.pack(
    pady=(20,0)
)
# rounds label
round_lbl = tk.Label(
    frame5,
    text = "Round : ",
    font=("Comic Sans MS",15)
)
round_lbl.pack(
    side=tk.LEFT
)

# show rounds label
show_round_lbl = tk.Label(
    frame5,
    text = count,
    bg="white",
    width=25,
    borderwidth=1,
    relief="solid",
    font=("Comic Sans MS",15)
)
show_round_lbl.pack(
    side=tk.LEFT,
    pady=(17,0)
)

# frame 6
frame6 = tk.Frame(app)
frame6.pack()
# reset button
reset_btn = tk.Button(
    frame6,
    text="Reset Game",
    font=("Comic Sans MS",15),
    bg="black",
    fg="red",
    command = reset
)
reset_btn.pack(
    pady=(17,0)
)
showMessage()

app.mainloop()