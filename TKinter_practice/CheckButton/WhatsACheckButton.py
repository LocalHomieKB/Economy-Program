#A regular button with an additional ability to hold
#a binary value of some kind, also known as a "toggle".

#Checkbutton widgets are frquently used to allow users
#To turn an option on or off

#You create them with the following example code
#You include contents and behvaiour at the same time
measureSystem = StringVar()
check = ttk.Checkbutton(parent, text='Use Metric',
	    command=metricChanged, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')

#The display options are as usual:
#text, textvariable, image, and compound
#Command-command to be called when toggled
#Invoke-Executes the same command
#state and instate-allows you to manipulatethe disabled
#state flag, enabling or disabling the checkbutton

