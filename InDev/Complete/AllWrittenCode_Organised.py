#UNKNOWN
"""
To limit randomness this could simply be changed
into an election race, so only 4 years are needed
allows the citizen simulation to be simplified
"""
"""
#This hopefully will lead to progress on either a grid based generic world game,
#or a wild west thing
#All Comments,Notes,Ideas e.t.c
# The Wild West
"""
"""
Let’s feed the numbers i have into godot and see what visuals i could get like 
houses and stuff, simulate emigration through abandoned buildings
the country is some landlocked state with a lot of nomadic movement

actually maybe it’s just a town in the wild west, with a tavern, and movement is
likely. Though if you provide the right
services there’s a chance people coming through will settle, if they’re cowboys
they’ll have specific traits and jobs
that help your town uniquely to them. These guys can settle impromptu without 
a house, but some types like accountants
will need their own space. The game should start with a group of cowboys, 
each can be assigned to any job and
although
    they’re jack of all trades there is some levity in their skills. For example
     for 5 stats there’s maximum of 4 skill 
    points up it could go down, at a chance of 1% that it could go this high, 
    for example perception 9 instead of 5 
    besides
     any other changes would take a 1% odd. So after a while of operating and 
     getting some immigrants you can build 
     specialised buildings for them. ANd start replacing cowboys with 
     profesional workers, after all not everyone wants
      a knife wielding gunslinger as their barber. The growth and birth 
      randomisation can be imported. The chances of 
      immigration and all that simulation can also be imported, to at the 
      beginning happen turn based with eventual 
      real time changing with natural changes in migration, although most 
      likely like this. You’re in the centre of 
      5 towns around you, north, south east, south west, east and west, 
      for someone from the north to go south east 
      it is very likely they will go through you, if either your area is 
      appealing enough or if it is too dangerous 
      to move through the wild west they’ll stay with you, either for a
       night or more, maybe convince them with some 
      escorts to see if you could get that towns favour.

step 1 - data based simulation of day by day changes in population, 
most likely your base population of 10 doesn’t change much. and then up to 
6 groups at most(one from each town) could possibly stay, . maximum of 24 
people let’s say. So at most your population would grow by 2.4 times base. 
To appease a town you can offer them food. One unit of food satisfies one
 person. So at most you could use up 24 units of food. How can food be obtained
 , buying from caravans, hunting, donations, random events.

Step 2 CDDA level graphics, if not DF style. The point of the game at this 
point should be. To slowly specialise into one way, in order to appease a 
specific town and guarantee survival of your town through trade incentives 
from that town for a specific good as well as many other for cheaper as well, 
e.g. food. After this you could try plundering rival towns in order to appease
 the town your favourable with.


it’s unlikely a caravan from one town should go all the way around, but if they
 do you’re the one missing out on sweet money, goods and potential loot if 
 they’re dumb enough( thievery aspect) Keep crime low, by keeping brigands 
 at bay and having a police force to keep aware of bounties by either visiting
 villages for info on criminals from either the police station, newspapers 
 from outside the towns or through gossip with citizens(3 cards each a choice
  that should be as dynamic as possible). This and attractiveness and as well
   as interesting sites(tavern, escort building). Or even bribes can guarantee 
   your town will stay alive, in the wild west

T-Tavern
H-Hotel
P-(Hitching) post
C-Camp
R-Residential (home)
C(-Commercial

So one of the first processes would be Caravan movement, it would go as follows:

(Town Name), (Town location) wants to trade with (TN), (TL). If adjacent it
 simulates it. Trade Value for TN1 + 3(they sell and buy in one turn),Trade
  value for TN2+2(they sell bormally but buy a limited amount from the caravan).

# These decisions should be based on what the caravan either specifically 
holds(Developed after it become a game) or predicted to (What the town produces
 versus how much the other town needs it) If a towns specialty is oil gathering 
 its priority to sell would be at some point 100% meaning up to 25% percent of
  its holding caravan space would be designated for it. If another town is oil 
  processing regardless of what size it has a high priority to buy this up to
   the point where it has reserves for at least 7 turns. Trade happens every 
   7 turns.

Determined:
Trade value earned is based on how much selling and buying is done. Simply that,
 no minus values for selling more than buying, simple.
Trade happens every 7 turns. They schedule imports 2 days before this? If we are
 to simulate an external economy this would be needed to ensure these towns 
 don’t die. So if we have two primary food producers, one oil producer, one 
 construction material producer, and one population producer . 


This is the order the code needs to be in, at least this early in.
	1.	movement of people in and out of town 7am
	2.	movement within town 7am
	3.	movement of people within town out of town 7am
	4.	Caravan events 7-12pm
	5.	Item gathering events 7-2pm
	6.	Town planning(building + emergency events)2-5pm
	7.	final movement out of town 2-7pm
	8.	Final movement into town 5-10pm

Chance of a caravan being caught should have a number peaking between 8pm and 
6am.  lowest between 12pm and 3pm And a static 10% chance for all other hours. 
CHance of succes should be based on each event, although some shouldn’t be all 
bad. Think oregon valley. There should be a choice to designate a patrol of 
some size to decrease chance of bad events in one or all 5 paths between your 
town and others. Sometimes you may get missions to patrol these when there’s 
rare cargo, important people or simply a relationship boost at hand.

Come back tommorow.
"""
#indevideas.py

#Simualtion choices
""".git\#Idea:: simulation choices
#   #Fantasy kinggdom (special scrripts) Check 'Simulacra' paint 3d file
#   #Greece (Troika pprogram, historical events, high score gained by
# learning a strategy to solve the crisis)
#   #United Kingdom(Long drain, freeplay essentially,
#Mainly reoccuring events. Try to avoid collapse of diplomacy and of your
# country. Strong economics and trade routes, one invisible to China +
#All commonwealth to be programmed. Need a journal for approximate trade output
# relative to GDP and/or any other country statistics
# Each starts with 3(May actually change)
# neighbours for events, trade and scripts
# 
# Greece - (Main pop 60, , secondary pop 40, tertiary pop 20)
# Need a matrix to define popularity, money donations, skill, the level of 
# their influence in % to an industry, which depending on industry influence 
# affects level based modifiers, 3 or 4 levels for each.
# TROIKA DIRECTIVES -"As the EU's biggest scapegoat, Greece and its debt
# can be annihilated, as to free the EU powers from their burden" Germany focus
# to take out Greece, Semi pre determined with these faction alignments:
# Anti EU
# America(Supports UK)
# UK(support Greece and independence blah blah bull)
# Russia(Advisor to Germany:"
#Obviously unless some under the table fun happens Russia will bend
# over the EU and have its fun", Russia gains all Black sea related land(Helps
# them mess up Ukraine later) as well as Islands(Naval stuff). They may decide
# to promise not to intervene, volunteer or invade all with separate 
#reprecussions)
# Pro EU
# Germany(Leader of EU decisions and determines EU intervention, historical
# will be an EU invasion as the AI, much costlier decisions scaling in cost
# Based on time for recovery
# Italy(Reignition of the iron pact, neutrality or invades Germany for
# Austrian land, this Austria path prevents a Greece war but is difficult for
# Italy obviously as this action is deemed nefarious by all other factions)
#Millenium dawn mod? Is there a mod that features this)
# Neutral
# France(Initial or forever?)
# Additionally each country contains one or more unique resources with their
# own modifiers based on trade influence and/or investment. The UK resource
# would be Banking and cyber security, these act as subsidiary to service
# industry, so investment in service affects it based on an equal spread
# to all other service subsidiaries, direct investment is possible into a sub,
# however this can disproportionately affect other branches, so a spread 
# approach could be better.
# Simulacra(The Castle"Security above all, condenment down to persecution")
# - (main pop 100, Secessionist possible later). This may become a hoi4 map...
# Simulacra resources are gonna be typical fantasy shit, Magic stones in the 
# small independent nation, which can use this to embargo The Castle and block
# them out of using magic. """
# 
# # next_steps.txt
# 
# #DATAINPUTTER#
# 


"""
Developing the datainputter function to a usable and eventually an advanced state akin to a simulation of Vic 2
#Immigration_percent is dependent on literacy,GDP,employment_rate (lower=high_immigration)
# total_welfare(higher better), taxes.
#In order of importance highest to lowest. With high mid and low being referred to.
#Immigrants will be defined as separate classes of high, mid, low and refugee.
#for lower class population: total welfare, literacy, taxes, employment_rate, GDP
# for middle class population: employment_rate, GDP, literacy, taxes, total welfare
# for upper class population: literacy, taxes, employment_rate, GDP, total welfare
# For immigrants the categories of desire are:
# for lower class population: employment_rate, total welfare, literacy, taxes, GDP
# for middle class population: employment_rate, employment_rate(intentional double),
# literacy, taxes, GDP,total welfare
# for upper class population: employment_rate(relative to base e.g. assume the home countries
# employment rate to be base, unless theyre 3rd country in which case a separate variable is necessary
# , 3rd countries will have a minute upper attraction. Its guiding features will be,
# the country attractiveness relevant to the home and tourist country,
# So consider what affects immigration as what is better about this country in comparison to that one,
# Ideally 3 variables will exist. Neighbour, continent, interglobal. Typed in order
# of relative immigration amounts. Even if employment is high a 3rd world country
# will only have so many people capable of purchasing VISA's etc. One change will be 
# upper populations have refugees as well as the other regions. 3rd class will have highest
# , mid will have a very small amount apart from criminal asylums. The high class
# may have more appearance in rich countries due to tax asylums and/or other fraud related 
# crimes. literacy, taxes, GDP, total welfare
# for refugee class population: employment_rate, total welfare, literacy, taxes, GDP
# employment must be more important for middle than low, welfare most for low, taxes for the rich,
#  are highest then middle and low are the same. GDP high, mid, low, lit high, mid, low.
#  For most variables, desirability is in order of which class you desire.


Additionally the following features would revolutionise the program:
Industrial performance
Residential performance
Construction index
Resource economy (Each country,city,region analysed shall be defined by three tangible resources:
Beyond which population factors in but isn't a part of. For a country like Greece it would be:
Fish? Cars? fraud?
Capital uncertainity: Similar to the evaluation of stock traders based on its performance:
    - Recession
    - Long time weak performance
    - 1.00 indicates great capital certainity, any number below is poor and has integral effects on:
        - Stock investments
        - Trade
        - Immigration
        - High wealth class spending
    
Trade - defined by random non printed events(unless printed for debugging reason to introduce:
    -Randomness
    -Replayability

Random or pre-defined or self-defined or self-defining trade acts. These will have some arbitrary
some free-from effects on public services, resource economy e.t.c. Think "Democracy 2016", HOI4
focuses. And other Paradox game idea systems
"""

