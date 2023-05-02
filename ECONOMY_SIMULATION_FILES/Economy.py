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
#    "If Weekly the program runs for a year with weekly updates of 52 " +
#    "If Yearly the programs runs for 20 years with yearly updates of 20 ")
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