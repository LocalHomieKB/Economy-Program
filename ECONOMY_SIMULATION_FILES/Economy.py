"""
An interactive tech demo to teach economics.
"""

import time
from time import sleep
import random
from random  import randint

WORKING_NAME = "Simulacra" # One simulation should be based on the economy of Greece before during and after the Troika program
POPULATION = 5000
WEEKLY_UPDATES = False
YEARLY_UPDATES = False

#Scan the variable INPUT_SCOPE before the program runs to
def SCOPE(INPUT_SCOPE):
    INPUT_SCOPE = input("Choose either Weekly (WEEK) or Yearly (YEAR)"\
    "If Weekly the program runs for a year with weekly updates of 52"\
    "If Yearly the programs runs for 20 years with yearly updates of 20")

def CRIME(CRIME):
    if SCOPE == "YEAR":
        CRIME = 520
    elif SCOPE == "WEEK":
        CRIME = 52 # criminal events a year, converitble to weeks if needed

def NEIGHBOURMAKER(NEIGHBOUR1, NEIGHBOUR2, NEIGHBOUR3):
    NEIGHBOURLIST = ("Turkey", "Yugoslavia", "Albania", "Bulgaria", "Italy"/
    "France", "The UK", "The USA")
    NEIGHBOURLISTAMOUNT = 0
    NEIGHBOUR1 = 0
    NEIGHBOUR2 = 0
    NEIGHBOUR3 = 0
    STOREDNEIGHBOUR = str(NEIGHBOURLIST[randint(0,NEIGHBOURLISTAMOUNT)])
    NEIGHBOUR1 = str(STOREDNEIGHBOUR)
    NEIGHBOURLIST.remove(STOREDNEIGHBOUR)
    STOREDNEIGHBOUR = str(NEIGHBOURLIST[randint(0,NEIGHBOURLISTAMOUNT)])
    NEIGHBOUR2 = str(STOREDNEIGHBOUR)
    NEIGHBOURLIST.remove(STOREDNEIGHBOUR)
    STOREDNEIGHBOUR = str(NEIGHBOURLIST[randint(0,NEIGHBOURLISTAMOUNT)])
    NEIGHBOUR3 = str(STOREDNEIGHBOUR)
    NEIGHBOURLIST.remove(STOREDNEIGHBOUR)
    #This code generates a neighbour, stores, assigns, removes from list

def main(TAXES,POPULATION,WORK_EFFICIENCY,PUBLIC_SPENDING,
            IMMIGRATION_RATE,WORKING_AGE_POPULATION,UNEMPLOYED_POPULATION,
            TOTAL_SALARIES_PAID,TOTAL_WELFARE,YEAR,CRIME,LITERACY,GDP,YEARLY_MORTALITY_RATE,
            ASSETS, HEALTHCARE):
    #Natural year by year evolution must be influenced by scripts, events so on
    #The random events are either in file, or out of file retrieved by open...
    YEAR = 0
    TAXES = 0
    POPULATION = 0
    WORK_EFFICIENCY = 0
    LITERACY = 0
    while YEAR<2020 or KeyboardInterrupt:
        print("Year ", (YEAR))
        YEAR += 1
        LITERACY += TOTAL_WELFARE * 0.001 - LITERACY * 0.01
        PUBLIC_SPENDING = 0.4 * GDP
        HEALTHCARE = (1000 * PUBLIC_SPENDING * 1)
        YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION) + (0.0024 * POPULATION)) / POPULATION)
        #first bracket=Elderly Death second bracketHealth Related Deaths
        IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
        POPULATION =(1000 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE)
        CRIME = 0.07952 * POPULATION
        WORKING_AGE_POPULATION = 0.8 * POPULATION
        GDP = WORK_EFFICIENCY * (0.6 * POPULATION) + ASSETS
        TOTAL_SALARIES_PAID = POPULATION * 0.6 * 400
        TOTAL_WELFARE = UNEMPLOYED_POPULATION * 150
        if time % 2 == 0:
            script_process()
        time.sleep(PACE)
    print(TOTAL_SALARIES_PAID)
    print(WORKING_AGE_POPULATION)
    print(TAXES)
    
        
<<<<<<< HEAD
def script_process(NEIGHBOUR1, NEIGHBOUR2, NEIGHBOUR3):
    A1="One"
=======
def script_process():
    A1="Epidemic"
>>>>>>> bdf50dca8dd8b4c8994ddb0865ad1513b20503ff
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
<<<<<<< HEAD
        print("Trade Opportunity!  /" #Description
            "Your Neighbour " + (NEIGHBOUR1) + "offers a trade opportunity")
            # ^ Description part 2                 
    if "Two" in CHOSEN_SCRIPT:
        print("Trade Opportunity!   /"# Description
            "Your Neighbour " + (NEIGHBOUR2) + "offers a trade opportunity") # 
            #^Description part 2
                                    
=======
        print("One  /"
            "Epidemic has broken out"
            "Mortality rate increases by 5% while its ongoing"
            "It may be wise to invest in healthcare to counteract this")
    if "Two" in CHOSEN_SCRIPT:
        print("Two   "
            "Government scandal"
            "Party popularity down by 20%")
        ValueRandomised = randint(0,10)
        if ValueRandomised > 0.7 :
            ("Protests continue"/
            "Rebellion time?")
>>>>>>> bdf50dca8dd8b4c8994ddb0865ad1513b20503ff
    if "Three" in CHOSEN_SCRIPT:
        print("Trade Opportunity   /"# Description
            "Your Neighbour " + (NEIGHBOUR3) + "offers a trade opportunity") # 
            #Description part 2
                                    
    if "Four" in CHOSEN_SCRIPT:
        print("Four   /"            # Description
            "                    ") # Description part 2
                                    
    if "Five" in CHOSEN_SCRIPT:
        print("Five   /"        # Description
            "                    ") # Description part 2
                                    
    if "Six" in CHOSEN_SCRIPT:
        print("Six   /"         # Description
            "                    ") # Description part 2
                                    
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
        TAXES += 0.1                            # Description part 2
    if "INTERESTRATECHANGE" in CHOSEN_SCRIPT:
        print("Interest rate change/"
            "                    ") # Description
                                    # Description part 2
    if "Twelve" in CHOSEN_SCRIPT:
        print("twelve/"
            "                    ") # Description
                                    # Description part 2
#Beginning of program load
DECIDEDPACE = False
while DECIDEDPACE is False:
    PACE = input("Slow or Fast or rapid Pace(input 1 or 2 or 3 or info)")
    if PACE == "info":
        print("If slow then data updates every 3 seconds"\
              "If fast then data updates every 0.5 seco1nds"\
              "If rapid then data has no update" )
    else:
        PACE = int(PACE)
        DECIDEDPACE = True

NEIGHBOURMAKER()

if __name__ == "__main__":
    main(YEAR = 1960,
    TAXES = 0.05,
    POPULATION = 67000000,
    WORK_EFFICIENCY = 0.6,
    LITERACY = 0.8)


#Idea:: simulation choices
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
# them out of using magic. 