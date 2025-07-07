#Ide3ntical to chedck cand radiobuttons entry also has a value associayed with it
#It is accessible through the textvariable config option

#Unlike various buttons an image or text must have a separate label to identify
# them.
# 
# One can obtain the value of the entry widget using only the get method.
# This is easier as it allows you to skip the linked variable. Delete and insert
# methods let you change the contents.
# 
print('current value is %s' % name.get())
name.delete(0,'end')          # delete between two indices, 0-based
name.insert(0, 'your name')   # insert new text at a given index