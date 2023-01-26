#A button is either normal or disabled
#If a command is not applicable(at any
# point in time),
#The button will be disabled
#All widgets maintain an internal state
#Of binary flags. Each can be
#Disabled and their commands are:
b.state(['disabled'])          # set the disabled flag
b.state(['!disabled'])         # clear the disabled flag
b.instate(['disabled'])        # true if disabled, else false
b.instate(['!disabled'])       # true if not disabled, else false
b.instate(['!disabled'], cmd)  # execute 'cmd' if not disabled
T#he full list of state flags available to themed widgets is:
#active, disabled, focus, pressed, selected, background, readonly, alternate, and invalid.