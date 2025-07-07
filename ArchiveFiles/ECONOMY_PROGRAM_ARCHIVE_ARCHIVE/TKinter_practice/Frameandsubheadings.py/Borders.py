#A border can be used to visually separate it from surroundings
# For example it may look "sunken" or "raise"
# 
# #To make it look sunken:
# 
# To do this, you need to set the borderwidth 
# configuration option (which defaults to 0, i.e., no border)
#  and the relief option, which specifies the visual appearance
#   of the border. 
#Thiscan be one of: flat (default),raised, sunken, solid, ridge, or groove.
# Operational example:
frame['borderwidth'] = 2
frame['relief'] = 'sunken'