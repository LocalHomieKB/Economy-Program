#Creating a danger frame. One of many styles that change:
# -Appearance
# OR
# -Behaviour
# 
# Operatonal example of a "Danger" frame:
s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, 
relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()
#This would creatE red background and a raised border.
# 
# Additional notes:
# This change is noticeable between tkinter and TTk as in the former
# You had many individual options for appearances e.t.c. Now you have 
# Styles. Simpler yes but less customisable