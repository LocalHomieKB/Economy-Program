#Current Scripts

#Should probably convert this into a dictionary
#Each number of a x0000000 series representing something

#Base Script Process

#Base scripting process
import random
from random import randint

##i000 = Script Category (Economy,Military)
##Xi00 = Script
##X0i0 = Variation of the Script
##X00i = Variation on the Variation
### Depending on the script there may be 81 versions of a single script
### This gives opportunity to make vague scripts which then specify
### and specify further to make use,
### e.g. Tax change could become defined with two more modifiers, happiness^
### From religous parties due to an Strip club tax(with other modifiers
### of relevance to this action), and the last one could perhaps be a time limit
### Considering on the things of action in these scripts, Time, Impact, Duration
### It may be worthwile to expand the amount of numbers used. Need to make a 
### function to peruse through this, first either the furthest left and across
### 
### If a script appears as follows: "A4"
### Script category A which arbitrarily in this case is Action is read, by
### by the program reading "A" and finding out in our scripts this means
### Action. Then it reads "4" and so it searches for the fourth script in Action
### Typically the program would read further but in this case it may be better
### to have each script have X000, rather than X0 and have it search for an
### empty case. This way if 0 is read it ends the search and uses the default
### variable.
A1="One"
A2="Two"
A3="Three"
A4="Four"
A5="Five"
A6="Six"
B1="Seven"
B2="Eight"
B3="Nine"
B4="Ten"
B5="Eleven"
B6="Twelve"
C1="Thirteen"
C2="Fourteen"
C3="Fifteen"
C4="Sixteen"
C5="Seventeen"
C6="Eighteen"
SCRIPTLIST1 = [A1,A2,A3,A4,A5,A6] #PRE_DEFINED
SCRIPTLIST2 = [B1,B2,B3,B4,B5,B6] #SEMI_PRE_DEFINED_SCRIPTS
SCRIPTLIST3 = [C1,C2,C3,C4,C5,C6] #NAMED_SCRIPTS
SCRIPT_NUMBER = random.randint(1,18)
SCRIPTS = (A1,A2,A3,A4,A5,A6,B1,B2,B3,B4,B5,B6,C1,C2,C3,C4,C5,C6)
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
if "Nine" in CHOSEN_SCRIPT:
    print("Nine    /"
          "                    ") # Description
                                  # Description part 2
if "Ten" in CHOSEN_SCRIPT:
    print("Ten     /"
          "                    ") # Description
                                  # Description part 2
if "Eleven" in CHOSEN_SCRIPT:
    print("Eleven  /"
          "                    ") # Description
                                  # Description part 2
if "Twelve" in CHOSEN_SCRIPT:
    print("Twelve  /"
          "                    ") # Description
                                  # Description part 2
if "Thirteen" in CHOSEN_SCRIPT:
    print("Thirteen  /"
          "                    ") # Description
                                  # Description part 2
if "Fourteen" in CHOSEN_SCRIPT:
    print("Fourteen  /"
          "                    ") # Description
                                  # Description part 2                                
if "Fifteen" in CHOSEN_SCRIPT:
    print("Fifteen   /"
          "                    ") # Description
                                  # Description part 2
if "Sixteen" in CHOSEN_SCRIPT:
    print("Sixteen   /"
          "                    ") # Description
                                  # Description part 2
if "Seventeen" in CHOSEN_SCRIPT:
    print("Seventeen /"
          "                    ") # Description
                                  # Description part 2
if "Eighteen" in CHOSEN_SCRIPT:
    print("Eighteen  /"
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