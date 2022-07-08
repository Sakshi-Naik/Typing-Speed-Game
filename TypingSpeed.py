words = ["Python","Mango", "summer", "happy", "crown", "Palace", "Door", "King", "Queen", "Coding", "program",
         "Apple", "gun", "laptop", "bird", "baby", "fan"]

def labelslider():
    global count,sliderwords
    text = "Welcome to Typing Speed Checker"
    if(count >= len(text)):
        count = 0
        sliderwords = ""
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(200,labelslider)

def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timerlabelcount.configure(fg="red")
    if (timeleft > 0):
        timeleft -= 1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000,time)
    else:
        gameplaylabel.configure(text="Hit = {}  Miss = {}  Total Score = {}".format(score,miss,score-miss))
        rr = messagebox.askretrycancel("Notification", "Hit Retry button to play again")
        if(rr == True):
            score = 0
            timeleft = 60
            miss = 0
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)


def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gameplaylabel.configure(text=" ")
    if(wordEntry.get() == wordlabel["text"]):
        score += 1
        scorelabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox
######################################################################################## Root Method
root = Tk()
root.geometry("800x600+400+100")
root.configure(bg="cyan")
root.title("Typing Speed Checker")
######################################################################################## Variables
score = 0
timeleft = 60
count = 0
sliderwords = ""
miss = 0
######################################################################################## Label Method
fontlabel = Label(root, text="", font=("arial",25,"italic bold"),
                  bg="cyan", fg="red", justify="right", width=40)
fontlabel.place(x=10,y=10)
labelslider()

random.shuffle(words)
wordlabel = Label(root, text=words[0], font=("arial",40,"italic bold"),bg="cyan")
wordlabel.place(x=320,y=200)

scorelabel =Label(root, text="Your Score: ", font=("arial",25,"italic bold"), bg="cyan")
scorelabel.place(x=10,y=100)

scorelabelcount = Label(root, text=score, font=("arial",25,"italic bold"), bg="cyan", fg="blue")
scorelabelcount.place(x=30,y=160)

timerlabel = Label(root, text="Time Left:   ", font=("arial",25,"italic bold"), bg="cyan")
timerlabel.place(x=600,y=100)

timerlabelcount = Label(root, text=timeleft, font=("arial",25,"italic bold"), bg="cyan", fg="blue")
timerlabelcount.place(x=630,y=160)

gameplaylabel = Label(root, text="Type the word and press Enter button", font=("arial",25,"italic bold"),
                      bg="cyan", fg="magenta")
gameplaylabel.place(x=120,y=450)
######################################################################################## Entry Method
wordEntry = Entry(root, font=("arial",25,"italic bold"), bd=10, justify="center")
wordEntry.place(x=200,y=300)
wordEntry.focus_set()
########################################################################################
root.bind("<Return>", startGame)
root.mainloop()
