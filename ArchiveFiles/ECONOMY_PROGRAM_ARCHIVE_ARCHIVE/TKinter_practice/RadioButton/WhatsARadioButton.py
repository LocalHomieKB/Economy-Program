#A radiobutton is a widget that lets you choose
# between several mutually exclusive choices.
# 
# They are lkmitied to more than two
# options unlike a chekcbuttonb. But
# Are most appropriate for 3-5 options
# 
# They are always used together in a set


#To create Radiobuttons:
# Use ttk.Radiobutton as shown below:
phone = StringVar()
home = ttk.Radiobutton(parent, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(parent, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(parent, text='Mobile', variable=phone, value='cell')



#RadioButtons only possess one value button. Unlike checkbuttons which possesso
#on and off values
# Same linked variable but a different value. Whence a variable holds the matching
# value, the radiobutton will visually indicayed it is selected. 
#If it doenst. The radiiutton will be unselected
# If th3e linked varaible doesnt exist or you dont specify one with
# <variable> then it will display as "tristate" or indeterminate.
# 
# Check this using the alternate state flag