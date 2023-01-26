#The variable option links a variable to the
#Widgets current value. Variable is updated whenever
#The widget is toggled. 1 when checked, 0 when not.
#The <onvalue> and <offvalue> options allow modification of this
#The program must be initialised to the appropriate starti-
#-ng value as it is not automatically set

#Without an onvalue or offvalue the checkbutton
#is put into tristate mode. Checkbox might display a
#single dash instead of being empty or holding a
#checkmark. Internally the state flag "alternate" is set
#,Which you can inspect using the "instate" method

check.instate(['alternate'])

#A fun fact:
#StringVar can be used to hold strings, in addition
#to this <BooleanVar>, <IntVar>, <DoubleVar> are used
#for bool,int and float respectively.