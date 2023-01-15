from tkinter import * #Standard library
from tkinter import ttk #New themed widgets, to access the themed versions:
                    #ttk.entry for example is required rather than entry
                    #As entry would give you the tk version
                    #Best advice is to prefix with ttk

def calculate(*args): # straightforward calculation
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        #Multiplying and dividiing by a thousand is to prevent rounding 
        #Problems
    except ValueError:
        pass

root = Tk() # application window
root.title("Feet to Meters") # title (duh)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # places the frame in 
                                                    #our main applciation window
root.columnconfigure(0, weight=1) # frame fills any space resized
root.rowconfigure(0, weight=1) # frame fills any space is resized
 
feet = StringVar() # Creates widget
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) #
# Places feet_entry inside the parent, the content frame known as ttk.entry
#Width defines how many characters wide it should appear
feet_entry.grid(column=2, row=1, sticky=(W, E))
#Defines the row and column it will be placed in. Sticky defines how it 
#should line up
meters = StringVar() # label that display meters to calculate
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#places the meters label
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, 
             row=3, sticky=W)
#the calculate button which defines the calculate function's action
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#The last 3 labels make the program easier to use and are visual

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#This puts padding around each widget to prevent them being scrunced
# #supposdely this could be bypassed by putting it into grid, but
#But this is a shortcut

feet_entry.focus() # cursor starts on the entry widget
root.bind("<Return>", calculate) # if return key is pressed it calculate

root.mainloop()