"""
TKButtons.py
#Unfinished Visual Component

from tkinter import * #Standard library
from tkinter import ttk #New themed widgets, to access the themed versions:
                    #ttk.entry for example is required rather than entry
                    #As entry would give you the tk version
                    #Best advice is to prefix with ttk
from PIL import ImageTk, Image
def calculate(*args): # straightforward calculation
    try:
        value = float(population.get())
        immigration.set(int(0.05*value))
        #Multiplying and dividiing by a thousand is to prevent rounding 
        #Problems
    except ValueError:
        pass

root = Tk() # application window
root.title("Immigration Calculator") # title (duh)
myimg = ImageTk.PhotoImage(Image.open('town.png'))
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # places the frame in 
                                                    #our main applciation window
root.columnconfigure(0, weight=1) # frame fills any space resized
root.rowconfigure(0, weight=1) # frame fills any space is resized
 
population = StringVar() # Creates widget
population_entry = ttk.Entry(mainframe, width=7, textvariable=population) #
# Places feet_entry inside the parent, the content frame known as ttk.entry
#Width defines how many characters wide it should appear
population_entry.grid(column=2, row=1, sticky=(W, E))
#Defines the row and column it will be placed in. Sticky defines how it 
#should line up
immigration = StringVar() # label that display meters to calculate
ttk.Label(mainframe, textvariable=immigration).grid(column=2, row=2, sticky=(W, E))
#places the meters label
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, 
             row=3, sticky=W)

#the calculate button which defines the calculate function's action
ttk.Label(mainframe, text="population").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to immigration rate of:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="immigrants a year").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="if immigration is 0.05% a year").grid(column=3, row=3, sticky=W)
#The last 3 labels make the program easier to use and are visual


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#This puts padding around each widget to prevent them being scrunced
# #supposdely this could be bypassed by putting it into grid, but
#But this is a shortcut

population_entry.focus() # cursor starts on the entry widget
root.bind("<Return>", calculate) # if return key is pressed it calculate

root.mainloop()
#More Visual component ideas
from tkinter import *

root = Tk()
root.title('Display1')
root.geometry("600x400")

def taxrateprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "0.05")
    #this creates a new label to the GUI
    label.pack() 

def populationprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "5000")
    #this creates a new label to the GUI
    label.pack() 

button = Button(root, text="Current Tax Rate", command=taxrateprint) 
button.pack()
button2 = Button(root, text="Current Tax Rate", command=populationprint) 
button.pack()

root.mainloop()

"""
##Entranched
#Compass.py
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
#What_is_a_tranche... .py
# Entranched.
# A tranche creation and education program

import random
from random import randint
import time
from time import sleep
print("What is a tranche"
      "A tranche is a 'basket' of non physical 'credit obligations' and physical 'assets'"
      "CDO - Credit Debt Obligation, gambling on the ability of a company to pay its debt"
      "CDS - Credit Default Swap, gambling on the ability of mortgage payees not defaulting on payments, and when "
      "they do depending on your position in the tranche you may lose your position"
      "Tranches depend on ratings from ratings agencies such as 'Moodys' in order to inform investors on the safety"
      "of their investment"
      "Ratings range from FFF rating at its lowest to AAA for the best quality"
      ""
      "Default values:"
      "'Equity' tranche = 3% losses"
      "'Mezzanine' tranche = 3%-7% losses (insulated by the 'equity' tranche up to 3% losses)"
      "'Junior Senior' tranche = 7%-10% losses (insulated by 'Mezzanine' tranche up to 7% losses)"
      "'Regular Senior' tranche = 10%-15% losses (insulated by 'Junior Senior' tranche up to 10% losses"
      "'Super Senior' tranche = 15%-30% losses (insulated by 'Regular Senior' tranche up to 15% losses safest tranche)"
      ""
      "The expected tranche sizes depend on the number and timing of any future default and the expected costs of"
      "these future defaults(ie recovery rates)"
      "Pricing tranches:"
      "The premium on a tranche is the spread paid by the protection buyer that equates the expected present value of"
      "default costs to be borne by the protection seller('protection leg') to the expected present value of investing"
      "in the tranche('premium leg')"
      "(Source(Amato,Gyntelberg/BIS (2005))"
      "The value of the premium leg is present value of spread payments the protection seller receives from the "
      "protection buyer"
      "Expected present value of 'Premium leg': V(sub)prem = S*E[sigma(super)M(sub)i-1*D(0,t(sub)i)*N(t(sub)i)"
      "t being the quartely payment date M(t=t(sub)1,t(sub)2...t(sub)M"
      "D(0,t(sub)i) is the uncertain discount factor of expected future income streams"
      "Tranche premium = S"
      "The present value of the 'premium leg' is made smaller by: low premium, low recovery rate, default losses"
      "incurred early"
      "Expected present value of the 'protection leg': "
      "V(sub)prot=E[sigma(super)M(sub)i-1*D(0,t(sub)i)*(N(t(sub)i)-N(t(sub)i-1))"
      "The present value of the 'protection leg' is made smaller by: tranche size unchanged, high recovery rate,"
      "defaults occure late during the contract period "
      "'Tranche premium' : (Solve) V(sub)prem=V(sub)prot /(or just)V(sub)prem/V(sub)prot"
      ""
      "Information is based on BIS quarterly review March 2005 unless specified differently"
      "To determine S you need to know the discount factors and future tranche sizes,"
      "For more on discount factors see Rebonato (2002)"
      "For more on future tranche sizes see below:"
      "1) losses-given-default:"
      "     -Assume a constant recovery rate of 40%, 1-recovery rate is the losses given default"
      "         -The recovery rate can also be estimate from CDS spreads but in this case we use the average historical"
      "          recovery rate on senior unsecured bonds for US corporations"
      "2) number of defaults:"
      "     -Estimated directly from single-name CDS spreads, directly from equity prices(Check Moody's KMV's expected"
      "      default frequencies)"
      "         -A recovery rate assumption is neded to extract default probabilities from CDS spreads"
      "3) timing of defaults:"
      "     -Timing of defaults for the N entities over the lifetime of the contract can be calculated from a joint"
      "      default time probability distribution. This is unknown assume default times follow an N-dimensional"
      "      multivariate normal distribution, ie the so-called Gaussian copula(see Nelsen(1999), Li(2000) and"
      "      Cherubini et al(2004))"
      "         -Example:one-factor Gaussian copula model is as follows and contains a latent random variable X(sub)i"
      "         -X(sub)i=(sqroot(p))*M+(sqroot(1-0))*Z(sub)i"
      "              Assumptions/Definitions"
      "             -M is a normally distributed random variable"
      "             -Z(sub)i's are mutually uncorrelated and normally distributed random variables"
      "             -(-1<p<1) is the constant pairwise correlation between default times"
      "                 -Hull and White(2004)"
      "                 -Estimated from correlatiions of equity returns in the range 0-30%"
      "             -Identical constant pairwise default time correlations"
      "             -Normally distributed default times"
      "             -Normal joint default probability distribution"
      "         -The model above can be interpreted to mean X(sub)i is the value of assets held by entity i, entity i"
      "          defaults if its assets fall below some threshold"
      "         -This model can be assumed to be a market standard for pricing tranches and see Nelsen(1999) for more"
      "         -This model is also simple thanks to its straightforward and easy to obtain(shorten) assumptions")

#Simulate a tranche of 100 assets of MBS, CDO, bond and residential properties.

print("A tranche of 100 assets is split based on the ratio 25/25/30/20"
      "Varying in price between 80-120, 100-150, 40-100, 300-400"
      "Their probability of default will be mainly random but each has roughy 1.5% chance of failure"
      "An investment in highest tier is safest, most expensive and least return, with an inverese relationship"
      "downwards")

def _RandomSplittingTheTranche_:
      mbs = 0.25
      cdo = 0.25
      bond = 0.3
      residential = 0.2
      junkbond = 0
      percentagesizeoftranche = cdo + mbs + bond + residential
      action = 1
      while action == 1:
            trancheassets = ("MBS", "CDO", "Bond", "Residential", "Junkbond")
            whichtrancheasset = randint(0,4)
            if whichtrancheasset == 0:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        mbs += assetchange
                  else:
                        mbs -= assetchange
            if whichtrancheasset == 1:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        cdo += assetchange
                  else:
                        cdo -= assetchange
            if whichtrancheasset == 2:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        bond += assetchange
                  else:
                        bond -= assetchange
            if whichtrancheasset == 3:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        residential += assetchange
                  else:
                        residential -= assetchange
            if whichtrancheasset == 4:
                  assetchange = randint(0,100)/100
                  print(str(assetchange))
                  plusorminus= randint(0,1)
                  print(str(plusorminus))
                  if plusorminus == 0:
                        cdo -= assetchange/4
                        mbs -= assetchange/4
                        bond -= assetchange/4
                        residential -= assetchange/4
                        junkbond += assetchange
                  else:
                        if junkbond > 0:
                              junkbond -= assetchange
                              if junkbond < 0:
                                    junkbond = 0
                        else:
                              break
            time.sleep(1)
            if percentagesizeoftranche != 1:
                  print("ERROR IN PERCENTAGE SIZE OF TRANCHE, ATTEMPTING REBALANCE:")
                  time.sleep(4)
                  restorationpoints = percentagesizeoftranche-1
                  actualrecoverypoints = restorationpoints / 3
                  if actualrecoverypoints > 0:
                        cdo += actualrecoverypoints
                        mbs += actualrecoverypoints
                        residential += actualrecoverypoints
                  elif actualrecoverypoints < 0:
                        cdo -= actualrecoverypoints
                        mbs -= actualrecoverypoints
                        residential -= actualrecoverypoints
                  if percentagesizeoftranche == 1:
                        print("PERCENTAGE SIZE CORRECT, RESUMING WITH FOLLOWING")
                        print("CDO =", cdo)
                        print("MBS =", mbs)
                        print("Residential =", residential)
                        print("Junkbonds =", junkbond)
            #proportion of tranche:
            print("MBS makes up  = ", mbs, "Proportion of tranche")


pastcommentsandnotes.py

""" 
#Taken from ImportCompass.py
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
"""
"""
#DATAINPUTTER#

"""
Developing the datainputter function to a usable and eventually an advanced state akin to a simulation of Vic 2
#Immigration_percent is dependent on literacy,GDP,employment_rate (lower=high_immigration)
# total_welfare(higher better), taxes.
#In order of importance highest to lowest. With high mid and low being referred to.
#Immigrants will be defined as separate classes of high, mid, low and refugee.
#for lower class population: total welfare, literacy, taxes, employment_rate, GDP
# for middle class population: employment_rate, GDP, literacy, taxes, total welfare
# for upper class population: literacy, taxes, employment_rate, GDP, total welfare
# For immigrants the categories of desire are:
# for lower class population: employment_rate, total welfare, literacy, taxes, GDP
# for middle class population: employment_rate, employment_rate(intentional double),
# literacy, taxes, GDP,total welfare
# for upper class population: employment_rate(relative to base e.g. assume the home countries
# employment rate to be base, unless theyre 3rd country in which case a separate variable is necessary
# , 3rd countries will have a minute upper attraction. Its guiding features will be,
# the country attractiveness relevant to the home and tourist country,
# So consider what affects immigration as what is better about this country in comparison to that one,
# Ideally 3 variables will exist. Neighbour, continent, interglobal. Typed in order
# of relative immigration amounts. Even if employment is high a 3rd world country
# will only have so many people capable of purchasing VISA's etc. One change will be 
# upper populations have refugees as well as the other regions. 3rd class will have highest
# , mid will have a very small amount apart from criminal asylums. The high class
# may have more appearance in rich countries due to tax asylums and/or other fraud related 
# crimes. literacy, taxes, GDP, total welfare
# for refugee class population: employment_rate, total welfare, literacy, taxes, GDP
# employment must be more important for middle than low, welfare most for low, taxes for the rich,
#  are highest then middle and low are the same. GDP high, mid, low, lit high, mid, low.
#  For most variables, desirability is in order of which class you desire.


