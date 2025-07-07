#Entry lacks a command option to invoke a callback wheneevr the entry is changed.
# To watch for changes you have to watch for changes through the linked variable.
# Check "validation"
# 
def it_has_been_written(*args):
    ...
username.trace_add("write", it_has_been_written)
#Alongside trace_add commands such as trace_remove and trace_info exist, as
# well as multiple callbacks being possible
# 
# Something that may be important to note:
# Tkinter allows you to watch for changes on a StringVar 
#(or any subclass of Variable). Both the older and newer tracing tools
# are a very thin (and not terribly Pythonic) front end to Tcl's trace command.