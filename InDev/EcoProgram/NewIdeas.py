# Start Imports
import time
from time import sleep
import random
from random  import randint
PROGRAMRUNNING = True

#Starter variables
COUNTRYDETERMINED = False
COUNTRYTYPE = ("") # Only purpose it serves is for me to know which type it is in the future of this program
COUNTRYDATA = [] # actually holds the data crucial for simulating the country

# Script system - in progress
# 
# UNUSED:
# # #SCRIPT SPECIFIC VARIABLES
# EPIDEMIC = False # If true, the program will run in epidemic mode.
# EPIDEMICRECOVERY = False # After the epidemic ends this activates, and enables an upturn
# EPIDEMICCOUNTDOWN = 3 # Each epidemic will last this many years, with the countdown starting after 
# #the first year
# """""
# 
def script_process(TAXINCOME,INFO,IMMIGRATION_RATE,CURRENTTAXINCOME,POPULATION,WORK_EFFICIENCY,
                   PUBLIC_SPENDING,WORKING_AGE_POPULATION,UNEMPLOYED_POPULATION,TOTAL_SALARIES_PAID,LITERACY):
    #     Script names:
    A1="NeighbourTrade1"
    A2="NeighbourTrade2"
    A3="NeighbourTrade3"
    A4="GovernmentScandal"
    B1="Epidemic"
    B2="TaxRateChange"
    B3="GoodYear"
    B4="BadYear"
    C1="Blank1"
    C2="Blank2"
    C3="Blank3"
    C4="Blank4"

#     Script types:
    PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
    SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
    UNDEFINED_SCRIPTS = [C1,C2,C3,C4]
     
#     Other script stuff:
    SCRIPT_NUMBER = random.randint(0,3)
    SCRIPTS = (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4)
    CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER]

#     Script variables:
    NEIGHBOUR1 = COUNTRYDATA[15] # Rich, high income, low pop, high education
    NEIGHBOUR2 = COUNTRYDATA[16] # Poor, low income, high pop, low education
    NEIGHBOUR3 = COUNTRYDATA[17] # Medium, medium income, medium pop, medium education

#     Start of script definition
    if "One" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME = CURRENTTAXINCOME + 100000
        IMMIGRATION_RATE += 0.05
        POPULATION += 500
        LITERACY += 0.02
        INFO = (
            "Trade Opportunity!  /"
            "Your Neighbour " + NEIGHBOUR1 + " offers a trade opportunity"
        )
        return INFO, TAXINCOME, IMMIGRATION_RATE # Added returns for related data
    if "Two" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME = CURRENTTAXINCOME + 30000
        IMMIGRATION_RATE += 0.05
        POPULATION += 4000
        LITERACY -= 0.02
        INFO = (
            "Trade Opportunity!  /"
            "Your Neighbour " + NEIGHBOUR2 + " offers a trade opportunity"
        )
        return INFO, TAXINCOME, IMMIGRATION_RATE # Added returns for related data
    if "Three" in CHOSEN_SCRIPT:
        CURRENTTAXINCOME = TAXINCOME
        TAXINCOME = CURRENTTAXINCOME + 50000
        IMMIGRATION_RATE += 0.05
        POPULATION += 2000
        LITERACY += 0.01
        INFO = (
            "Trade Opportunity!  /"
            "Your Neighbour " + NEIGHBOUR3 + " offers a trade opportunity"
        )
        return INFO, TAXINCOME, IMMIGRATION_RATE # Added returns for related data

# UNUSED:
#    if "Four" in CHOSEN_SCRIPT:
#        INFO = (
#            "Government scandal"
#            "Party popularity down by 20%"
#        )
#        ValueRandomised = randint(0, 10)
#        if ValueRandomised > 7:
#            print("Protests continue")

