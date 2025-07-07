#The first example is displaying a gif on file in disk:
# 
# Create an image object:
#image = PhotoImage(file='myimage.gif')
# Tell the label to use the object via image configuration:
#label['image'] = image

#Displaying texts and images at once by using <compound>:
#<none> #display only image
# # <text> or <textvariable> # display text specified if no image present
# # <text> #text only
# # <image> #image only
# # <center> #text in center of image
# # <top> #image above text
# # <left> #left
# # <bottom> #below
# <right> #right
# 
# also
# from PIL import ImageTk, Image
#myimg = ImageTk.PhotoImage(Image.open('myimage.png'))
# #A more advanced and compatible with more file types version
from PIL import ImageTk, Image
myimg = ImageTk.PhotoImage(Image.open('town.png'))