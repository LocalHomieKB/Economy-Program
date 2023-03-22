#This is the file for Entranched display, the program being called compass as a source of directio to trading
#I Nee dthe following bittons for literal data interpretation:
#Display button with plain colour as background
#Display button for title
#Display button for Tranche proportion and the whole process essentially viewable from the display, errors shown,
#proportion difference shown through colours similar to how a stock changes.
#Once finished the square goes gray and proportions stay still until one default.
#Time button showing date going in days active after proportion finished
#default button showing chance increasing, resetting and increasing as default occurs.
#investment window allowing alteration to original bet on the CDO, decreasing in danger, increase in safety presumably.
#Many CDOs should be available at once, a window on the left that hides and reappears when selected over. Initially one
#available, expands with a use of money as well as capital allocation ratio (tbc)
#Size of inital investment available after inital CDO is completed, either defaulted fully or investment exit, or sold
#on, if owned, although this hould be available after inital investment (tc), more expensive (tbc)
#Button list for semidefined automation, at _% default : _action_
#Victoria like balance level button
#Random influxes of cash from investors, better return history more likely

#----

#Scrap everythin year by year simulation in hourlyvisu increments, status of balance, returns, consistency and following
#nvestor objectives is necessary to determine working the year after.
#Bankruptcy = loss
#Stagnant = small influx at first, two years in a row is a loss.
#5% increase small win, no influx but more lenient objectives. This will combine with next year performance
#Lets make this a semi idle game, limit transactions at first then introduce as to not disturb the natural
#balance of the game
#Make a fun visual display of the tranche, essentially square segments showing what the CDO is made of.
#Either sell CDO individually, realistic and more attention requiring, or as a part of a trade including, property
#(cash), an additional ABS, and it can also determine the quality of it.

#link to image file inspiration made by myself, hopefully python is capable of this otherwise unity may have to be used,
#Altohugh its not out of question to use it. Check "Compass early design image" for more information on current ideas.


#Following is some code from Chichilnisky(?) and their short selling manual textbook, hopefully
#This will be useful to define the general market environment that the business can exist inside of and
#Conduct its business in

import random
from random import randint
PERIOD = ("a")
TRADERS = randint(2,5) # For a random market x there will exist 2 to 5 traders who have an interest in it:
#Shorting it or investing in it may be decided later, this is a visual template.
COMMODITIES = randint(2,20) # For a random market x there exists 2 to 20 commodities that can be interacted with.
def TIME():
    CURRENTTIME = 0
    for i in PERIOD:
        CURRENTTIME += 1