Additionally the following features would revolutionise the program:
Industrial performance
Residential performance
Construction index
Resource economy (Each country,city,region analysed shall be defined by three tangible resources:
Beyond which population factors in but isn't a part of. For a country like Greece it would be:
Fish? Cars? fraud?
Capital uncertainity: Similar to the evaluation of stock traders based on its performance:
    - Recession
    - Long time weak performance
    - 1.00 indicates great capital certainity, any number below is poor and has integral effects on:
        - Stock investments
        - Trade
        - Immigration
        - High wealth class spending
    
Trade - defined by random non printed events(unless printed for debugging reason to introduce:
    -Randomness
    -Replayability

Random or pre-defined or self-defined or self-defining trade acts. These will have some arbitrary
some free-from effects on public services, resource economy e.t.c. Think "Democracy 2016", HOI4
focuses. And other Paradox game idea systems


"""
Tests here in case of a change in variables:
Either Define a few names for a variable
Check which variables exist, those that don't are 
automatically removed from being written in the file and
at the bottom of the file, or when the program finishes it says
which ones were missed
"""
#OldC:
"""
Natural year by year evolution must be influenced by scripts, events so on
The random events are either in file, or out of file retrieved by open...
"""

#NewC:If the code fails, it should read out the chunk its from
#Ergo fail in Neighbour should read "Neighbours"
#OldC:
"""
All variables now equal pre determined values
equations for variables of the town equal 
the pre determined values at year 1960, in the
future they should randomise and extrapolate
past this, for now only gradual changes.

All variables are that of a small town

10 year simulation spam

no sleep function
"""
indeveconomy.py

"""
An interactive tech demo to teach economics.
"""


#Recent changes:
"""""
All variables now equal pre determined values
equations for variables of the town equal 
the pre determined values at year 1960, in the
future they should randomise and extrapolate
past this, for now only gradual changes.

All variables are that of a small town

10 year simulation spam

no sleep function
"""
import time
from time import sleep
import random
from random  import randint

#For file saving
AMOUNT_WRITTEN=0
#MODE = str(input("Input mode ")) For debugging MODE = all
MODE = "all"
#THis resets the file
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
        fp.write("")
        fp.close
#Simulation stuff
WORKING_NAME = "Simulacra" # One simulation should be based on the 
#economy of Greece before during and after the Troika program
WEEKLY_UPDATES = False
YEARLY_UPDATES = False

#Scan the variable INPUT_SCOPE before the program runs to
#INPUT_SCOPE = input("Choose either Weekly (WEEK) or Yearly (YEAR) " + For debugging it is always year based
#    "If Weekly the program runs for a year with weekly updates of 52 " +#    "If Yearly the programs runs for 20 years with yearly updates of 20 ")
INPUT_SCOPE = "YEAR"

#Simulating crime events a year, converitble to weeks if needed
if INPUT_SCOPE == "YEAR":
    CRIME = 520
elif INPUT_SCOPE == "WEEK":
    CRIME = 52

#This code generates a neighbour, stores, assigns, removes from list
NEIGHBOURLIST = ["Turkey", "Yugoslavia", "Albania", "Bulgaria", "Italy", "France", "The UK", "The USA"]
NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
NEIGHBOUR1 = 0
NEIGHBOUR2 = 0
NEIGHBOUR3 = 0
##TURN NEIGHBOUR INTO A FUNCTION THAT RETURNS NEIGHBOUR
NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOUR1 = str(STOREDNEIGHBOUR)
del NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOUR2 = STOREDNEIGHBOUR
del NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOUR3 = STOREDNEIGHBOUR
del NEIGHBOURLIST[NEIGHBOURCHOSEN]
NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))

#Natural year by year evolution must be influenced by scripts, events so on
#The random events are either in file, or out of file retrieved by open...
#The Simulation data, to be grouped in integer and decimal     
YEAR = 1960
TAXINCOME = 50000
POPULATION = 5000
WORK_EFFICIENCY = 0.6 #Based partially on: technology, education, resistance by working class
PUBLIC_SPENDING = 20000
IMMIGRATION_RATE = 0.05
WORKING_AGE_POPULATION = 3000
UNEMPLOYED_POPULATION = 500
TOTAL_SALARIES_PAID = 15000
LITERACY = 0.5
TOTAL_WELFARE = 1000
GDP = 100000
YEARLY_MORTALITY_RATE = 0.035
HEALTHCAREEFFICIENCY = 0.6
ECONOMICDEVELOPMENT = 0.5
HOMELESSRATE = 0.05

#SCRIPT SPECIFIC VARIABLES
EPIDEMIC = False # If true, the program will run in epidemic mode.
EPIDEMICRECOVERY = False # After the epidemic ends this activates, and enables an upturn
EPIDEMICCOUNTDOWN = 3 # Each epidemic will last this many years, with the countdown starting after 
#the first year
"""""
def script_process(TAXINCOME):
    A1="NeighbourTrade1"
    A2="NeighbourTrade2"
    A3="NeighbourTrade3"
    A4="GovernmentScandal"
    B1="Epidemic"
    B2="TaxRateChange"
    B3="GoodYear"
    B4="BadYear"
    PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
    SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
    #Undefined Scripts = [C1,C2,C3,C4]
    SCRIPT_NUMBER = random.randint(0,5)
    SCRIPTS = (A1,A2,A3,A4,B1,B2B3,B4)#C1,C2,C3,C4)
    CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER]
    if "One" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR1) + "offers a trade opportunity")
        return INFO
    if "Two" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR2) + "offers a trade opportunity")
        return INFO
    if "Three" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR3) + "offers a trade opportunity")    
        return INFO          
    if "Four" in CHOSEN_SCRIPT:
        INFO = ("Government scandal" +
            "Party popularity down by 20%")
        ValueRandomised = randint(0,10)
        if ValueRandomised > 7 :
            ("Protests continue")
        return INFO
    if "Five" in CHOSEN_SCRIPT:
        INFO = ("Epidemic has broken out" +
            "Mortality rate increases by 5% while its ongoing" +
            "It may be wise to invest in healthcare to counteract this")
        global EPIDEMIC
        EPIDEMIC = True                         
        return INFO
    #if "ELECTION" in CHOSEN_SCRIPT:
    #    print("Election time!/"
    #        "The new prime minister is ...") # Should be integrated with political leader variable at some point
    #                                        # Calculated by party popularity defined by money, nepotism whatverthefuck...
    #Political system in progress
    if "TAXRATECHANGE" in CHOSEN_SCRIPT:
        INFO = ("Tax Rate Change")
        TAXINCOME += TAXINCOME * 0.01
        return INFO
    if "GOODYEAR" in CHOSEN_SCRIPT:
        COUNTRYDEVELOPMENT += 0.01(for every 0.01 this increases all other variables to improve the country)   
"""
#Beginning of program load
DECIDEDPACE = False
"""
while DECIDEDPACE is False:
    PACE = str(input("Slow or Fast or rapid Pace(input 1 or 2 or 3 or info)"))
    if PACE == "info":
        print("If slow then data updates every 3 seconds"\
              "If fast then data updates every second"\
              "If rapid then data has no update" ) #For debugging
    elif PACE == "1" or "one" or "One":
        PACE = int(3)
        DECIDEDPACE = True
    elif PACE == "2" or "two" or "Two":
        PACE = int(0.5)
        DECIDEDPACE = True
    elif PACE == "3" or "three" or "Three":
        PACE = int(0)
        DECIDEDPACE = True
    #TEST 1 : PACE
    else:
        print("Pace failed")
"""

"""
Potential change
GoodYear/BadYear:
    When this function is invoked the program will randomly decide which is true, and then certain variables
    attributed will then increase or decrease.
"""
"""
def POPULATION_HIERARCHY(POPULATION):
Lower
Middle
Upper
A diagram on how they affect the government is on paper, these should dictate the variables they impact.
Hopefully this number of people in each hierachy will be dynamic, more on each individuals capabilities, than 
of the economy as a whole(quality of education, welfare etc).
A way to define certain policies would be useful, if visual easy, if written then there needs to be defined points, e.g
every 4 years a new government can be appointed, you choose the one with preferential policies, which would 
be based on what the party leans towards.
Conservative : corp tax down
Leftist : Human rights
"""
#Main portion of code
while YEAR != 1970:
    POPULATION_START_OF_YEAR = POPULATION
    print("Year ", (YEAR))
    YEAR += 1
    #All this code needs to implement gradual changes not new definitions each time
    LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
    PUBLIC_SPENDING = 0.1 * GDP
    HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4) #THis results in it being equal to 0.6 at start
    # The 1000000 is only suitable for small simulations, it will represent
    #the peak of GDP that should be attainable meaning more can be spent on healthcare
    #0.4 represents base healthcare, which at its lowest should equal this
    #in year 1 with no other changes it should equal 0.45
    #unsure code :YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION) + (0.0024 * POPULATION)) / POPULATION)
    #first bracket=Elderly Death second bracketHealth Related Deaths
    #unsure code:IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
    #POPULATION =(100 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE) For debugging pop increases by 100 each year
    POPULATION += 100
    #Bad Code : events already determined : CRIME = 0.07952 * POPULATION
    WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
    UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
    #Bad Code : just use a real equation : GDP = WORK_EFFICIENCY * (0.6 * POPULATION)
    TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
    TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
    TAXINCOME = POPULATION * 10
    CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
    #Needs to calculate tax income somehow
    """""
    #SCRIPT SPECIFIC
    These require scripts to not ruin readability of the program
    if EPIDEMIC == True:
        POPULATION  -= 50000
        GDP -= 10000000
        PUBLIC_SPENDING += 10000000
        TOTAL_WELFARE += 50000000
        EPIDEMICCOUNTDOWN -= 1
        IMMIGRATION_RATE = 0.015
        if EPIDEMICCOUNTDOWN == 0:
            EPIDEMIC = False
            EPIDEMICRECOVERY = True
            EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
    elif EPIDEMICRECOVERY == True:
        PUBLIC_SPENDING -= 10000000
        TOTAL_WELFARE -= 50000000
        EPIDEMICCOUNTDOWN -= 1
        if EPIDEMICCOUNTDOWN == 0:
            EPIDEMICRECOVERY = False
            EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
    """""
    #END OF YEAR CHECKS
    """""
    if YEAR % 2 == 0:
        script_process(TAXINCOME)
    PACEUNDECIDED = True
    while PACEUNDECIDED == True:
        if PACE == 0:
            PACEUNDECIDED = False
        else:
            time.sleep(PACE)
            PACEUNDECIDED = False
    """
    """
    if ECONOMICDEVELOPMENT > 0.5:
        IMMIGRATION_RATE += 0.01
        HOMELESSRATE -= 0.001
    """
    POPULATION_END_OF_YEAR = POPULATION
    #   File save code
    # The save to file functions are in progress, though it's possible to print all to a file,
    # comparative pairs direct to an Excel file would be easiest to recursively compare.
    with open("FileNumber.txt", "a", encoding="utf-8") as fp:
        AMOUNT_WRITTEN += 1
        fp.write(str(AMOUNT_WRITTEN))       
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = str(("The year at finish = ", YEAR))
        MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
        PO = str(("Population = ", POPULATION))
        TR = str(("Tax Income = ", (TAXINCOME)))
        SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
        WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
        FILEINPUTDETERMINED = False
        while FILEINPUTDETERMINED == False:
            if MODE == "all":
                MODE = "WYMIPOTRSALPWELP"
            if "WY" in MODE:
                fp.write(" " + WY + " " + "\n" )
            if "MI" in MODE:
                fp.write(" " + MI + " " + "\n")
            if "PO" in MODE:
                fp.write(" " + PO + " " + "\n")
            if "TR" in MODE:
                fp.write(" " + TR + " " + "\n")
            if "SALP" in MODE:
                fp.write(" " + SALP + " " + "\n")
            if "WELP" in MODE:
                fp.write(" " + WELP + " " + "\n")           
            FILEINPUTDETERMINED = True
        fp.write("\n")
        fp.close()

