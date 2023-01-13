from tkinter import *

root = Tk()
root.title('Display1')
root.geometry("600x400")

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "0.05")
    #this creates a new label to the GUI
    label.pack() 

button = Button(root, text="Current Tax Rate", command=printSomething) 
button.pack()

root.mainloop()
