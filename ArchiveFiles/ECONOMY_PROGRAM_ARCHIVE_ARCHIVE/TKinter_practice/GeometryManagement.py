#Grid is the most useful,
#by specifying the column and row and how they align

#Geometry management in TK relies on master and slave widget
#Master is toplevel, i contains slaves. A geo manager takes control of 
#The master and decides where the slaves will be displayed
#Master and teacher, slave and child are interchangeable.
#Apart from in backward compatibility 

#The manager has an algorithm calculating the space a slave is allocated
#It does this by the slave saying its natural size. The slave is 
#Responsible for rendering itself within that rectangle

#Some other geometry managers are pack, place, canvas, text