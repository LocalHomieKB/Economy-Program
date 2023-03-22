#Entry is a signle line t3ext field. For typing in string values.
# 
# Created using ttk.entry as showm below:
# 
username = StringVar()
name = ttk.Entry(parent, textvariable=username)

#The only noticeable config option is width, allowing you to 
# determien the length of entry

#One thing that may be missing is the scrolling option as the text
# exceeds the screen width of the textbox