#     if "Five" in CHOSEN_SCRIPT:
#         INFO = ("Epidemic has broken out" +
#             "Mortality rate increases by 5% while its ongoing" +
#             "It may be wise to invest in healthcare to counteract this")
# 
#         global EPIDEMIC
#         EPIDEMIC = True                         
#         return INFO
#     if "ELECTION" in CHOSEN_SCRIPT:
#        print("Election time!/"
#            "The new prime minister is ...") # Should be integrated with political leader variable at some point
#                                            # Calculated by party popularity defined by money, nepotism whatverthefuck...
# 

#Country types and their information
# Future: RICH, POOR, ZOMBIE, APOCALYPSE, 
AMERICA = [int(50000), int(5000), float(0.6), int(20000), float(0.05), int(3000), int(500), int(15000), float(0.5),
            int(1000), int(10000), float(0.035), float(0.6), float(0.5), float(0.05), # This is country data, ends at
            #[14] which means theres 15 variables in total up to this point
            ("Canada"),("Colombia"),("Mexico")]# these are its three neighbours, ends at [17] which means
            #there are 18 variables in total up to this point
RICH = []
POOR = []

# Program loop
while PROGRAMRUNNING == True:
#The program will now begin by asking a series of questions to determine the type of country to simulate
    while COUNTRYDETERMINED == False:
        COUNTRYTYPEQUESTION1 = input("Do you want to try the default country?(Y/N)") 
        # Unsure whether to use a real country or not
        if COUNTRYTYPEQUESTION1 == ("Y"):
            COUNTRYTYPE = ("AMERICA") # This is the default country type, and will be used for testing
            COUNTRYDATA = AMERICA
            COUNTRYDETERMINED = True
            # This skips the rest of the while and chooses default as the country and starts the stimulation
        else:
            COUNTRYDETERMINED = True
            PROGRAMRUNNING = False

    AMOUNT_WRITTEN=0
    MODE = "all"
    with open("FileNumber.txt", "w+", encoding="utf-8") as fp: # This script has been edited to read from the country type
    #Then read from the list and assign that integer for the variables. Makes new country types easy, and experimenting
    # with stuff like unusual data and exponential values as well. Potential new country types will be above.
            fp.write("")
            fp.close
    YEAR = 1960
    TAXINCOME = COUNTRYDATA[0]
    POPULATION = COUNTRYDATA[1]
    WORK_EFFICIENCY = COUNTRYDATA[2]
    PUBLIC_SPENDING = COUNTRYDATA[3]
    IMMIGRATION_RATE = COUNTRYDATA[4]
    WORKING_AGE_POPULATION = COUNTRYDATA[5]
    UNEMPLOYED_POPULATION = COUNTRYDATA[6]
    TOTAL_SALARIES_PAID = COUNTRYDATA[7]
    LITERACY = COUNTRYDATA[8]
    TOTAL_WELFARE = COUNTRYDATA[9]
    GDP = COUNTRYDATA[10]
    YEARLY_MORTALITY_RATE = COUNTRYDATA[11]
    HEALTHCAREEFFICIENCY = COUNTRYDATA[12]
    ECONOMICDEVELOPMENT = COUNTRYDATA[13]
    HOMELESSRATE = COUNTRYDATA[14]
    while YEAR != 1970:
        POPULATION_START_OF_YEAR = POPULATION
        print("Year ", (YEAR))
        YEAR += 1
        #All these following calculations should be innovated in the future, but for now they are simple
        LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
        PUBLIC_SPENDING = 0.1 * GDP
        HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4)
        POPULATION += 100

        #IMMIGRATION calculation now randomly decides between up by 0.05% or down by the same.
        IMMIGRATION_RATE_CHANGE = random.random()
        if IMMIGRATION_RATE_CHANGE == 0:
            IMMIGRATION_RATE -= 0.05
        else:
            IMMIGRATION_RATE += 0.05

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
            fp.close() #run time 0.251 seconds, should be quicker, what can we
            # speed up? File system removal, on the go variable changes
        PROGRAMRUNNING = False