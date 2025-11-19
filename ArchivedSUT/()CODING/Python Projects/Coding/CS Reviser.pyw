import pickle
from tkinter import *
from tkinter import ttk
import random
import csv

 
window = Tk()
window.title("Welcome to CS Reviser")

s = ttk.Style()
s.configure('TNotebook.Tab', font=('Arial','18') )


lblTitle = Label(window, text="CS Reviser",font=("Arial Bold", 50))
lblTitle.grid(column=0, row=0,sticky="WE")

scoreframe = Frame(window, relief=FLAT, bd=1)
scoreframe.grid(column=0,row=1,sticky="WE")

scorelbl = Label(scoreframe, text="Score", font=("Arial",16,"italic"))
scorelbl.grid(column=0,row=0,sticky="E")

scorenum = Label(scoreframe, text="0", font=("Arial",16,"italic"))
scorenum.grid(column=1,row=0,sticky="E")

scoreframe.columnconfigure(0, weight=1)

section = {}

#pickle_in = open("terms.pkl","rb")
#section = pickle.load(pickle_in)
def clean(definition):
    if not definition[0].isalpha():
        definition = definition[1:]
    if not definition[-1].isalpha():
        definition = definition[:-1]
    
    return definition

with open('questions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:                
        if row['Spec'] + "~" + row['Section'] in section:
            section[row['Spec']+"~"+row['Section']][row['Term']] = clean(row['Definition'])
        else:
            section[row['Spec']+"~"+row['Section']] = {}
            section[row['Spec']+"~"+row['Section']][row['Term']] = clean(row['Definition'])


tabs = {}

tab_control = ttk.Notebook(window)

def getAnswer():
    lbl = tab_control.tab(tab_control.select(), "text")
    s = lbl+"~"+tabs[lbl][1]["text"]
    #print("section",s)
    question = tabs[lbl][2]["text"]
    #print("question",question)
    for k in list(section[s].keys()):
        if section[s][k] == question:
            return k

def hint():
    answer = getAnswer()
    lbl = tab_control.tab(tab_control.select(), "text")
    s = lbl+"~"+tabs[lbl][1]["text"]    

    #print(tabs[lbl][4]["text"])
    pointsavail = int(tabs[lbl][4]["text"].split(' ', 1)[0])

    if pointsavail > 0:
        #print("points avaialble",pointsavail)
        tabs[lbl][5].delete(0, END)
        pointsavail-=1
        tabs[lbl][4]["text"] = str(pointsavail)+" points avaiable"

        difference = len(answer) - pointsavail
        tabs[lbl][5].insert(0,answer[0:difference])
        #print("points avaialble",pointsavail-1)

def check():
    answer = getAnswer()
    lbl = tab_control.tab(tab_control.select(), "text")
    s = lbl+"~"+tabs[lbl][1]["text"]
    if tabs[lbl][5].get().upper() == answer.upper():
        #correct
        tabs[lbl][5].delete(0, END)
        #add to score
        scorenum["text"] = str(int(scorenum["text"])+ int(tabs[lbl][4]["text"].split(' ', 1)[0]))

        #change hint
        rndkey = random.choice(list(section[s].keys()))
        tabs[lbl][2]["text"] = section[s][rndkey]
        
        
        tabs[lbl][3]["text"] = "Answer is "+str(len(getAnswer()))+" characters long"
        tabs[lbl][4]["text"] = str(len(getAnswer()))+" points avaiable"        
        pass
    else:
        #incorrect
        pass
            
            

sections = list(section.keys())
for s in sections:
    snum = s.split("~")[0]
    stxt = s.split("~")[1]

    tabs[snum] = []
    tabs[snum].append(ttk.Frame(tab_control))
    tab_control.add(tabs[snum][0], text=snum)

    lblDefTitle = Label(tabs[snum][0],text=stxt,font=('Arial','28'))
    lblDefTitle.grid(column=0,row=0,sticky="WE",columnspan=2)
    tabs[snum].append(lblDefTitle)

    rndkey = random.choice(list(section[s].keys()))

    lblQ = Message(tabs[snum][0],text=section[s][rndkey],font=('Arial','14'),width=400)
    lblQ.grid(column=0,row=1,sticky="WE",columnspan=2)
    tabs[snum].append(lblQ)

    lblAnswer = Label(tabs[snum][0],text="Answer:",font=('Arial','22'))
    lblAnswer.grid(column=0,row=2,sticky="WE",columnspan=2)

    lblAnswerLen = Label(tabs[snum][0],text="Answer is "+str(len(rndkey))+" characters long",font=('Arial','12'))
    lblAnswerLen.grid(column=0,row=3,sticky="WE",columnspan=2)
    tabs[snum].append(lblAnswerLen)

    lblPointsAvail = Label(tabs[snum][0],text=str(len(rndkey))+" points avaiable",font=('Arial','12'))
    lblPointsAvail.grid(column=0,row=4,sticky="WE",columnspan=2)
    tabs[snum].append(lblPointsAvail)

    entA = Entry(tabs[snum][0],font=('Arial','14'))
    entA.grid(column=0,row=5,sticky="WE",columnspan=2)
    tabs[snum].append(entA)    

    btnHint = Button(tabs[snum][0],font=('Arial','14'),command=hint,text="Reveal A Letter")
    btnHint.grid(column=0,row=6,sticky="WE")

    btnCheck = Button(tabs[snum][0],font=('Arial','14'),command=check,text="Check Your Answer")
    btnCheck.grid(column=1,row=6,sticky="WE")

    tabs[snum][0].columnconfigure(0,weight=1)
    tabs[snum][0].columnconfigure(1,weight=1)
    #tabs[snum].columnconfigure(1,weight=1)
    #root.columnconfigure(1,weight=2)
    
tab_control.grid(column=0,row=2,sticky="WE",columnspan=2)
window.columnconfigure(0,weight=1)


window.mainloop()

#print(section)
#for k in list(section.keys()):
    #print("###############################",k)
    #for sk in list(section[k].keys()):
        #print (sk,section[k][sk])
        #print(section[k][sk])
