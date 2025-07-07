#For decorative or explanatory purposes this is ideal
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

#results content displays the new value of the variable
# 
# <get> reads current value
# <set> writes current value
#
# Not sure why get exists tbh...