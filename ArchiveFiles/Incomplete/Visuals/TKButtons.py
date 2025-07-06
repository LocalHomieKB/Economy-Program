#Unfinished Visual Component
"""
from tkinter import * #Standard library
from tkinter import ttk #New themed widgets, to access the themed versions:
                    #ttk.entry for example is required rather than entry
                    #As entry would give you the tk version
                    #Best advice is to prefix with ttk
from PIL import ImageTk, Image
def calculate(*args): # straightforward calculation
    try:
        value = float(population.get())
        immigration.set(int(0.05*value))
        #Multiplying and dividiing by a thousand is to prevent rounding 
        #Problems
    except ValueError:
        pass

root = Tk() # application window
root.title("Immigration Calculator") # title (duh)
myimg = ImageTk.PhotoImage(Image.open('town.png'))
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # places the frame in 
                                                    #our main applciation window
root.columnconfigure(0, weight=1) # frame fills any space resized
root.rowconfigure(0, weight=1) # frame fills any space is resized
 
population = StringVar() # Creates widget
population_entry = ttk.Entry(mainframe, width=7, textvariable=population) #
# Places feet_entry inside the parent, the content frame known as ttk.entry
#Width defines how many characters wide it should appear
population_entry.grid(column=2, row=1, sticky=(W, E))
#Defines the row and column it will be placed in. Sticky defines how it 
#should line up
immigration = StringVar() # label that display meters to calculate
ttk.Label(mainframe, textvariable=immigration).grid(column=2, row=2, sticky=(W, E))
#places the meters label
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, 
             row=3, sticky=W)

#the calculate button which defines the calculate function's action
ttk.Label(mainframe, text="population").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to immigration rate of:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="immigrants a year").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="if immigration is 0.05% a year").grid(column=3, row=3, sticky=W)
#The last 3 labels make the program easier to use and are visual


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#This puts padding around each widget to prevent them being scrunced
# #supposdely this could be bypassed by putting it into grid, but
#But this is a shortcut

population_entry.focus() # cursor starts on the entry widget
root.bind("<Return>", calculate) # if return key is pressed it calculate

root.mainloop()
#More Visual component ideas
from tkinter import *

root = Tk()
root.title('Display1')
root.geometry("600x400")

def taxrateprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "0.05")
    #this creates a new label to the GUI
    label.pack() 

def populationprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "5000")
    #this creates a new label to the GUI
    label.pack() 

button = Button(root, text="Current Tax Rate", command=taxrateprint) 
button.pack()
button2 = Button(root, text="Current Tax Rate", command=populationprint) 
button.pack()

root.mainloop()

"""