#Everything seems to work, time to find a gaussian or brownian simulation for population

pickascriptoutofahat

import random
from random import randint

List = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten")
scriptfromlist = randint(0, 9)
print(scriptfromlist)
print(List[scriptfromlist])

save_to_a_file.py

"""os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
DATA_INPUTTED = 0
with open("File_Number.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNT_WRITTEN = int(Content[0])
    AMOUNT_WRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNT_WRITTEN))
    fp.close()
AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
        POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = print("The year ", YEAR),
        MI = print("MIGRATION", MIGRATION),
        PO = print("POPULATION", POPULATION),
        TR = print("Tax rate", round((TAXES * 100), 2), "%"),
        MP = print("MIGRATION percent", MIGRATION_PERCENT),
        if VALUE_OF_TOWN > 1000000000:
            VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
        else:
            print("Value of the country ", int(VALUE_OF_TOWN))
        SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
        WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
        print("You increased taxes ", CHOICE1, "times.")
        TOTAL_SCORE += VALUE_OF_TOWN
    print("You changed taxes ", CHOICE1, "times.")
    if CHOICE1 > 5:
        print("Perhaps too much...")
        print(CHOICE1)
    if CHOICE2 > 5:
        print("Perhaps too little...")
        print(CHOICE2)
    print(TOTAL_SCORE)
    RoundTaxes = round((TAXES * 100), 2)
    YAR = "Final year " + str(YEAR)
    if TOTAL_SCORE>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TOTAL_SCORE)
    MAR = "MIGRATION in final year " + str(MIGRATION)
    PAR = "POPULATION in final year " + str(POPULATION)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
    VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
    TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
    TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
    TAXINC = "Tax changes " + str(CHOICE1)
# The save to file functions are in progress, though it's possible to print all to a file,
# comparative pairs direct to an Excel file would be easiest to recursively compare.
    Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
    os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
    with open(Name, 'a', encoding="utf-8") as fp:
        fp.write("\n")
        if MODE == "all":
            MODE = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in  MODE:
            with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
                tsfp.write(str(TOTLSCR))
                tsfp.close()
            with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
                trfp.write(str(TAXR))
                trfp.close()
        if 'TM' in  MODE:
            fp.write("\n")
            fp.write(str(MAR))
        if 'TP' in  MODE:
            fp.write("\n")
            fp.write(str(PAR))
        if 'TT' in  MODE:
            fp.write("\n")
            fp.write(str(TAXR))
        if 'TMP' in MODE:
            fp.write("\n")
            fp.write(str(MARPR))
        if 'TV' in  MODE:
            fp.write("\n")
            fp.write(str(VALT))
        if 'TSP' in MODE:
            fp.write("\n")
            fp.write(str(TOTLSAL))
        if 'TWP' in MODE:
            fp.write("\n")
            fp.write(str(TOTALWEL))
        if 'TINC' in    MODE:
            fp.write("\n")
            fp.write(TAXINC)
        fp.write("\n")
        fp.close()"""

scriptingpractice.py

import random
from random import randint

A1="One"
A2="Two"
A3="Three"
A4="Four"
B1="Five"
B2="Six"
B3="Seven"
B4="Eight"
C1="ELECTION"
C2="TAXRATECHANGE"
C3="INTERESTRATECHANGE"
C4="Twelve"
PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
NAMED_SCRIPTS = [C1,C2,C3,C4]
SCRIPT_NUMBER = random.randint(1,12)
SCRIPTS = (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4)
CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER-1]
if "One" in CHOSEN_SCRIPT:
    print("One  /"
          "                    ") # Description
                                  # Description part 2
if "Two" in CHOSEN_SCRIPT:
    print("Two   /"
          "                    ") # Description
                                  # Description part 2
if "Three" in CHOSEN_SCRIPT:
    print("Three   /"
          "                    ") # Description
                                  # Description part 2
if "Four" in CHOSEN_SCRIPT:
    print("Four   /"
          "                    ") # Description
                                  # Description part 2
if "Five" in CHOSEN_SCRIPT:
    print("Five   /"
          "                    ") # Description
                                  # Description part 2
if "Six" in CHOSEN_SCRIPT:
    print("Six   /"
          "                    ") # Description
                                  # Description part 2
if "Seven" in CHOSEN_SCRIPT:
    print("Seven   /"
          "                    ") # Description
                                  # Description part 2
if "Eight" in CHOSEN_SCRIPT:
    print("Eight   /"
          "                    ") # Description
                                  # Description part 2          
if "ELECTION" in CHOSEN_SCRIPT:
    print("Election time!/"
          "The new prime minister is ...") # Should be integrated with political leader variable at some point
                                           # Calculated by party popularity defined by money, nepotism whatverthefuck...
if "TAXRATECHANGE" in CHOSEN_SCRIPT:
    print("Tax Rate Change/"
          "                    ") # Description
                                  # Description part 2
if "INTERESTRATECHANGE" in CHOSEN_SCRIPT:
    print("Interest rate change/"
          "                    ") # Description
                                  # Description part 2
if "Twelve" in CHOSEN_SCRIPT:
    print("twelve/"
          "                    ") # Description
                                  # Description part 2

townimage.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter PhotoImage Demo')

        self.image = Image.open('town.png')
        self.python_image = ImageTk.PhotoImage(self.image)

        ttk.Label(self, image=self.python_image).pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()

wealthevent.py

import numpy as np
import os
import sys
TESTS= False
def WealthEvent():
    SYMBOLCHANGE = 0
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
    global PERCENTAGECHANGE
    global HOLDINGSALARY
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHANGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
                     p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
    if '1p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
    #Tests
    if TESTS == True:
        print(HOLDINGSALARY)
        print(SYMBOLCHANGE)
        print(PERCENTAGECHANGE)
class Citizen:
    def __init__(self, s):
        self.salary = s
#Showing Python the path to my code        
directory = "citizensalarystorage"
parent_dir = "C:/Users/kbudz/Documents/GitHub/Economy-Program"
path = os.path.join(parent_dir, directory)
os.chdir(path) # This code assigns the current directory to the path seen above
#Helping with organisation

#Making the program accessible with sleep, a choice of continuing the citizen simulation,
#Citizen simulation will print the amount of years of simulation, each iteration
#Is one year.It can also let you create new citizens. Each citizen group should have their own name
#e.g. Citizens
print("New Simulation (N) \n Load Simulation (L) \n Exit (E)")
CHOICE = str(input())
SIMULATIONCHOSEN = False
NUMBEROFPREVIOUSSIMULATIONS = 0
while SIMULATIONCHOSEN == False:
    if "N" in CHOICE:
         NUMBEROFPREVIOUSSIMULATIONS += 1 # amount before this one
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")
    elif "L" in CHOICE:
         FILEWRITING = str("NEWCITIZENSALARIES.txt")
    elif "E" in CHOICE:
        sys.exit()
    else:
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")

# The following code can be used to make new directories exclusively even any parent directories:
# os.mkdir(path)
P1 = Citizen(30000)
P1.salary= 30000
with open(FILEWRITING, "w+", encoding="utf-8") as NCS:
                NCS.write("")
                NCS.close()
with open("CITIZENSALARIES.txt", "r", encoding="utf-8") as fp:
        CURRENTCITIZENCOUNT = 0
        while CURRENTCITIZENCOUNT < 20:
            CITIZENID = str(("P",str(CURRENTCITIZENCOUNT)))
            CITIZENID = Citizen(fp.readline())
            #Salary change
            HOLDINGSALARY = P1.salary
            WealthEvent()
            with open("NEWCITIZENSALARIES.txt", "a+", encoding="utf-8") as NCS:
                NCS.write(str(HOLDINGSALARY))
                NCS.write("\n")
                NCS.close()
            #End of Salary change

            #Need a test to see how many citizen numbers were printed, if below a certain
            #amount, the file is discarded and the while loop ended.
            #Try (name file), except if (CITIZENCOUNT < 20)

            CURRENTCITIZENCOUNT += 1
        fp.close()

splittingthetranche.py

#Simulate losses to the economy, if not inadvertantly caused by the economy

DAY = 1
while (DAY != 365):
      DAY -= 1
      assetfailure = np.random.choice(['NOFAIL','FAIL'], 1, p =[0.98,0.02])
      if assetfailure == 'FAIL':
            assetfailed = np.random.choice(["mbs", "cdo" , "bond", "residential", "junkbond"], 1, p =[0.2,0.2,0.2,0.2,0.2])
            if assetfailed == 'mbs':
                  numbermbs -= 1
                  actualnumberofassetsintranche -= 1
            if assetfailed == 'cdo':
                  numbercdo -= 1
                  actualnumberofassetsintranche -= 1
            if assetfailed == 'bond':
                  numberbond -= 1
                  actualnumberofassetsintranche -= 1
            if assetfailed == 'residential':
                  numberresidential -= 1 
                  actualnumberofassetsintranche -= 1
            if assetfailed == 'junkbond':
                  numberjunkbond -= 1
                  actualnumberofassetsintranche -= 1

print("Number of MBS assets left over " , (numbermbs))
print("Change in MBS assets" , ((numbermbs - (mbs * 1000))/mbs*1000), "%")
print("Number of CDO assets left over " , (numbercdo))
print("Change in CDO assets" , ((numbercdo - (cdo * 1000))/cdo*1000) , "%")
print("Number of Bond assets left over " , (numberbond))
print("Change in Bond assets" , ((numberbond - (bond * 1000))/bond*1000), "%")
print("Number of Residential assets left over " , (numberresidential))
print("Change in Residential assets" , ((numberresidential - (residential * 1000))/residential*1000), "%")
print("Number of Junkbond assets left over " , (numberjunkbond))
print("Change in Junkbond assets" , ((numberjunkbond - (junkbond * 1000))/junkbond*1000) , "%")
-doesnt work, sometimes over a 100% comes out


