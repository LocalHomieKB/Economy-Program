from tkinter import * #Standard library
from tkinter import ttk #New themed widgets, to access the themed versions:
                    #ttk.entry for example is required rather than entry
                    #As entry would give you the tk version
                    #Best advice is to prefix with ttk
                    # Change movingpiece1 into the independent variable
                    #   e.g. population
                    # Change movingpiece2 into the dependent variable
                    #   e.g. immigration if population is chosen
MOVINGPIECE1=1
MOVINGPIECE2=2
def calculate(*args): # straightforward calculation
    try:
        value = float(MOVINGPIECE1.get())
        MOVINGPIECE2.set(int(0.05*value)) #Set to the value the independent
        #variable is changed to. e.g. immigration of 5% multiplied by population
        # and gives the calculate value
        #Multiplying and dividiing by a thousand is to prevent rounding 
        #Problems
    except ValueError:
        pass

root = Tk() # application window
root.title("MOVINGPIECE2 Calculator") # title (duh)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # places the frame in 
                                                    #our main applciation window
root.columnconfigure(0, weight=1) # frame fills any space resized
root.rowconfigure(0, weight=1) # frame fills any space is resized
 
MOVINGPIECE1 = StringVar() # Creates widget
MOVINGPIECE1_entry = ttk.Entry(mainframe, width=7, textvariable=MOVINGPIECE1) #
# Places feet_entry inside the parent, the content frame known as ttk.entry
#Width defines how many characters wide it should appear
MOVINGPIECE1_entry.grid(column=2, row=1, sticky=(W, E))
#Defines the row and column it will be placed in. Sticky defines how it 
#should line up
MOVINGPIECE2 = StringVar() # label that display meters to calculate
ttk.Label(mainframe, textvariable=MOVINGPIECE2).grid(column=2, row=2, sticky=(W, E))
#places the meters label
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, 
             row=3, sticky=W)
#the calculate button which defines the calculate function's action
ttk.Label(mainframe, text="MOVINGPIECE1").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to MOVINGPIECE2 rate of:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="immigrants a year").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="if MOVINGPIECE2 is 0.05% a year").grid(column=3, row=3, sticky=W) 
#^ EXTRA LABEL FOR CLARIFICATION
# For more labels change <row> in label into the next number available
#The last 3 labels make the program easier to use and are visual

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#This puts padding around each widget to prevent them being scrunced
# #supposdely this could be bypassed by putting it into grid, but
#But this is a shortcut

MOVINGPIECE1_entry.focus() # cursor starts on the entry widget
root.bind("<Return>", calculate) # if return key is pressed it calculate

root.mainloop()