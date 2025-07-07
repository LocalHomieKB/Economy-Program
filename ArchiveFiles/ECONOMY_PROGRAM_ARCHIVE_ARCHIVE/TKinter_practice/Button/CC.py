#Command connects the action and the application
#When a user presses the button, the script provided
#By the option is evaluated by the interpreter
action = ttk.Button(root, text="Action", default="active", command=myaction)
root.bind('<Return>', lambda e: action.invoke())

#Note the use of a callback, this is more convnient than
#Repeat instructions. It shortens code, and it allows
#changes at one point without having to double check
#its other iterations

#Use <Return> or <Key-Return>
# to invoke the action or <Key-Escape> to
#Cancel. or <KP_Enter> to active button and <command-,)
#to close or cancel