#released program
import time
from time import sleep
import random
from random  import randint
AMOUNT_WRITTEN=0
MODE = "all"
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
        fp.write("")
        fp.close
YEAR = 1960
TAXINCOME = 50000
POPULATION = 5000
WORK_EFFICIENCY = 0.6
PUBLIC_SPENDING = 20000
IMMIGRATION_RATE = 0.05
WORKING_AGE_POPULATION = 3000
UNEMPLOYED_POPULATION = 500
TOTAL_SALARIES_PAID = 15000
LITERACY = 0.5
TOTAL_WELFARE = 1000
GDP = 100000
YEARLY_MORTALITY_RATE = 0.035
HEALTHCAREEFFICIENCY = 0.6
ECONOMICDEVELOPMENT = 0.5
HOMELESSRATE = 0.05
while YEAR != 1970:
    POPULATION_START_OF_YEAR = POPULATION
    print("Year ", (YEAR))
    YEAR += 1
    LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
    PUBLIC_SPENDING = 0.1 * GDP
    HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4)
    POPULATION += 100
    WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
    UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
    TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
    TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
    TAXINCOME = POPULATION * 10
    CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
    POPULATION_END_OF_YEAR = POPULATION
    with open("FileNumber.txt", "a", encoding="utf-8") as fp:
        AMOUNT_WRITTEN += 1
        fp.write(str(AMOUNT_WRITTEN))       
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = str(("The year at finish = ", YEAR))
        MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
        PO = str(("Population = ", POPULATION))
        TR = str(("Tax Income = ", (TAXINCOME)))
        SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
        WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
        FILEINPUTDETERMINED = False
        while FILEINPUTDETERMINED == False:
            if MODE == "all":
                MODE = "WYMIPOTRSALPWELP"
            if "WY" in MODE:
                fp.write(" " + WY + " " + "\n" )
            if "MI" in MODE:
                fp.write(" " + MI + " " + "\n")
            if "PO" in MODE:
                fp.write(" " + PO + " " + "\n")
            if "TR" in MODE:
                fp.write(" " + TR + " " + "\n")
            if "SALP" in MODE:
                fp.write(" " + SALP + " " + "\n")
            if "WELP" in MODE:
                fp.write(" " + WELP + " " + "\n")           
            FILEINPUTDETERMINED = True
        fp.write("\n")
        fp.close() #run time 0.251 seconds, should be quicker, what can we speed up? File system removal, on the go variable changes
#vat-happiness.py
#Making the program accessible with sleep, a choice of continuing the citizen simulation,
#Citizen simulation will print the amount of years of simulation, each iteration
#Is one year.It can also let you create new citizens. Each citizen group should have their own name
#e.g. Citizens
print("New Simulation (N) \n Load Simulation (L) \n Exit (E)")
CHOICE = str(input())
SIMULATIONCHOSEN = False
NUMBEROFPREVIOUSSIMULATIONS = 0
while SIMULATIONCHOSEN == False:
    if "N" in CHOICE:
         NUMBEROFPREVIOUSSIMULATIONS += 1 # amount before this one
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")
    elif "L" in CHOICE:
         FILEWRITING = str("NEWCITIZENSALARIES.txt")
    elif "E" in CHOICE:
        sys.exit()
    else:
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")

# The following code can be used to make new directories exclusively even any parent directories:
# os.mkdir(path)

#This citizen simulation should be done to simulate an average salary, average lifespan and other things
#To make it usable there will have to be a upper and lower bound based on the normal distribution of the said
#Variables

P1 = Citizen(30000)
P1.salary= 30000
with open(FILEWRITING, "w+", encoding="utf-8") as NCS:
                NCS.write("")
                NCS.close()
with open("CITIZENSALARIES.txt", "r", encoding="utf-8") as fp:
        CURRENTCITIZENCOUNT = 0
        while CURRENTCITIZENCOUNT < 20:
            CITIZENID = str(("P",str(CURRENTCITIZENCOUNT)))
            CITIZENID = Citizen(fp.readline())
            #Salary change
            HOLDINGSALARY = P1.salary
            WealthEvent()
            with open("NEWCITIZENSALARIES.txt", "a+", encoding="utf-8") as NCS:
                NCS.write(str(HOLDINGSALARY))
                NCS.write("\n")
                NCS.close()
            #End of Salary change

            #Need a test to see how many citizen numbers were printed, if below a certain
            #amount, the file is discarded and the while loop ended.
            #Try (name file), except if (CITIZENCOUNT < 20)

            CURRENTCITIZENCOUNT += 1
        fp.close()


#Next steps
#To implement fully VAT And Happiness
#add VAT to variables
#add Happiness to variables
#Create an option to introduce VAT yourself, program it so that by putting x% vat, it will
#Use a suitable amount of happiness change, and suitable change in vatincome. Search
#up how much goods a person in a country like the UK uses, another for a second class country like
#Greece, and then perhaps a 3rd class
#More range for happiness, below 60 or above 80 a bigger impact is needed on the economy
#Buying habits
#Emigration
#All of these should be negatively impacted
#VAT:HAPPINESS
#4% + 5% Happiness
#5% +- 0% Happiness
#6% -5% Happiness

#Assuming each family of the sample buys a bottle of wine once a week for a
#yea, this code shows how the amount of Income from VAT changes with changes
#to % changes in VAT

"""

Year = 2023
Month = 5
while Year != 2024 and Month != 5:
    HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier)
    TotalIncomeFromVAT += VAT * (GoodConsumptionModifier * Population)
    Month += 1
    if Month == 12:
        Year += 1
        Month = 1

HAPPINESSRESULT(HappinessModifier)
FINANCIALRETURN = ("The government imposed a " , (VAT) , "% Value Added Tax, this earned\
 them " , (TotalIncomeFromVAT) , "from the sale of wine alone")
SOCIALRETURN = ("The citizens felt " , (HappinessResult) , "With the current \
                state of affairs")
                
print(FINANCIALRETURN)
print(SOCIALRETURN)

Introduce tests per each chunk of code, e.g. setup, variable introduction, running, functions
file saving, each should have a few in a "Testing" file, but not in release to speed it up
Need to speed up the running of the code, file saving can be made optional, by using an aditional
line of options:
Release, Testing
Release runs the code and dialogue ONLY
Testing also runs the tests and saves to a file your stats.
Filesaving = false for release essentially
"""

TESTING = True
VAT = ""
Population = 5000
GoodConsumptionModifier = 52
HappinessModifier = 65
TotalIncomeFromVAT = 0

VAT = int(input("Choose 4, 5, 6 for VAT "))        
VATLoop = True
while VATLoop == True:
    if VAT == 4:#%
        HappinessModifier += 5#% happiness
        VATLoop = False
    if VAT == 5:#%
        HappinessModifier += 0#% happiness
        VATLoop = False
    if VAT == 6:#%
        HappinessModifier += -5#% happiness
        VATLoop = False
    else:
        VATLoop = False
"""
while TESTING == True:
    if VAT != int:
        #
    while VAT != int:
        VAT = int(input("Choose 4, 5, 6 for VAT"))
        continue
"""

def HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier):
    if HappinessModifier == 60:
        Population -= GoodConsumptionModifier
        HappinessModifier -= 0.5
    if HappinessModifier == 65:
        Population += GoodConsumptionModifier
        HappinessModifier += 0.5
    if HappinessModifier == 70:
        Population += GoodConsumptionModifier * 1.2
        HappinessModifier += 0.75
        
def HAPPINESSRESULT(HappinessModifier):
    global HappinessResult
    if HappinessModifier <= 50:
        HappinessResult = ("Unhappy")
    if 50 <= HappinessModifier <= 70:
        HappinessResult = ("Satisified")
    if HappinessModifier <= 50    :
        HappinessResult = ("Overjoyed")

#variabledefining.py
#Variable Defining:
#Merge these variables:
#All this code needs to implement gradual changes not new definitions each time
LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
PUBLIC_SPENDING = 0.1 * GDP
HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4) #THis results in it being equal to 0.6 at start
# The 1000000 is only suitable for small simulations, it will represent
#the peak of GDP that should be attainable meaning more can be spent on healthcare
#0.4 represents base healthcare, which at its lowest should equal this
#in year 1 with no other changes it should equal 0.45
#unsure code :YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION) + (0.0024 * POPULATION)) / POPULATION)
#first bracket=Elderly Death second bracketHealth Related Deaths
#unsure code:IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
#POPULATION =(100 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE) For debugging pop increases by 100 each year
POPULATION += 100
#Bad Code : events already determined : CRIME = 0.07952 * POPULATION
WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
#Bad Code : just use a real equation : GDP = WORK_EFFICIENCY * (0.6 * POPULATION)
TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
TAXINCOME = POPULATION * 10
CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
#Needs to calculate tax income somehow
YEAR = 1960
TAXINCOME = 50000
#TaxRate = 0.05
POPULATION = 5000
WORK_EFFICIENCY = 0.6 #Based partially on: technology, education, resistance by working class
LITERACY = 0.5
PUBLIC_SPENDING = 20000
IMMIGRATION_RATE = 0.05 #Needs to represent emigration-immigration
WORKING_AGE_POPULATION = 3000
UNEMPLOYED_POPULATION = 500
#RichPopValue = RichPopulation * 100
#WorkingPopValue = (WorkEfficiency * WorkingAgePopulation) * (24 * 7) * 350
#WorkingAgePopulation = 0.8 * Population
#UnemployedPopulation = 0.2 * Population
#RichPopulation = 0.1 * Population
TOTAL_SALARIES_PAID = 15000
#TotalSalariesPaid = WorkingAgePopulation * 400
#TotalWelfare = UnemployedPopulation * 150
#TotalScore = 90348800000
#ValueOfTown = 1129360000
TOTAL_WELFARE = 1000
GDP = 100000
YEARLY_MORTALITY_RATE = 0.035
HEALTHCAREEFFICIENCY = 0.6
ECONOMICDEVELOPMENT = 0.5
HOMELESSRATE = 0.05

#scripts.py

#Current Scripts

#Should probably convert this into a dictionary
#Each number of a x0000000 series representing something

#Base Script Process

#Base scripting process
import random
from random import randint

A1="One"
A2="Two"
A3="Three"
A4="Four"
B1="Five"
B2="Six"
B3="Seven"
B4="Eight"
C1="ELECTION"
C2="TAXRATECHANGE"
C3="INTERESTRATECHANGE"
C4="Twelve"
PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
NAMED_SCRIPTS = [C1,C2,C3,C4]
SCRIPT_NUMBER = random.randint(1,12)
SCRIPTS = (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4)
CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER-1]
if "One" in CHOSEN_SCRIPT:
    print("One  /"
          "                    ") # Description
                                  # Description part 2
if "Two" in CHOSEN_SCRIPT:
    print("Two   /"
          "                    ") # Description
                                  # Description part 2
if "Three" in CHOSEN_SCRIPT:
    print("Three   /"
          "                    ") # Description
                                  # Description part 2
if "Four" in CHOSEN_SCRIPT:
    print("Four   /"
          "                    ") # Description
                                  # Description part 2
if "Five" in CHOSEN_SCRIPT:
    print("Five   /"
          "                    ") # Description
                                  # Description part 2
if "Six" in CHOSEN_SCRIPT:
    print("Six   /"
          "                    ") # Description
                                  # Description part 2
if "Seven" in CHOSEN_SCRIPT:
    print("Seven   /"
          "                    ") # Description
                                  # Description part 2
if "Eight" in CHOSEN_SCRIPT:
    print("Eight   /"
          "                    ") # Description
                                  # Description part 2          
if "ELECTION" in CHOSEN_SCRIPT:
    print("Election time!/"
          "The new prime minister is ...") # Should be integrated with political leader variable at some point
                                           # Calculated by party popularity defined by money, nepotism whatverthefuck...
if "TAXRATECHANGE" in CHOSEN_SCRIPT:
    print("Tax Rate Change/"
          "                    ") # Description
                                  # Description part 2
if "INTERESTRATECHANGE" in CHOSEN_SCRIPT:
    print("Interest rate change/"
          "                    ") # Description
                                  # Description part 2
if "Twelve" in CHOSEN_SCRIPT:
    print("twelve/"
          "                    ") # Description
                                  # Description part 2
#Currently Written Script Process
"""
def script_process(TAXINCOME):
    A1="NeighbourTrade1"
    A2="NeighbourTrade2"
    A3="NeighbourTrade3"
    A4="GovernmentScandal"
    B1="Epidemic"
    B2="TaxRateChange"
    B3="GoodYear"
    B4="BadYear"
    PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
    SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
    #Undefined Scripts = [C1,C2,C3,C4]
    SCRIPT_NUMBER = random.randint(0,5)
    SCRIPTS = (A1,A2,A3,A4,B1,B2B3,B4)#C1,C2,C3,C4)
    CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER]
    if "One" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR1) + "offers a trade opportunity")
        return INFO
    if "Two" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR2) + "offers a trade opportunity")
        return INFO
    if "Three" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME =  CURRENTTAXINCOME + 100000
        INFO = ("Trade Opportunity!  /" #Description +
            "Your Neighbour " + (NEIGHBOUR3) + "offers a trade opportunity")    
        return INFO          
    if "Four" in CHOSEN_SCRIPT:
        INFO = ("Government scandal" +
            "Party popularity down by 20%")
        ValueRandomised = randint(0,10)
        if ValueRandomised > 7 :
            ("Protests continue")
        return INFO
    if "Five" in CHOSEN_SCRIPT:
        INFO = ("Epidemic has broken out" +
            "Mortality rate increases by 5% while its ongoing" +
            "It may be wise to invest in healthcare to counteract this")
        global EPIDEMIC
        EPIDEMIC = True                         
        return INFO
    #if "ELECTION" in CHOSEN_SCRIPT:
    #    print("Election time!/"
    #        "The new prime minister is ...") # Should be integrated with political leader variable at some point
    #                                        # Calculated by party popularity defined by money, nepotism whatverthefuck...
    #Political system in progress
    if "TAXRATECHANGE" in CHOSEN_SCRIPT:
        INFO = ("Tax Rate Change")
        TAXINCOME += TAXINCOME * 0.01
        return INFO
    if "GOODYEAR" in CHOSEN_SCRIPT:
        COUNTRYDEVELOPMENT += 0.01(for every 0.01 this increases all other variables to improve the country)   
"""

"""Add to scripts:
Potential change
GoodYear/BadYear:
    When this function is invoked the program will randomly decide which is true, and then certain variables
    attributed will then increase or decrease.
"""

#programversions.py

#Program start
ProgramVersion = str(input("Which version of the program will you access\
                   Release, or Testing?"))
#Needs to either: change where file saving so as to deactivate it
#Or WhatToWriteToFile needs to work with the option of nothing being printed
#This could also be done by only giving append privileges, and putting
#File saving in a try statement, which if failed it simply bypasses it

#programspeed.py

#Edit to make a speed variable
DECIDEDPACE = False
"""
while DECIDEDPACE is False:
    PACE = str(input("Slow or Fast or rapid Pace(input 1 or 2 or 3 or info)"))
    if PACE == "info":
        print("If slow then data updates every 3 seconds"\
              "If fast then data updates every second"\
              "If rapid then data has no update" ) #For debugging
    elif PACE == "1" or "one" or "One":
        PACE = int(3)
        DECIDEDPACE = True
    elif PACE == "2" or "two" or "Two":
        PACE = int(0.5)
        DECIDEDPACE = True
    elif PACE == "3" or "three" or "Three":
        PACE = int(0)
        DECIDEDPACE = True
    #TEST 1 : PACE
    else:
        print("Pace failed")
"""

#population_hierarchy.py

"""A way to give population more depth:
def POPULATION_HIERARCHY(POPULATION):
Lower
Middle
Upper
A diagram on how they affect the government is on paper, these should dictate the variables they impact.
Hopefully this number of people in each hierachy will be dynamic, more on each individuals capabilities, than 
of the economy as a whole(quality of education, welfare etc).
A way to define certain policies would be useful, if visual easy, if written then there needs to be defined points, e.g
every 4 years a new government can be appointed, you choose the one with preferential policies, which would 
be based on what the party leans towards.
Conservative : corp tax down
Leftist : Human rights
"""

#normalwealthhealth.py

#Simulating the wealth of citizens
import numpy as np
import os
import sys
TESTS= False
def WealthEvent():
    SYMBOLCHANGE = 0
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
    global PERCENTAGECHANGE
    global HOLDINGSALARY
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHANGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
                     p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
    if '1p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
    #Tests
    if TESTS == True:
        print(HOLDINGSALARY)
        print(SYMBOLCHANGE)
        print(PERCENTAGECHANGE)
class Citizen:
    def __init__(self, s):
        self.salary = s

#main program changes.py

#Simulating the wealth of citizens
import numpy as np
import os
import sys
TESTS= False
def WealthEvent():
    SYMBOLCHANGE = 0
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
    global PERCENTAGECHANGE
    global HOLDINGSALARY
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHANGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
                     p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
    if '1p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
    #Tests
    if TESTS == True:
        print(HOLDINGSALARY)
        print(SYMBOLCHANGE)
        print(PERCENTAGECHANGE)
class Citizen:
    def __init__(self, s):
        self.salary = s

#finishedeconomyprogram.py

#Old economy code from between 1.05 to 1.10
"""
An interactive tech demo to teach economics.
"""
#the first year
#Beginning of program load

#Main portion of code
    
#Everything seems to work, time to find a gaussian or brownian simulation for population

#filesavingefficiencyimpriovements.py

#The first file saving option is longest,
#Easiest to understand. Needs to 
#be converted to the new variables


#Another file saving version
#Archivable data for consulting of future ideas
DATA_INPUTTED=0
MODE = str(input("Input mode "))

#Tests here in case of a change in variables:
"""
Either Define a few names for a variable
Check which variables exist, those that don't are 
automatically removed from being written in the file and
at the bottom of the file, or when the program finishes it says
which ones were missed
"""
#File save code for data analysis
"""os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
DATA_INPUTTED = 0
with open("File_Number.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNT_WRITTEN = int(Content[0])
    AMOUNT_WRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNT_WRITTEN))
    fp.close()
AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
        POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = print("The year ", YEAR),
        MI = print("MIGRATION", MIGRATION),
        PO = print("POPULATION", POPULATION),
        TR = print("Tax rate", round((TAXES * 100), 2), "%"),
        MP = print("MIGRATION percent", MIGRATION_PERCENT),
        if VALUE_OF_TOWN > 1000000000:
            VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
        else:
            print("Value of the country ", int(VALUE_OF_TOWN))
        SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
        WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
        print("You increased taxes ", CHOICE1, "times.")
        TOTAL_SCORE += VALUE_OF_TOWN
    print("You changed taxes ", CHOICE1, "times.")
    if CHOICE1 > 5:
        print("Perhaps too much...")
        print(CHOICE1)
    if CHOICE2 > 5:
        print("Perhaps too little...")
        print(CHOICE2)
    print(TOTAL_SCORE)
    RoundTaxes = round((TAXES * 100), 2)
    YAR = "Final year " + str(YEAR)
    if TOTAL_SCORE>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TOTAL_SCORE)
    MAR = "MIGRATION in final year " + str(MIGRATION)
    PAR = "POPULATION in final year " + str(POPULATION)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
    VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
    TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
    TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
    TAXINC = "Tax changes " + str(CHOICE1)
# The save to file functions are in progress, though it's possible to print all to a file,
# comparative pairs direct to an Excel file would be easiest to recursively compare.
    Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
    os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
    with open(Name, 'a', encoding="utf-8") as fp:
        fp.write("\n")
        if MODE == "all":
            MODE = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in  MODE:
            with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
                tsfp.write(str(TOTLSCR))
                tsfp.close()
            with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
                trfp.write(str(TAXR))
                trfp.close()
        if 'TM' in  MODE:
            fp.write("\n")
            fp.write(str(MAR))
        if 'TP' in  MODE:
            fp.write("\n")
            fp.write(str(PAR))
        if 'TT' in  MODE:
            fp.write("\n")
            fp.write(str(TAXR))
        if 'TMP' in MODE:
            fp.write("\n")
            fp.write(str(MARPR))
        if 'TV' in  MODE:
            fp.write("\n")
            fp.write(str(VALT))
        if 'TSP' in MODE:
            fp.write("\n")
            fp.write(str(TOTLSAL))
        if 'TWP' in MODE:
            fp.write("\n")
            fp.write(str(TOTALWEL))
        if 'TINC' in    MODE:
            fp.write("\n")
            fp.write(TAXINC)
        fp.write("\n")
        fp.close()"""

#Version 2 

#Another version of file saving
"""os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
DATA_INPUTTED = 0
with open("File_Number.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNT_WRITTEN = int(Content[0])
    AMOUNT_WRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNT_WRITTEN))
    fp.close()
AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
        POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = print("The year ", YEAR),
        MI = print("MIGRATION", MIGRATION),
        PO = print("POPULATION", POPULATION),
        TR = print("Tax rate", round((TAXES * 100), 2), "%"),
        MP = print("MIGRATION percent", MIGRATION_PERCENT),
        if VALUE_OF_TOWN > 1000000000:
            VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
        else:
            print("Value of the country ", int(VALUE_OF_TOWN))
        SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
        WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
        print("You increased taxes ", CHOICE1, "times.")
        TOTAL_SCORE += VALUE_OF_TOWN
    print("You changed taxes ", CHOICE1, "times.")
    if CHOICE1 > 5:
        print("Perhaps too much...")
        print(CHOICE1)
    if CHOICE2 > 5:
        print("Perhaps too little...")
        print(CHOICE2)
    print(TOTAL_SCORE)
    RoundTaxes = round((TAXES * 100), 2)
    YAR = "Final year " + str(YEAR)
    if TOTAL_SCORE>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TOTAL_SCORE)
    MAR = "MIGRATION in final year " + str(MIGRATION)
    PAR = "POPULATION in final year " + str(POPULATION)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
    VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
    TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
    TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
    TAXINC = "Tax changes " + str(CHOICE1)
# The save to file functions are in progress, though it's possible to print all to a file,
# comparative pairs direct to an Excel file would be easiest to recursively compare.
    Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
    os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
    with open(Name, 'a', encoding="utf-8") as fp:
        fp.write("\n")
        if MODE == "all":
            MODE = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in  MODE:
            with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
                tsfp.write(str(TOTLSCR))
                tsfp.close()
            with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
                trfp.write(str(TAXR))
                trfp.close()
        if 'TM' in  MODE:
            fp.write("\n")
            fp.write(str(MAR))
        if 'TP' in  MODE:
            fp.write("\n")
            fp.write(str(PAR))
        if 'TT' in  MODE:
            fp.write("\n")
            fp.write(str(TAXR))
        if 'TMP' in MODE:
            fp.write("\n")
            fp.write(str(MARPR))
        if 'TV' in  MODE:
            fp.write("\n")
            fp.write(str(VALT))
        if 'TSP' in MODE:
            fp.write("\n")
            fp.write(str(TOTLSAL))
        if 'TWP' in MODE:
            fp.write("\n")
            fp.write(str(TOTALWEL))
        if 'TINC' in    MODE:
            fp.write("\n")
            fp.write(TAXINC)
        fp.write("\n")
        fp.close()"""

#Version 3(Release Version Saving):
"""
#Needs to be at beginning:
AMOUNT_WRITTEN=0
WhatToWriteToFile = "all"
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
        fp.write("")
        fp.close

#Needs to be within the while loop of the program
    POPULATION_END_OF_YEAR = POPULATION
    #   File save code
    # The save to file functions are in progress, though it's possible to print all to a file,
    # comparative pairs direct to an Excel file would be easiest to recursively compare.
    with open("FileNumber.txt", "a", encoding="utf-8") as fp:
        AMOUNT_WRITTEN += 1
        fp.write(str(AMOUNT_WRITTEN))       
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = str(("The year at finish = ", YEAR))
        MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
        PO = str(("Population = ", POPULATION))
        TR = str(("Tax Income = ", (TAXINCOME)))
        SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
        WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
        FILEINPUTDETERMINED = False
        while FILEINPUTDETERMINED == False:
            if MODE == "all":
                MODE = "WYMIPOTRSALPWELP"
            if "WY" in MODE:
                fp.write(" " + WY + " " + "\n" )
            if "MI" in MODE:
                fp.write(" " + MI + " " + "\n")
            if "PO" in MODE:
                fp.write(" " + PO + " " + "\n")
            if "TR" in MODE:
                fp.write(" " + TR + " " + "\n")
            if "SALP" in MODE:
                fp.write(" " + SALP + " " + "\n")
            if "WELP" in MODE:
                fp.write(" " + WELP + " " + "\n")           
            FILEINPUTDETERMINED = True
        fp.write("\n")
        fp.close()
    with open("FileNumber.txt", "a", encoding="utf-8") as fp:
        AMOUNT_WRITTEN += 1
        fp.write(str(AMOUNT_WRITTEN))       
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = str(("The year at finish = ", YEAR))
        MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
        PO = str(("Population = ", POPULATION))
        TR = str(("Tax Income = ", (TAXINCOME)))
        SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
        WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
        #New Code:
        FILEINPUTDETERMINED = False
        #^^^^^^^^^^^^^^^^^^^^^^^^^^
        #Separate file saving from main code completely. Or the same way it is.
        while FILEINPUTDETERMINED == False:
            if WhatToWriteToFile == "":
                FILEINPUTDETERMINED = True
            if WhatToWriteToFile == "all":
                WhatToWriteToFile = "WYMIPOTRSALPWELP"
            if "WY" in WhatToWriteToFile:
                fp.write(" " + WY + " " + "\n" )
            if "MI" in WhatToWriteToFile:
                fp.write(" " + MI + " " + "\n")
            if "PO" in WhatToWriteToFile:
                fp.write(" " + PO + " " + "\n")
            if "TR" in WhatToWriteToFile:
                fp.write(" " + TR + " " + "\n")
            if "SALP" in WhatToWriteToFile:
                fp.write(" " + SALP + " " + "\n")
            if "WELP" in WhatToWriteToFile:
                fp.write(" " + WELP + " " + "\n")           
            FILEINPUTDETERMINED = True
        fp.write("\n")

"""
#externaleconomy.py
#For simulating the economy around the simulation
PERIOD = ("a")
TRADERS = randint(2,5) # For a random market x there will exist 2 to 5 traders who have an interest in it:
#Shorting it or investing in it may be decided later, this is a visual template.
COMMODITIES = randint(2,20) # For a random market x there exists 2 to 20 commodities that can be interacted with.
def TIME():
    CURRENTTIME = 0
    for i in PERIOD:
        CURRENTTIME += 1

#epidemic.py
EPIDEMIC = False # If true, the program will run in epidemic mode.
EPIDEMICRECOVERY = False # After the epidemic ends this activates, and enables an upturn
EPIDEMICCOUNTDOWN = 3 # Each epidemic will last this many years, with the countdown starting after 
#NewC:^^Ideally this should be simplified, perhaps as an object with 3 properties that could be read
#Simultaneously.
#one way to implement epidemic, this should act as a template for what scripts
#Should be, in terms of their impact on the simulation
#These require scripts to not ruin readability of the program

#Variable Declarations:
POPULATION = 0
GDP = 0
PUBLIC_SPENDING = 0
TOTAL_WELFARE = 0

def __BEGINNINGVARIABLES__():
    global POPULATION, GDP, PUBLIC_SPENDING, TOTAL_WELFARE

#PRSV (PRE-SCRIPT-VARIABLES):
if EPIDEMIC == True:
    #COT Variables (CHANGE-OVER-TIME)
    POPULATION  -= 50000
    GDP -= 10000000
    PUBLIC_SPENDING += 10000000
    TOTAL_WELFARE += 50000000
    EPIDEMICCOUNTDOWN -= 1
    #COS Variables (CONSTANT)
    IMMIGRATION_RATE = 0.015
    #CHE Variables (CHECK)
    if EPIDEMICCOUNTDOWN == 0:
        EPIDEMIC = False
        EPIDEMICRECOVERY = True
        EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
    
#POSV (POST-SCRIPT-VARIABLES):
if EPIDEMICRECOVERY == True:
    PUBLIC_SPENDING -= 10000000
    TOTAL_WELFARE -= 50000000
    EPIDEMICCOUNTDOWN -= 1
elif EPIDEMICCOUNTDOWN == 0:
    EPIDEMICRECOVERY = False
    EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery

#EPIDEMIC CODE PRE SIMPLIFCATION^

###Visual code



##Visual From archive
#drawing.txt
Drawing commands


• goto, x, y, width, color
• circle, radius, width, color
• beginfill, color
• endfill
• penup
• pendown

Drawing code:
1 beginfill, black
2 circle, 20, 1, black
3 endfill
4 penup
5 goto, 120, 0, 1, black
6 pendown
7 beginfill, black
8 circle, 20, 1, black
9 endfill
10 penup
11 goto, 150, 40, 1, black
12 pendown
13 beginfill, yellow
14 goto, -30, 40, 1, black
15 goto, -30, 70, 1, black
16 goto, 60, 70, 1, black
17 goto, 60, 100, 1, black
18 goto, 90, 100, 1, black
19 goto, 115, 70, 1, black
20 goto, 150, 70, 1, black
21 goto, 150, 40, 1, black
22 endfill


A program to read the above lines from a file line by line
1 # This imports the turtle graphics module.
2 import turtle
3
4 # The main function is where the main code of the program is written.
5 def main():
6 # This line reads a line of input from the user.
7 filename = input("Please enter drawing filename: ")
8
9 # Create a Turtle Graphics window to draw in.
10 t = turtle.Turtle()
11 # The screen is used at the end of the program.
12 screen = t.getscreen()
13
14 # The next line opens the file for "r" or reading. "w" would open it for
15 # writing, and "a" would open the file to append to it (i.e. add to the
16 # end). In this program we are only interested in reading the file.
17 file = open(filename, "r")
18
19 # The following for loop reads the lines of the file, one at a time
20 # and executes the body of the loop once for each line of the file.
21 for line in file:
22
23 # The strip method strips off the newline character at the end of the line
24 # and any blanks that might be at the beginning or end of the line.
25 text = line.strip()
26
27 # The following line splits the text variable into its pieces.
28 # For instance, if text contained "goto, 10, 20, 1, black" then
29 # commandList will be equal to ["goto
30 # splitting text.
31 commandList = text.split(",")
32
33 # get the drawing command
34 command = commandList[0]
35
36 if command == "goto":
37 # Writing float(commandList[1]) makes a float object out of the
38 # string found in commandList[1]. You can do simila  cvax r conversion
39 # between types for int objects.
40 x = float(commandList[1])
41 y = float(commandList[2])
42 width = float(commandList[3])
43 color = commandList[4].strip()
44 t.width(width)
45 t.pencolor(color)
46 t.goto(x,y)
47 elif command == "circle":
48 radius = float(commandList[1])
49 width = float(commandList[2])
50 color = commandList[3].strip()
51 t.width(width)
52 t.pencolor(color)
53 t.circle(radius)
54 elif command == "beginfill":
55 color = commandList[1].strip()
56 t.fillcolor(color)
57 t.begin_fill()
58 elif command == "endfill":
59 t.end_fill()
60 elif command == "penup":
61 t.penup()
62 elif command == "pendown":
63 t.pendown()
64 else:
65 print("Unknown command found in file:",command)
66
67 #close the file
68 file.close()
69
70 #hide the turtle that we used to draw the picture.
71 t.ht()
72
73 # This causes the program to hold the turtle graphics window open
74 # until the mouse is clicked.
75 screen.exitonclick()
76 print("Program Execution Completed.")
77
78
79 # This code calls the main function to get everything started.
80 if __name__ == "__main__":
81 main()

#magicoperators.py
Method Defintion Operator Description
__add__(self,y) x+y The addition of two objects. The type of x determines which add
operator is called.
__contains__(self,y) y in x When x is a collection you can test to see if y is in it.
__eq__(self,y) x == y Returns True or False depending on the values of x and y.
__ge__(self,y) x >= y Returns True or False depending on the values of x and y.
__getitem__(self,y) x[y] Returns the item at the yth position in x.
__gt__(self,y) x>y Returns True or False depending on the values of x and y.
__hash__(self) hash(x) Returns an integral value for x.
__int__(self) int(x) Returns an integer representation of x.
__iter__(self) for v in x Returns an iterator object for the sequence x.
__le__(self,y) x <= y Returns True or False depending on the values of x and y.
__len__(self) len(x) Returns the size of x where x has some length attribute.
__lt__(self,y) x<y Returns True or False depending on the values of x and y.
__mod__(self,y) x%y Returns the value of x modulo y. This is the remainder of x/y.
__mul__(self,y) x*y Returns the product of x and y.
__ne__(self,y) x != y Returns True or False depending on the values of x and y.
__neg__(self) -x Returns the unary negation of x.

__repr__(self) repr(x) Returns a string version of x suitable to be evaluated by the eval
function.
#Necessary for re-evaluation by the computer

__setitem__(self,i,y) x[i] = y Sets the item at the ith position in x to y.
__str__(self) str(x) Return a string representation of x suitable for user-level interaction.
__sub__(self,y) x-y The difference of two objects.

#UITEMPLATE.PY

###NoteCompilation

goals.txt
Goals for this program:
Your success in the simulation is based on your total score as well as your final year score
Do better in these than in a simulation with no changes added, and you will be a winner
The only variable that needs changing should be the OS directory. Usually a subfolder exists
below the economy folder but my understanding of GitHub prevents me from doing this.
Any questions should be directed to my GitHub project. Constructive criticism is appreciated
especially from a data analysis standpoint as that is the direction this project is going towards
The average score for the game is equal to playing it with no tax tampering whatsoever
This is equal to:TOTAL_SCORE = 90348800000 VALUE_OF_TOWN = 1129360000

#improvements needed.txt
"""
Quicker File Saving
Block of variable defining
Chunk defining using notes
"""

#Averageeconomy
Year = 1960
Choice = 0
Choice1 = 0
Choice2 = 0
MigrationPercent = 0.03
Taxes = 0.05
Population = 425467 # Far too extreme a 10 times increase is far too much
WorkEfficiency = 0.6
PublicSpending = 13414 * Population
Migration = 1200
WorkingAgePopulation = 0.8 * Population
UnemployedPopulation = 0.2 * Population
RichPopulation = 0.1 * Population
RichPopValue = RichPopulation * 100
WorkingPopValue = (WorkEfficiency * WorkingAgePopulation) * (24 * 7) * 350
TotalSalariesPaid = WorkingAgePopulation * 400
TotalWelfare = UnemployedPopulation * 150
TotalScore = 90348800000
ValueOfTown = 1129360000

#Economyui.py

from tkinter import * #Standard library
from tkinter import ttk #New themed widgets, to access the themed versions:
                    #ttk.entry for example is required rather than entry
                    #As entry would give you the tk version
                    #Best advice is to prefix with ttk
from PIL import ImageTk, Image
def calculate(*args): # straightforward calculation
    try:
        value = float(population.get())
        immigration.set(int(0.05*value))
        #Multiplying and dividiing by a thousand is to prevent rounding 
        #Problems
    except ValueError:
        pass

root = Tk() # application window
root.title("Immigration Calculator") # title (duh)
myimg = ImageTk.PhotoImage(Image.open('town.png'))
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # places the frame in 
                                                    #our main applciation window
root.columnconfigure(0, weight=1) # frame fills any space resized
root.rowconfigure(0, weight=1) # frame fills any space is resized
 
population = StringVar() # Creates widget
population_entry = ttk.Entry(mainframe, width=7, textvariable=population) #
# Places feet_entry inside the parent, the content frame known as ttk.entry
#Width defines how many characters wide it should appear
population_entry.grid(column=2, row=1, sticky=(W, E))
#Defines the row and column it will be placed in. Sticky defines how it 
#should line up
immigration = StringVar() # label that display meters to calculate
ttk.Label(mainframe, textvariable=immigration).grid(column=2, row=2, sticky=(W, E))
#places the meters label
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, 
             row=3, sticky=W)

#the calculate button which defines the calculate function's action
ttk.Label(mainframe, text="population").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to immigration rate of:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="immigrants a year").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="if immigration is 0.05% a year").grid(column=3, row=3, sticky=W)
#The last 3 labels make the program easier to use and are visual


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#This puts padding around each widget to prevent them being scrunced
# #supposdely this could be bypassed by putting it into grid, but
#But this is a shortcut

population_entry.focus() # cursor starts on the entry widget
root.bind("<Return>", calculate) # if return key is pressed it calculate

root.mainloop()

#Economyuiinprogress.py

from tkinter import *

root = Tk()
root.title('Display1')
root.geometry("600x400")

def taxrateprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "0.05")
    #this creates a new label to the GUI
    label.pack() 

def populationprint():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "5000")
    #this creates a new label to the GUI
    label.pack() 

button = Button(root, text="Current Tax Rate", command=taxrateprint) 
button.pack()
button2 = Button(root, text="Current Tax Rate", command=populationprint) 
button.pack()

root.mainloop()

#file_save.py

#Archivable data for consulting of future ideas
DATA_INPUTTED=0
MODE = str(input("Input mode "))

#File save code for data analysis
"""os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
DATA_INPUTTED = 0
with open("File_Number.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNT_WRITTEN = int(Content[0])
    AMOUNT_WRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNT_WRITTEN))
    fp.close()
AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
        POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
        POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
        /POPULATION_START_OF_YEAR)
        WY = print("The year ", YEAR),
        MI = print("MIGRATION", MIGRATION),
        PO = print("POPULATION", POPULATION),
        TR = print("Tax rate", round((TAXES * 100), 2), "%"),
        MP = print("MIGRATION percent", MIGRATION_PERCENT),
        if VALUE_OF_TOWN > 1000000000:
            VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
        else:
            print("Value of the country ", int(VALUE_OF_TOWN))
        SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
        WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
        print("You increased taxes ", CHOICE1, "times.")
        TOTAL_SCORE += VALUE_OF_TOWN
    print("You changed taxes ", CHOICE1, "times.")
    if CHOICE1 > 5:
        print("Perhaps too much...")
        print(CHOICE1)
    if CHOICE2 > 5:
        print("Perhaps too little...")
        print(CHOICE2)
    print(TOTAL_SCORE)
    RoundTaxes = round((TAXES * 100), 2)
    YAR = "Final year " + str(YEAR)
    if TOTAL_SCORE>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TOTAL_SCORE)
    MAR = "MIGRATION in final year " + str(MIGRATION)
    PAR = "POPULATION in final year " + str(POPULATION)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
    VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
    TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
    TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
    TAXINC = "Tax changes " + str(CHOICE1)
# The save to file functions are in progress, though it's possible to print all to a file,
# comparative pairs direct to an Excel file would be easiest to recursively compare.
    Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
    os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
    with open(Name, 'a', encoding="utf-8") as fp:
        fp.write("\n")
        if MODE == "all":
            MODE = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in  MODE:
            with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
                tsfp.write(str(TOTLSCR))
                tsfp.close()
            with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
                trfp.write(str(TAXR))
                trfp.close()
        if 'TM' in  MODE:
            fp.write("\n")
            fp.write(str(MAR))
        if 'TP' in  MODE:
            fp.write("\n")
            fp.write(str(PAR))
        if 'TT' in  MODE:
            fp.write("\n")
            fp.write(str(TAXR))
        if 'TMP' in MODE:
            fp.write("\n")
            fp.write(str(MARPR))
        if 'TV' in  MODE:
            fp.write("\n")
            fp.write(str(VALT))
        if 'TSP' in MODE:
            fp.write("\n")
            fp.write(str(TOTLSAL))
        if 'TWP' in MODE:
            fp.write("\n")
            fp.write(str(TOTALWEL))
        if 'TINC' in    MODE:
            fp.write("\n")
            fp.write(TAXINC)
        fp.write("\n")
        fp.close()"""




###Archived


"""
Method Defintion Operator Description
__add__(self,y) x+y The addition of two objects. The type of x determines which add
operator is called.
__contains__(self,y) y in x When x is a collection you can test to see if y is in it.
__eq__(self,y) x == y Returns True or False depending on the values of x and y.
__ge__(self,y) x >= y Returns True or False depending on the values of x and y.
__getitem__(self,y) x[y] Returns the item at the yth position in x.
__gt__(self,y) x>y Returns True or False depending on the values of x and y.
__hash__(self) hash(x) Returns an integral value for x.
__int__(self) int(x) Returns an integer representation of x.
__iter__(self) for v in x Returns an iterator object for the sequence x.
__le__(self,y) x <= y Returns True or False depending on the values of x and y.
__len__(self) len(x) Returns the size of x where x has some length attribute.
__lt__(self,y) x<y Returns True or False depending on the values of x and y.
__mod__(self,y) x%y Returns the value of x modulo y. This is the remainder of x/y.
__mul__(self,y) x*y Returns the product of x and y.
__ne__(self,y) x != y Returns True or False depending on the values of x and y.
__neg__(self) -x Returns the unary negation of x.
__repr__(self) repr(x) Returns a string version of x suitable to be evaluated by the eval
function.
#Necessary for re-evaluation by the computer
__setitem__(self,i,y) x[i] = y Sets the item at the ith position in x to y.
__str__(self) str(x) Return a string representation of x suitable for user-level interaction.
__sub__(self,y) x-y The difference of two objects.
"""

"""
AGE = 0
Height = 0
def Citizen(AGE,HEIGHT)
TOTALCITIZENS[]
CITIZENSGENERATED = 0
while CITIZENSGENERATED < 10:
    CITIZENSGENERATED
"""

#Goal: Simulate an economy
# Need:
#POP Simulation
# -Migration
# -Growth
# -age
# -physical properties
# -behaviours
#Market simulation
# -Good production
# -Price of goods
# -Accessibility
#Credit simulation
# -Citizen loans
# -Business loans
# -Foreign loans
# -Nation loans
#Bank simulation 
# -behavioural Actions(interest rates)
# -service actions(loan limits)
#Stock simulation
# -CDS, MBS, MBO e.t.c (1/2)
#Risk Based Investments
#IPO's
#Swaps
#Real estate simulation
# -Acquisition
# -Inheritance
#House simulation
# -Rental
# -Ownership
# 
# 
# Note Alamanac
""" POP Simulation """
""" A nation is nothing without its people """
# Migration #
# 
# Growth #
# 
# Age #
# 
# Physical Properties #
# 
# Behaviours #
# 
""" Market Simulation """
""" """
# Good Production #
#
# Price Of Goods #
#
# Accessibility #
#
""" Credit Simulation """
""" """
# Citizen Loans #
#
# Business Loans #
#
# Foreign Loans # 
#
# Nation Loans #
""" Bank Simulation """
""" """
# Behavioural Actions #
"""Interest rate adjustment:
                            """
"""Loan Limit Adjustment
                            """
# Service Actions #
"""Expansion"""
"""Acquisition"""
"""Diversification"""
"""Introduction"""
"""Investment"""
# Stock simulation ""
""" Risk Based Investments """
""" IPO's """
""" Swaps """
"""CDS, MBS, MBO e.t.c"""
#Real estate simulation
""" Acquisition """
""" Inheritance """
#House simulation
""" Rental """
""" Ownership """