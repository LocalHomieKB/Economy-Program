"""

So the code can be ordered as so:
UTILITY, POPULATION SPECIFIC, ECONOMY SPECIFIC, SCRIPTING, EXTERNAL ENVIRONMENT SPECIFIC
Brothel/Food economy should both exist based on these, with lower amounts you could flesh out charactrs

# #Natural year by year evolution must be influenced by scripts, events so on
# #The random events are either in file, or out of file retrieved by open...
# #The Simulation data, to be grouped in integer and decimal     
# YEAR = 1960
# TAXINCOME = 50000
# POPULATION = 5000
# WORK_EFFICIENCY = 0.6 #Based partially on: technology, education, resistance by working class
# PUBLIC_SPENDING = 20000
# IMMIGRATION_RATE = 0.05
# WORKING_AGE_POPULATION = 3000
# UNEMPLOYED_POPULATION = 500
# TOTAL_SALARIES_PAID = 15000
# LITERACY = 0.5
# TOTAL_WELFARE = 1000
# GDP = 100000
# YEARLY_MORTALITY_RATE = 0.035
# HEALTHCAREEFFICIENCY = 0.6
# ECONOMICDEVELOPMENT = 0.5
# HOMELESSRATE = 0.05

# #This code generates a neighbour, stores, assigns, removes from list
# NEIGHBOURLIST = ["Turkey", "Yugoslavia", "Albania", "Bulgaria", "Italy", "France", "The UK", "The USA"]
# NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
# NEIGHBOUR1 = 0
# NEIGHBOUR2 = 0
# NEIGHBOUR3 = 0
# ##TURN NEIGHBOUR INTO A FUNCTION THAT RETURNS NEIGHBOUR
# NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
# STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOUR1 = str(STOREDNEIGHBOUR)
# del NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
# NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
# STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOUR2 = STOREDNEIGHBOUR
# del NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
# NEIGHBOURCHOSEN = randint(0,NEIGHBOURLISTAMOUNT-1)
# STOREDNEIGHBOUR = NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOUR3 = STOREDNEIGHBOUR
# del NEIGHBOURLIST[NEIGHBOURCHOSEN]
# NEIGHBOURLISTAMOUNT = int(len(NEIGHBOURLIST))
# 
# Additionally the following features would revolutionise the program:
# Industrial performance
# Residential performance
# Construction index
# Resource economy (Each country,city,region analysed shall be defined by three tangible resources:
# Beyond which population factors in but isn't a part of. For a country like Greece it would be:
# Fish? Cars? fraud?
# Capital uncertainity: Similar to the evaluation of stock traders based on its performance:
#     - Recession
#     - Long time weak performance
#     - 1.00 indicates great capital certainity, any number below is poor and has integral effects on:
#         - Stock investments
#         - Trade
#         - Immigration
#         - High wealth class spending
    
# Trade - defined by random non printed events(unless printed for debugging reason to introduce:
#     -Randomness
#     -Replayability

# Random or pre-defined or self-defined or self-defining trade acts. These will have some arbitrary
# some free-from effects on public services, resource economy e.t.c. Think "Democracy 2016", HOI4
focuses. And other Paradox game idea systems

# #SCRIPT SPECIFIC VARIABLES
# EPIDEMIC = False # If true, the program will run in epidemic mode.
# EPIDEMICRECOVERY = False # After the epidemic ends this activates, and enables an upturn
# EPIDEMICCOUNTDOWN = 3 # Each epidemic will last this many years, with the countdown starting after 
# #the first year
# """""
# def script_process(TAXINCOME):
#     A1="NeighbourTrade1"
#     A2="NeighbourTrade2"
#     A3="NeighbourTrade3"
#     A4="GovernmentScandal"
#     B1="Epidemic"
#     B2="TaxRateChange"
#     B3="GoodYear"
#     B4="BadYear"
#     PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
#     SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
#     #Undefined Scripts = [C1,C2,C3,C4]
#     SCRIPT_NUMBER = random.randint(0,5)
#     SCRIPTS = (A1,A2,A3,A4,B1,B2B3,B4)#C1,C2,C3,C4)
#     CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER]
#     if "One" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR1) + "offers a trade opportunity")
#         return INFO
#     if "Two" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR2) + "offers a trade opportunity")
#         return INFO
#     if "Three" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR3) + "offers a trade opportunity")    
#         return INFO          
#     if "Four" in CHOSEN_SCRIPT:
#         INFO = ("Government scandal" +
#             "Party popularity down by 20%")
#         ValueRandomised = randint(0,10)
#         if ValueRandomised > 7 :
#             ("Protests continue")
#         return INFO
#     if "Five" in CHOSEN_SCRIPT:
#         INFO = ("Epidemic has broken out" +
#             "Mortality rate increases by 5% while its ongoing" +
#             "It may be wise to invest in healthcare to counteract this")
#         global EPIDEMIC
#         EPIDEMIC = True                         
#         return INFO
#     #if "ELECTION" in CHOSEN_SCRIPT:
#     #    print("Election time!/"
#     #        "The new prime minister is ...") # Should be integrated with political leader variable at some point
#     #                                        # Calculated by party popularity defined by money, nepotism whatverthefuck...
#     #Political system in progress
#     if "TAXRATECHANGE" in CHOSEN_SCRIPT:
#         INFO = ("Tax Rate Change")
#         TAXINCOME += TAXINCOME * 0.01
#         return INFO
#     if "GOODYEAR" in CHOSEN_SCRIPT:
#         COUNTRYDEVELOPMENT += 0.01(for every 0.01 this increases all other variables to improve the country)   
#
# #Simulating crime events a year, converitble to weeks if needed
# if INPUT_SCOPE == "YEAR":
#     CRIME = 520
# elif INPUT_SCOPE == "WEEK":
#     CRIME = 52
"""
Epidemic event
For now until a full scripting system exists an epidemic could be a random luck or a predefined event for a certain week

# #epidemic.py
# EPIDEMIC = False # If true, the program will run in epidemic mode.
# EPIDEMICRECOVERY = False # After the epidemic ends this activates, and enables an upturn
# EPIDEMICCOUNTDOWN = 3 # Each epidemic will last this many years, with the countdown starting after 
# #NewC:^^Ideally this should be simplified, perhaps as an object with 3 properties that could be read
# #Simultaneously.
# #one way to implement epidemic, this should act as a template for what scripts
# #Should be, in terms of their impact on the simulation
# #These require scripts to not ruin readability of the program

# #Variable Declarations:
# POPULATION = 0
# GDP = 0
# PUBLIC_SPENDING = 0
# TOTAL_WELFARE = 0

# def __BEGINNINGVARIABLES__():
#     global POPULATION, GDP, PUBLIC_SPENDING, TOTAL_WELFARE

# #PRSV (PRE-SCRIPT-VARIABLES):
# if EPIDEMIC == True:
#     #COT Variables (CHANGE-OVER-TIME)
#     POPULATION  -= 50000
#     GDP -= 10000000
#     PUBLIC_SPENDING += 10000000
#     TOTAL_WELFARE += 50000000
#     EPIDEMICCOUNTDOWN -= 1
#     #COS Variables (CONSTANT)
#     IMMIGRATION_RATE = 0.015
#     #CHE Variables (CHECK)
#     if EPIDEMICCOUNTDOWN == 0:
#         EPIDEMIC = False
#         EPIDEMICRECOVERY = True
#         EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
    
# #POSV (POST-SCRIPT-VARIABLES):
# if EPIDEMICRECOVERY == True:
#     PUBLIC_SPENDING -= 10000000
#     TOTAL_WELFARE -= 50000000
#     EPIDEMICCOUNTDOWN -= 1
# elif EPIDEMICCOUNTDOWN == 0:
#     EPIDEMICRECOVERY = False
#     EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery

# #EPIDEMIC CODE PRE SIMPLIFCATION^
# 
#Initial wealth system, mainly based on the job they get. These introduce static compound growth changes
# to the industry the person works in, and a static determinant for their wealth, rather than dynamic
# 
# #main program changes.py

# wealthevent.py
# 
# #Simulating the wealth of citizens
# import numpy as np
# import os
# import sys
# TESTS= False
# def WealthEvent():
#     SYMBOLCHANGE = 0
#     SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
#     global PERCENTAGECHANGE
#     global HOLDINGSALARY
#     if 'POSITIVE' in SYMBOLCHANGE:
#         SYMBOLCHANGE = 1
#     else:
#         SYMBOLCHANGE = -1
#     PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
#                      p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
#     if '1p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
#     elif '2p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
#     elif '3p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
#     elif '4p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
#     elif '5p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
#     elif '6p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
#     elif '7p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
#     elif '8p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
#     elif '9p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
#     elif '10p' in PERCENTAGECHANGE:
#         HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
#     #Tests
#     if TESTS == True:
#         print(HOLDINGSALARY)
#         print(SYMBOLCHANGE)
#         print(PERCENTAGECHANGE)
# class Citizen:
#     def __init__(self, s):
#         self.salary = s
#
# 
# Happiness, people generation. happiness based on the closeness of each economy product to its ideal base
# of 1
# #vat-happiness.py
# #Making the program accessible with sleep, a choice of continuing the citizen simulation,
# #Citizen simulation will print the amount of years of simulation, each iteration
# #Is one year.It can also let you create new citizens. Each citizen group should have their own name
# #e.g. Citizens
# print("New Simulation (N) \n Load Simulation (L) \n Exit (E)")
# CHOICE = str(input())
# SIMULATIONCHOSEN = False
# NUMBEROFPREVIOUSSIMULATIONS = 0
# while SIMULATIONCHOSEN == False:
#     if "N" in CHOICE:
#          NUMBEROFPREVIOUSSIMULATIONS += 1 # amount before this one
#          FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")
#     elif "L" in CHOICE:
#          FILEWRITING = str("NEWCITIZENSALARIES.txt")
#     elif "E" in CHOICE:
#         sys.exit()
#     else:
#          FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")

# # The following code can be used to make new directories exclusively even any parent directories:
# # os.mkdir(path)

# #This citizen simulation should be done to simulate an average salary, average lifespan and other things
# #To make it usable there will have to be a upper and lower bound based on the normal distribution of the said
# #Variables

# P1 = Citizen(30000)
# P1.salary= 30000
# with open(FILEWRITING, "w+", encoding="utf-8") as NCS:
#                 NCS.write("")
#                 NCS.close()
# with open("CITIZENSALARIES.txt", "r", encoding="utf-8") as fp:
#         CURRENTCITIZENCOUNT = 0
#         while CURRENTCITIZENCOUNT < 20:
#             CITIZENID = str(("P",str(CURRENTCITIZENCOUNT)))
#             CITIZENID = Citizen(fp.readline())
#             #Salary change
#             HOLDINGSALARY = P1.salary
#             WealthEvent()
#             with open("NEWCITIZENSALARIES.txt", "a+", encoding="utf-8") as NCS:
#                 NCS.write(str(HOLDINGSALARY))
#                 NCS.write("\n")
#                 NCS.close()
#             #End of Salary change

#             #Need a test to see how many citizen numbers were printed, if below a certain
#             #amount, the file is discarded and the while loop ended.
#             #Try (name file), except if (CITIZENCOUNT < 20)

#             CURRENTCITIZENCOUNT += 1
#         fp.close()

# 
# """
"""

#Something else wiht happiness vat and consumtpion
# Year = 2023
Month = 5
# while Year != 2024 and Month != 5:
#     HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier)
#     TotalIncomeFromVAT += VAT * (GoodConsumptionModifier * Population)
#     Month += 1
#     if Month == 12:
#         Year += 1
#         Month = 1
# 
# 
#            def HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier):
#     if HappinessModifier == 60:
#         Population -= GoodConsumptionModifier
#         HappinessModifier -= 0.5
#     if HappinessModifier == 65:
#         Population += GoodConsumptionModifier
#         HappinessModifier += 0.5
#     if HappinessModifier == 70:
#         Population += GoodConsumptionModifier * 1.2
#         HappinessModifier += 0.75
        
#           def HAPPINESSRESULT(HappinessModifier):
#     global HappinessResult
#     if HappinessModifier <= 50:
#         HappinessResult = ("Unhappy")
#     if 50 <= HappinessModifier <= 70:
#         HappinessResult = ("Satisified")
#     if HappinessModifier <= 50    :
#         HappinessResult = ("Overjoyed")
# 

# import random
# from random import randint
# PERIOD = ("a")
# TRADERS = randint(2,5) # For a random market x there will exist 2 to 5 traders who have an interest in it:
# #Shorting it or investing in it may be decided later, this is a visual template.
# COMMODITIES = randint(2,20) # For a random market x there exists 2 to 20 commodities that can be interacted with.
# def TIME():
#     CURRENTTIME = 0
#     for i in PERIOD:
#         CURRENTTIME += 1
# HAPPINESSRESULT(HappinessModifier)
# FINANCIALRETURN = ("The government imposed a " , (VAT) , "% Value Added Tax, this earned\
#  them " , (TotalIncomeFromVAT) , "from the sale of wine alone")
# SOCIALRETURN = ("The citizens felt " , (HappinessResult) , "With the current \
#                 state of affairs")
                
# print(FINANCIALRETURN)
# print(SOCIALRETURN)
# 
# The most important and most lengthy part of the game code: Scripting
# 
# pickascriptoutofahat

# import random
# from random import randint

# List = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten")
# scriptfromlist = randint(0, 9)
# print(scriptfromlist)
# print(List[scriptfromlist])
# 
# #scripts.py

# #Current Scripts

# #Should probably convert this into a dictionary
# #Each number of a x0000000 series representing something

# #Base Script Process

# #Base scripting process
# import random
# from random import randint

# A1="One"
# A2="Two"
# A3="Three"
# A4="Four"
# B1="Five"
# B2="Six"
# B3="Seven"
# B4="Eight"
# C1="ELECTION"
# C2="TAXRATECHANGE"
# C3="INTERESTRATECHANGE"
# C4="Twelve"
# PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
# SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
# NAMED_SCRIPTS = [C1,C2,C3,C4]
# SCRIPT_NUMBER = random.randint(1,12)
# SCRIPTS = (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4)
# CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER-1]
# if "One" in CHOSEN_SCRIPT:
#     print("One  /"
#           "                    ") # Description
#                                   # Description part 2
# if "Two" in CHOSEN_SCRIPT:
#     print("Two   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Three" in CHOSEN_SCRIPT:
#     print("Three   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Four" in CHOSEN_SCRIPT:
#     print("Four   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Five" in CHOSEN_SCRIPT:
#     print("Five   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Six" in CHOSEN_SCRIPT:
#     print("Six   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Seven" in CHOSEN_SCRIPT:
#     print("Seven   /"
#           "                    ") # Description
#                                   # Description part 2
# if "Eight" in CHOSEN_SCRIPT:
#     print("Eight   /"
#           "                    ") # Description
#                                   # Description part 2          
# if "ELECTION" in CHOSEN_SCRIPT:
#     print("Election time!/"
#           "The new prime minister is ...") # Should be integrated with political leader variable at some point
#                                            # Calculated by party popularity defined by money, nepotism whatverthefuck...
# if "TAXRATECHANGE" in CHOSEN_SCRIPT:
#     print("Tax Rate Change/"
#           "                    ") # Description
#                                   # Description part 2
# if "INTERESTRATECHANGE" in CHOSEN_SCRIPT:
#     print("Interest rate change/"
#           "                    ") # Description
#                                   # Description part 2
# if "Twelve" in CHOSEN_SCRIPT:
#     print("twelve/"
#           "                    ") # Description
#                                   # Description part 2
# #Currently Written Script Process
# """
# def script_process(TAXINCOME):
#     A1="NeighbourTrade1"
#     A2="NeighbourTrade2"
#     A3="NeighbourTrade3"
#     A4="GovernmentScandal"
#     B1="Epidemic"
#     B2="TaxRateChange"
#     B3="GoodYear"
#     B4="BadYear"
#     PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
#     SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
#     #Undefined Scripts = [C1,C2,C3,C4]
#     SCRIPT_NUMBER = random.randint(0,5)
#     SCRIPTS = (A1,A2,A3,A4,B1,B2B3,B4)#C1,C2,C3,C4)
#     CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER]
#     if "One" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR1) + "offers a trade opportunity")
#         return INFO
#     if "Two" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR2) + "offers a trade opportunity")
#         return INFO
#     if "Three" in CHOSEN_SCRIPT:
#         CURRENTTAXINCOME = TAXINCOME
#         TAXINCOME =  CURRENTTAXINCOME + 100000
#         INFO = ("Trade Opportunity!  /" #Description +
#             "Your Neighbour " + (NEIGHBOUR3) + "offers a trade opportunity")    
#         return INFO          
#     if "Four" in CHOSEN_SCRIPT:
#         INFO = ("Government scandal" +
#             "Party popularity down by 20%")
#         ValueRandomised = randint(0,10)
#         if ValueRandomised > 7 :
#             ("Protests continue")
#         return INFO
#     if "Five" in CHOSEN_SCRIPT:
#         INFO = ("Epidemic has broken out" +
#             "Mortality rate increases by 5% while its ongoing" +
#             "It may be wise to invest in healthcare to counteract this")
#         global EPIDEMIC
#         EPIDEMIC = True                         
#         return INFO
#     #if "ELECTION" in CHOSEN_SCRIPT:
#     #    print("Election time!/"
#     #        "The new prime minister is ...") # Should be integrated with political leader variable at some point
#     #                                        # Calculated by party popularity defined by money, nepotism whatverthefuck...
#     #Political system in progress
#     if "TAXRATECHANGE" in CHOSEN_SCRIPT:
#         INFO = ("Tax Rate Change")
#         TAXINCOME += TAXINCOME * 0.01
#         return INFO
#     if "GOODYEAR" in CHOSEN_SCRIPT:
#         COUNTRYDEVELOPMENT += 0.01(for every 0.01 this increases all other variables to improve the country)   
# """

# """Add to scripts:
# Potential change
# GoodYear/BadYear:
#     When this function is invoked the program will randomly decide which is true, and then certain variables
#     attributed will then increase or decrease.
# """
# 

#
"""
for this i would need:
consumption events ( consumes food -5 food)
bandit events (steals food -5 food)
production ( whiskey making +10 food +20 money)
leadership ( hire sheriff -10 money bandits skip next days raid)
population ( endorse a visit from a travelling circus -10 food bandits skip next two raids)

variables food money
consumption
bandit
production
leadership or population or skip

let’s simply make this small part of the program, that’s it, no more events,
 no randomising just this simple static little visual text based game.
"""


"""
IMPORT SECTION
"""

from random import randint

""" 
NTRO AND DEFINITIONS
"""

print("Your people have 10 days to survive in the wild west... Good Luck")
# #File save code for data analysis
# """os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
# DATA_INPUTTED = 0
# with open("File_Number.txt", "r+", encoding="utf-8") as fp:
#     Content = fp.readlines()
#     AMOUNT_WRITTEN = int(Content[0])
#     AMOUNT_WRITTEN += 1
#     fp.close()
# with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
#     fp.write(str(AMOUNT_WRITTEN))
#     fp.close()
# AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
#         POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = print("The year ", YEAR),
#         MI = print("MIGRATION", MIGRATION),
#         PO = print("POPULATION", POPULATION),
#         TR = print("Tax rate", round((TAXES * 100), 2), "%"),
#         MP = print("MIGRATION percent", MIGRATION_PERCENT),
#         if VALUE_OF_TOWN > 1000000000:
#             VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
#         else:
#             print("Value of the country ", int(VALUE_OF_TOWN))
#         SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
#         WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
#         print("You increased taxes ", CHOICE1, "times.")
#         TOTAL_SCORE += VALUE_OF_TOWN
#     print("You changed taxes ", CHOICE1, "times.")
#     if CHOICE1 > 5:
#         print("Perhaps too much...")
#         print(CHOICE1)
#     if CHOICE2 > 5:
#         print("Perhaps too little...")
#         print(CHOICE2)
#     print(TOTAL_SCORE)
#     RoundTaxes = round((TAXES * 100), 2)
#     YAR = "Final year " + str(YEAR)
#     if TOTAL_SCORE>1000000000:
#         TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
#     else:
#         TOTLSCR = "Total Score " + str(TOTAL_SCORE)
#     MAR = "MIGRATION in final year " + str(MIGRATION)
#     PAR = "POPULATION in final year " + str(POPULATION)
#     TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
#     MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
#     VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
#     TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
#     TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
#     TAXINC = "Tax changes " + str(CHOICE1)
# # The save to file functions are in progress, though it's possible to print all to a file,
# # comparative pairs direct to an Excel file would be easiest to recursively compare.
#     Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
#     os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
#     with open(Name, 'a', encoding="utf-8") as fp:
#         fp.write("\n")
#         if MODE == "all":
#             MODE = "TSTMTPTTTMPTVTSPTWPTINC"
#         if 'TS' in  MODE:
#             with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
#                 tsfp.write(str(TOTLSCR))
#                 tsfp.close()
#             with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
#                 trfp.write(str(TAXR))
#                 trfp.close()
#         if 'TM' in  MODE:
#             fp.write("\n")
#             fp.write(str(MAR))
#         if 'TP' in  MODE:
#             fp.write("\n")
#             fp.write(str(PAR))
#         if 'TT' in  MODE:
#             fp.write("\n")
#             fp.write(str(TAXR))
#         if 'TMP' in MODE:
#             fp.write("\n")
#             fp.write(str(MARPR))
#         if 'TV' in  MODE:
#             fp.write("\n")
#             fp.write(str(VALT))
#         if 'TSP' in MODE:
#             fp.write("\n")
#             fp.write(str(TOTLSAL))
#         if 'TWP' in MODE:
#             fp.write("\n")
#             fp.write(str(TOTALWEL))
#         if 'TINC' in    MODE:
#             fp.write("\n")
#             fp.write(TAXINC)
#         fp.write("\n")
#         fp.close()"""
# Another version of MAIN
# 
# 
# #released program
# import time
# from time import sleep
# import random
# from random  import randint
# AMOUNT_WRITTEN=0
# MODE = "all"
# with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
#         fp.write("")
#         fp.close
# YEAR = 1960
# TAXINCOME = 50000
# POPULATION = 5000
# WORK_EFFICIENCY = 0.6
# PUBLIC_SPENDING = 20000
# IMMIGRATION_RATE = 0.05
# WORKING_AGE_POPULATION = 3000
# UNEMPLOYED_POPULATION = 500
# TOTAL_SALARIES_PAID = 15000
# LITERACY = 0.5
# TOTAL_WELFARE = 1000
# GDP = 100000
# YEARLY_MORTALITY_RATE = 0.035
# HEALTHCAREEFFICIENCY = 0.6
# ECONOMICDEVELOPMENT = 0.5
# HOMELESSRATE = 0.05
# while YEAR != 1970:
#     POPULATION_START_OF_YEAR = POPULATION
#     print("Year ", (YEAR))
#     YEAR += 1
#     LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
#     PUBLIC_SPENDING = 0.1 * GDP
#     HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4)
#     POPULATION += 100
#     WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
#     UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
#     TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
#     TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
#     TAXINCOME = POPULATION * 10
#     CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
#     POPULATION_END_OF_YEAR = POPULATION
#     with open("FileNumber.txt", "a", encoding="utf-8") as fp:
#         AMOUNT_WRITTEN += 1
#         fp.write(str(AMOUNT_WRITTEN))       
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = str(("The year at finish = ", YEAR))
#         MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
#         PO = str(("Population = ", POPULATION))
#         TR = str(("Tax Income = ", (TAXINCOME)))
#         SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
#         WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
#         FILEINPUTDETERMINED = False
#         while FILEINPUTDETERMINED == False:
#             if MODE == "all":
#                 MODE = "WYMIPOTRSALPWELP"
#             if "WY" in MODE:
#                 fp.write(" " + WY + " " + "\n" )
#             if "MI" in MODE:
#                 fp.write(" " + MI + " " + "\n")
#             if "PO" in MODE:
#                 fp.write(" " + PO + " " + "\n")
#             if "TR" in MODE:
#                 fp.write(" " + TR + " " + "\n")
#             if "SALP" in MODE:
#                 fp.write(" " + SALP + " " + "\n")
#             if "WELP" in MODE:
#                 fp.write(" " + WELP + " " + "\n")           
#             FILEINPUTDETERMINED = True
#         fp.write("\n")
   #     fp.close() 


# save_to_a_file.py

# """os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
# DATA_INPUTTED = 0
# with open("File_Number.txt", "r+", encoding="utf-8") as fp:
#     Content = fp.readlines()
#     AMOUNT_WRITTEN = int(Content[0])
#     AMOUNT_WRITTEN += 1
#     fp.close()
# with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
#     fp.write(str(AMOUNT_WRITTEN))
#     fp.close()
# AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)            
#         POPULATION_END_OF_YEAR = POPULATION_START_OF_YEAR
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = print("The year ", YEAR),
#         MI = print("MIGRATION", MIGRATION),
#         PO = print("POPULATION", POPULATION),
#         TR = print("Tax rate", round((TAXES * 100), 2), "%"),
#         MP = print("MIGRATION percent", MIGRATION_PERCENT),
#         if VALUE_OF_TOWN > 1000000000:
#             VALT = print("Value of the town ", int(VALUE_OF_TOWN)/1000000000, "billion"),
#         else:
#             print("Value of the country ", int(VALUE_OF_TOWN))
#         SALP = print("Salaries paid this year ", int(TOTAL_SALARIES_PAID)),
#         WELP = print("Welfare paid this year ", int(TOTAL_WELFARE)),
#         print("You increased taxes ", CHOICE1, "times.")
#         TOTAL_SCORE += VALUE_OF_TOWN
#     print("You changed taxes ", CHOICE1, "times.")
#     if CHOICE1 > 5:
#         print("Perhaps too much...")
#         print(CHOICE1)
#     if CHOICE2 > 5:
#         print("Perhaps too little...")
#         print(CHOICE2)
#     print(TOTAL_SCORE)
#     RoundTaxes = round((TAXES * 100), 2)
#     YAR = "Final year " + str(YEAR)
#     if TOTAL_SCORE>1000000000:
#         TOTLSCR = "Total Score " + str(round((int(TOTAL_SCORE)/1000000000), 2)) + " billions"
#     else:
#         TOTLSCR = "Total Score " + str(TOTAL_SCORE)
#     MAR = "MIGRATION in final year " + str(MIGRATION)
#     PAR = "POPULATION in final year " + str(POPULATION)
#     TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
#     MARPR = "MIGRATION percent in final year " + str(MIGRATION_PERCENT)
#     VALT = "Value of the town in final year " + str(VALUE_OF_TOWN)
#     TOTLSAL = "Salaries paid in final year " + str(TOTAL_SALARIES_PAID)
#     TOTALWEL = "Welfare paid in final year " + str(TOTAL_WELFARE)
#     TAXINC = "Tax changes " + str(CHOICE1)
# # The save to file functions are in progress, though it's possible to print all to a file,
# # comparative pairs direct to an Excel file would be easiest to recursively compare.
#     Name = "Scores" + AMOUNT_WRITTEN +   MODE + ".txt"
#     os.chdir('/workspaces/Economy-Program/EconomySimulationFiles/EconomyLogFiles')
#     with open(Name, 'a', encoding="utf-8") as fp:
#         fp.write("\n")
#         if MODE == "all":
#             MODE = "TSTMTPTTTMPTVTSPTWPTINC"
#         if 'TS' in  MODE:
#             with open(("TOTAL_SCORE" + Name), "a", encoding="utf-8") as tsfp:
#                 tsfp.write(str(TOTLSCR))
#                 tsfp.close()
#             with open(("Tax" + Name), "a", encoding="utf-8") as trfp:
#                 trfp.write(str(TAXR))
#                 trfp.close()
#         if 'TM' in  MODE:
#             fp.write("\n")
#             fp.write(str(MAR))
#         if 'TP' in  MODE:
#             fp.write("\n")
#             fp.write(str(PAR))
#         if 'TT' in  MODE:
#             fp.write("\n")
#             fp.write(str(TAXR))
#         if 'TMP' in MODE:
#             fp.write("\n")
#             fp.write(str(MARPR))
#         if 'TV' in  MODE:
#             fp.write("\n")
#             fp.write(str(VALT))
#         if 'TSP' in MODE:
#             fp.write("\n")
#             fp.write(str(TOTLSAL))
#         if 'TWP' in MODE:
#             fp.write("\n")
#             fp.write(str(TOTALWEL))
#         if 'TINC' in    MODE:
#             fp.write("\n")
#             fp.write(TAXINC)
#         fp.write("\n")
#         fp.close()"""
# # """
# #Main portion of code
# while YEAR != 1970:
#     POPULATION_START_OF_YEAR = POPULATION
#     print("Year ", (YEAR))
#     YEAR += 1
#     #All this code needs to implement gradual changes not new definitions each time
#     LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
#     PUBLIC_SPENDING = 0.1 * GDP
#     HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4) #THis results in it being equal to 0.6 at start
#     # The 1000000 is only suitable for small simulations, it will represent
#     #the peak of GDP that should be attainable meaning more can be spent on healthcare
#     #0.4 represents base healthcare, which at its lowest should equal this
#     #in year 1 with no other changes it should equal 0.45
#     #unsure code :YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION) + (0.0024 * POPULATION)) / POPULATION)
#     #first bracket=Elderly Death second bracketHealth Related Deaths
#     #unsure code:IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
#     #POPULATION =(100 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE) For debugging pop increases by 100 each year
#     POPULATION += 100
#     #Bad Code : events already determined : CRIME = 0.07952 * POPULATION
#     WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
#     UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
#     #Bad Code : just use a real equation : GDP = WORK_EFFICIENCY * (0.6 * POPULATION)
#     TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
#     TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
#     TAXINCOME = POPULATION * 10
#     CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
#     #Needs to calculate tax income somehow
#     """""
#     #SCRIPT SPECIFIC
#     These require scripts to not ruin readability of the program
#     if EPIDEMIC == True:
#         POPULATION  -= 50000
#         GDP -= 10000000
#         PUBLIC_SPENDING += 10000000
#         TOTAL_WELFARE += 50000000
#         EPIDEMICCOUNTDOWN -= 1
#         IMMIGRATION_RATE = 0.015
#         if EPIDEMICCOUNTDOWN == 0:
#             EPIDEMIC = False
#             EPIDEMICRECOVERY = True
#             EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
#     elif EPIDEMICRECOVERY == True:
#         PUBLIC_SPENDING -= 10000000
#         TOTAL_WELFARE -= 50000000
#         EPIDEMICCOUNTDOWN -= 1
#         if EPIDEMICCOUNTDOWN == 0:
#             EPIDEMICRECOVERY = False
#             EPIDEMICCOUNTDOWN = 3 # This will be used to countdown recovery
#     """""
#     #END OF YEAR CHECKS
#     """""
#     if YEAR % 2 == 0:
#         script_process(TAXINCOME)
#     PACEUNDECIDED = True
#     while PACEUNDECIDED == True:
#         if PACE == 0:
#             PACEUNDECIDED = False
#         else:
#             time.sleep(PACE)
#             PACEUNDECIDED = False
#     """
#     """
#     if ECONOMICDEVELOPMENT > 0.5:
#         IMMIGRATION_RATE += 0.01
#         HOMELESSRATE -= 0.001
#     """
#     POPULATION_END_OF_YEAR = POPULATION
#     #   File save code
#     # The save to file functions are in progress, though it's possible to print all to a file,
#     # comparative pairs direct to an Excel file would be easiest to recursively compare.
#     with open("FileNumber.txt", "a", encoding="utf-8") as fp:
#         AMOUNT_WRITTEN += 1
#         fp.write(str(AMOUNT_WRITTEN))       
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = str(("The year at finish = ", YEAR))
#         MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
#         PO = str(("Population = ", POPULATION))
#         TR = str(("Tax Income = ", (TAXINCOME)))
#         SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
#         WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
#         FILEINPUTDETERMINED = False
#         while FILEINPUTDETERMINED == False:
#             if MODE == "all":
#                 MODE = "WYMIPOTRSALPWELP"
#             if "WY" in MODE:
#                 fp.write(" " + WY + " " + "\n" )
#             if "MI" in MODE:
#                 fp.write(" " + MI + " " + "\n")
#             if "PO" in MODE:
#                 fp.write(" " + PO + " " + "\n")
#             if "TR" in MODE:
#                 fp.write(" " + TR + " " + "\n")
#             if "SALP" in MODE:
#                 fp.write(" " + SALP + " " + "\n")
#             if "WELP" in MODE:
#                 fp.write(" " + WELP + " " + "\n")           
#             FILEINPUTDETERMINED = True
#         fp.write("\n")
#         fp.close()


"""

	◦	use script scheme from economy simulation, use
     also character generation and a simple economy scheme. 
     based on The economy  three arrows down to booze, ladies,
      robberies. Your economy relies on the amount and strength 
      of these 3 products. Therefore the stronger these 3 are the 
      stronger your economy, the higher your immigration rate, 
      lowering these numbers down again. In an ideal world each 
      person has traits affecting the amount of each he will want.
       With only 3 each person can have a base and one up and one
        down for each one based on a dice roll. Something like a 
        dwarf fortress interface i would like but honestly every 
        game maker seems like dog shit made for 2d side scrollers 
        or 3rd person games. I just need a strategy game game maker. 
        Maybe we could jerry rig a rpg maker game into this.
         The economy is a figure known as accountant. Each dialogue 
         choice says the abundance of each product. Too much of 
         certain ones should bring their own impacts, as well as
          too little of some. Then the 3 products are represented
           by another figure each. And then we could think about
            1 or 2 figures underneath each one. To reduce the
             feeling of an rpg you could send people on missions, 
             after which recovery would also be based on the 3 products.
             At the start it will be easy to meta and it will likely be 
             very short days, but with more random events it could be
             better. stage one accountant and all in the bar. He just 
            works at one of the tables with a ledger in front of him and 
            other papers. Stage 2 an office for you as the mayor and the
             accountant and 3 representatives in each of their respective
              areas e.g. distillery/bar, brothel, bar for robbers
	◦	Step 1 Download the most compatible RPG maker or GM maker or something else you find for 2d strategy even something like civ ffs. Potentially defold, use something called an ECS, do i need c++ to do this?
	◦	step 2 Tile set if needed new or find one
	◦	step 3 Now the accountant design
	◦	step 4 the three products looks
	◦	step 5 now dialog for accountant
	◦	step 6 now dialog for 3 products
	◦	step 7 scripting with 50 50 chance for an increase in a products abundance .
"""

#Economy - Booze, Ladies, Robbery
# Booze - Distilling, Trade
# Ladies - Kidnapping, buying
# Robbery - On the road, in the town
# Distilling - Distillery owner
# Trade - Merchant
# Kidnapping - Highway robber
# Buying - Pimp
# On the road - Highway robber #2
# In the town - Scallywag
# 
# 
# future use
# 
# 
# #Version 3(Release Version Saving):
# """
# #Needs to be at beginning:
# AMOUNT_WRITTEN=0
# WhatToWriteToFile = "all"
# with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
#         fp.write("")
#         fp.close

# #Needs to be within the while loop of the program
#     POPULATION_END_OF_YEAR = POPULATION
#     #   File save code
#     # The save to file functions are in progress, though it's possible to print all to a file,
#     # comparative pairs direct to an Excel file would be easiest to recursively compare.
#     with open("FileNumber.txt", "a", encoding="utf-8") as fp:
#         AMOUNT_WRITTEN += 1
#         fp.write(str(AMOUNT_WRITTEN))       
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = str(("The year at finish = ", YEAR))
#         MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
#         PO = str(("Population = ", POPULATION))
#         TR = str(("Tax Income = ", (TAXINCOME)))
#         SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
#         WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
#         FILEINPUTDETERMINED = False
#         while FILEINPUTDETERMINED == False:
#             if MODE == "all":
#                 MODE = "WYMIPOTRSALPWELP"
#             if "WY" in MODE:
#                 fp.write(" " + WY + " " + "\n" )
#             if "MI" in MODE:
#                 fp.write(" " + MI + " " + "\n")
#             if "PO" in MODE:
#                 fp.write(" " + PO + " " + "\n")
#             if "TR" in MODE:
#                 fp.write(" " + TR + " " + "\n")
#             if "SALP" in MODE:
#                 fp.write(" " + SALP + " " + "\n")
#             if "WELP" in MODE:
#                 fp.write(" " + WELP + " " + "\n")           
#             FILEINPUTDETERMINED = True
#         fp.write("\n")
#         fp.close()
#     with open("FileNumber.txt", "a", encoding="utf-8") as fp:
#         AMOUNT_WRITTEN += 1
#         fp.write(str(AMOUNT_WRITTEN))       
#         POPULATION_CHANGE = ((POPULATION_END_OF_YEAR-POPULATION_START_OF_YEAR)
#         /POPULATION_START_OF_YEAR)
#         WY = str(("The year at finish = ", YEAR))
#         MI = str(("Immigration Rate = ", IMMIGRATION_RATE))
#         PO = str(("Population = ", POPULATION))
#         TR = str(("Tax Income = ", (TAXINCOME)))
#         SALP = str(("Salaries paid this year ", int(TOTAL_SALARIES_PAID)))
#         WELP = str(("Welfare paid this year ", int(TOTAL_WELFARE)))
#         #New Code:
#         FILEINPUTDETERMINED = False
#         #^^^^^^^^^^^^^^^^^^^^^^^^^^
#         #Separate file saving from main code completely. Or the same way it is.
#         while FILEINPUTDETERMINED == False:
#             if WhatToWriteToFile == "":
#                 FILEINPUTDETERMINED = True
#             if WhatToWriteToFile == "all":
#                 WhatToWriteToFile = "WYMIPOTRSALPWELP"
#             if "WY" in WhatToWriteToFile:
#                 fp.write(" " + WY + " " + "\n" )
#             if "MI" in WhatToWriteToFile:
#                 fp.write(" " + MI + " " + "\n")
#             if "PO" in WhatToWriteToFile:
#                 fp.write(" " + PO + " " + "\n")
#             if "TR" in WhatToWriteToFile:
#                 fp.write(" " + TR + " " + "\n")
#             if "SALP" in WhatToWriteToFile:
#                 fp.write(" " + SALP + " " + "\n")
#             if "WELP" in WhatToWriteToFile:
#                 fp.write(" " + WELP + " " + "\n")           
#             FILEINPUTDETERMINED = True
    #    fp.write("\n")



# #This hopefully will lead to progress on either a grid based generic world game,
# #or a wild west thing
# #All Comments,Notes,Ideas e.t.c
# # The Wild West
# """
# """
# Let’s feed the numbers i have into godot and see what visuals i could get like 
# houses and stuff, simulate emigration through abandoned buildings
# the country is some landlocked state with a lot of nomadic movement

# actually maybe it’s just a town in the wild west, with a tavern, and movement is
# likely. Though if you provide the right
# services there’s a chance people coming through will settle, if they’re cowboys
# they’ll have specific traits and jobs
# that help your town uniquely to them. These guys can settle impromptu without 
# a house, but some types like accountants
# will need their own space. The game should start with a group of cowboys, 
# each can be assigned to any job and
# although
#     they’re jack of all trades there is some levity in their skills. For example
#      for 5 stats there’s maximum of 4 skill 
#     points up it could go down, at a chance of 1% that it could go this high, 
#     for example perception 9 instead of 5 
#     besides
#      any other changes would take a 1% odd. So after a while of operating and 
#      getting some immigrants you can build 
#      specialised buildings for them. ANd start replacing cowboys with 
#      profesional workers, after all not everyone wants
#       a knife wielding gunslinger as their barber. The growth and birth 
#       randomisation can be imported. The chances of 
#       immigration and all that simulation can also be imported, to at the 
#       beginning happen turn based with eventual 
#       real time changing with natural changes in migration, although most 
#       likely like this. You’re in the centre of 
#       5 towns around you, north, south east, south west, east and west, 
#       for someone from the north to go south east 
#       it is very likely they will go through you, if either your area is 
#       appealing enough or if it is too dangerous 
#       to move through the wild west they’ll stay with you, either for a
#        night or more, maybe convince them with some 
#       escorts to see if you could get that towns favour.

# step 1 - data based simulation of day by day changes in population, 
# most likely your base population of 10 doesn’t change much. and then up to 
# 6 groups at most(one from each town) could possibly stay, . maximum of 24 
# people let’s say. So at most your population would grow by 2.4 times base. 
# To appease a town you can offer them food. One unit of food satisfies one
#  person. So at most you could use up 24 units of food. How can food be obtained
#  , buying from caravans, hunting, donations, random events.

# Step 2 CDDA level graphics, if not DF style. The point of the game at this 
# point should be. To slowly specialise into one way, in order to appease a 
# specific town and guarantee survival of your town through trade incentives 
# from that town for a specific good as well as many other for cheaper as well, 
# e.g. food. After this you could try plundering rival towns in order to appease
#  the town your favourable with.


# it’s unlikely a caravan from one town should go all the way around, but if they
#  do you’re the one missing out on sweet money, goods and potential loot if 
#  they’re dumb enough( thievery aspect) Keep crime low, by keeping brigands 
#  at bay and having a police force to keep aware of bounties by either visiting
#  villages for info on criminals from either the police station, newspapers 
#  from outside the towns or through gossip with citizens(3 cards each a choice
#   that should be as dynamic as possible). This and attractiveness and as well
#    as interesting sites(tavern, escort building). Or even bribes can guarantee 
#    your town will stay alive, in the wild west

# T-Tavern
# H-Hotel
# P-(Hitching) post
# C-Camp
# R-Residential (home)
# C(-Commercial

# So one of the first processes would be Caravan movement, it would go as follows:

# (Town Name), (Town location) wants to trade with (TN), (TL). If adjacent it
#  simulates it. Trade Value for TN1 + 3(they sell and buy in one turn),Trade
#   value for TN2+2(they sell bormally but buy a limited amount from the caravan).

# # These decisions should be based on what the caravan either specifically 
# holds(Developed after it become a game) or predicted to (What the town produces
#  versus how much the other town needs it) If a towns specialty is oil gathering 
#  its priority to sell would be at some point 100% meaning up to 25% percent of
#   its holding caravan space would be designated for it. If another town is oil 
#   processing regardless of what size it has a high priority to buy this up to
#    the point where it has reserves for at least 7 turns. Trade happens every 
#    7 turns.

# Determined:
# Trade value earned is based on how much selling and buying is done. Simply that,
#  no minus values for selling more than buying, simple.
# Trade happens every 7 turns. They schedule imports 2 days before this? If we are
#  to simulate an external economy this would be needed to ensure these towns 
#  don’t die. So if we have two primary food producers, one oil producer, one 
#  construction material producer, and one population producer . 


# This is the order the code needs to be in, at least this early in.
# 	1.	movement of people in and out of town 7am
# 	2.	movement within town 7am
# 	3.	movement of people within town out of town 7am
# 	4.	Caravan events 7-12pm
# 	5.	Item gathering events 7-2pm
# 	6.	Town planning(building + emergency events)2-5pm
# 	7.	final movement out of town 2-7pm
# 	8.	Final movement into town 5-10pm

# Chance of a caravan being caught should have a number peaking between 8pm and 
# 6am.  lowest between 12pm and 3pm And a static 10% chance for all other hours. 
# CHance of succes should be based on each event, although some shouldn’t be all 
# bad. Think oregon valley. There should be a choice to designate a patrol of 
# some size to decrease chance of bad events in one or all 5 paths between your 
# town and others. Sometimes you may get missions to patrol these when there’s 
# rare cargo, important people or simply a relationship boost at hand.


# Hour by hour
# Economy
# 
# 

##Interactive part of simulation and setup for the town
import random
from random import randint
BANDITSTRENGTH = 3 #(0 = lowest 3 = highest)
PEOPLE = 10
Food = 50
Cash = 100
ALCOHOL = 10
FOODGAIN = 5
FOODLOSS = 2
ALCOHOLLOSS = 1
FOODVALUE = 1
ALCOHOLVALUE = 4 
PEOPLEVALUE = 50
DAY = 1 
CURRENTINVESTMENTS = ["SCARECROW", "BARREL"]
GAMEACTIVE = True
EMERGENCY = False
CHOICE = "N"
BUILD = False

# Start of game
while GAMEACTIVE == True:
    print("This is your chance to see what will happen to a wild western town over the course of a day")
    # Start of day events(7AM)
    DAYS = 1
    while DAYS < 2:
        print("Day" , (DAY))
            if FOOD >= 5:
                print("Your people eat")
                FOOD -= 5
            else:
                print("Your people starve")
                PEOPLE -= 1
        Food += FOODGAIN
        print("CURRENT TRADER POSITIONS RELATIVE TO YOU(X IS TRADER, C IS Your town, T and a is other towns")
        print(":::::::::::::::::::::::::::::::::")
        print(":::::TXT:::::::CCC::::::::::::AAA")
        print(":::::::::::::::::::::::::::::::::")
    
        #Next event at 12pm is caravan event
        # Food goes up by 1kg for 2 dollars
        
        Food += 5
        Cash -= 10
        #At the same time you can choose to send people to rob a caravan
        CHOICE = input("Your people report a stray caravan, do you send them to rob it?")
        if CHOICE == "Y":
            SUCCESSAMOUNT = randint(0,2)
            if SUCCESSAMOUNT == 0:
                print("Rats, the caravan was as empty as the oafs brain who brought you this idea")
            if SUCCESSAMOUNT == 1:
                Food += 5
                Cash += 5
                print("The caravan was a meagre haul")
            if SUCCESSAMOUNT == 2:
                Food += 10
                Cash += 10
                print("The caravan was a great haul, there will be food for plenty days.")
    
        #The time is now 2pm:
        BUILDORDISASTER = randint(1,5)
        if (BUILDORDISASTER == 1) == True:
            EMERGENCY = True
            BUILD = False
        elif (BUILDORDISASTER > 1 and BUILDORDISASTER < 5):
            EMERGENCY = False
            BUILD = True
        else:
            EMERGENCY = False
            BUILD = False
        if EMERGENCY == True:
            BANDITEVENT = randint(0,1)
            if BANDITEVENT == 0:
                print("The bandits raid you")
                BANDITEVENTSUCCESS = randint(0,2)
                if BANDITEVENTSUCCESS:
                    if BANDITEVENTSUCCESS == 2:
                        print("The bandits succeed in raiding you")
                        FOOD -= 10
                        CASH -= 5
                    else:
                        BANDITCHOICE = input("You beat back the bandits, do you rob them for food?(Y/N)")
                        if BANDITCHOICE == ("Y"):
                            FOOD += 5
                        else:
                            print("The defeat of the bandits discourages some from further raiding")
                            print("They will be back however...")
                            BANDITSTRENGTH -= 1
            if BANDITSTRENGTH == 0:
                print("With the bandits defeated your people can live indefinetly longer without their threat")
        if BUILD == True:
            print(CURRENTINVESTMENTS[0])
            print(CURRENTINVESTMENTS[1])
            print("Your henchmen handy with a hammer informs you of various investments in the town")
            INVESTMENTCHOICE = input("Which do you choose?")
            if INVESTMENTCHOICE == 1:
                print("Upon building the scarecrow a couple people discover some plants nearby")
                print("You may get some food from these! How quaint.")
                FOODGAIN += 3
                CURRENTINVESTMENTS.remove("SCARECROW")
            elif INVESTMENTCHOICE == 2:
                print("Upon building some barrels a couple people discover that food in barrels")
                print("Can't be touched by rodents!")
                FOODLOSS -= 1
                CURRENTINVESTMENTS.remove("BARREL")
        FOOD -= FOODLOSS
        print("CURRENT TRADER POSITIONS RELATIVE TO YOU(X IS TRADER, C IS Your town")
        print(" T and a is other towns, other symbold are only rumoured...")        
        print(":::::::::W:::::::::::::::::::::::")
        print(":::::::::::::::::::::::::::::::::")
        print(":::::TTT:::::::CCC::::::X:::::AAA")
        print(":::::::::::::::::::::::::::::::::")
        print("::::::::::::::::::::TRTR:::::::::")
        choice = input("Send an expedition?")
        if choice == ("y"):
            expedition()
        else:
            #fuckitidontcare
        
    
        #The time is 7pm, Time for some traveller events
        #This should just be identical to the currentinvestments stuff
        #The time is 10pm, Time to rest
        GAMEACTIVE = False
        DAYS = 2
        #In the future the day limit will be different, meaning that raids are less likely,
         #build events less often etc

###Uninteractive part of simulation e.g. citizen generation and economy daily changes in prices

####Citizen Generation
#The random citizen generator is in progress, for now 10 people with their details in square brackets
#CITIZEN? = [TITLE, NAME, AGE, GENDER, HEIGHT, PERSONALITY]
CITIZEN1 = [Governor, HAYLE STAR, 30, M, 172, THRIFTY]
CITIZIEN2 = [Advisor, DAMN DANIEL, 35, M, 176, INTELLIGENT]
#ETC THIS SHIT SUCKS


####ECONOMY
#For simulating the economy around the town
PERIOD = (1)
TRADERS = randint(2,5) # For a random market x there will exist 2 to 5 traders who have an interest in it:
#Shorting it or investing in it may be decided later, this is a visual template.
COMMODITIES = randint(2,5) # For a random market x there exists 2 to 20 commodities that can be interacted with.
#In this case these commodities are subject to change based on what commodities are interacted with by the traders


#For now both of these functions are in progress
def TIME():
     CURRENTTIME = 0
     for i in PERIOD:
         CURRENTTIME += 1

def trader1():
    TRADERCANCELLED = 0
    while TRADERCANCELLED != 1:
        if int(ALCOHOL) > 5:
            SELLALCOHOL = input("Your advisor begrudgingly offers a sale of some alcohol for cash")
            print("(2 dollars perlitre")
            ALCOHOL -= int(SELLALCOHOL)
            CASH += 2*SELLALCOHOL
        if FOOD >= 50:
            SELLFOOD = input("The trader offers a meagre 50 cents per kg of food, how much do you sell?")
            print("(0 TO CANCEL)")
            if SELLFOOD =("0"):
                TRADERCANCELLED = 1
            SELLFOOD = int(SELLFOOD)
            else:
                if SELLFOOD > FOOD:
                    print("The trader rejects your ridiculous offer and moves on")
                    TRADERCANCELLED = 1
                if SELLFOOD = FOOD:
                    print("Your advisor shudders thinking of how your town will survive with no food")
                FOOD -= int(SELLFOOD)
                CASH += float(0.5*SELLFOOD)

    else:
        print("The trader reviews your meagre stocks and spares you from his savage prices")
        TRADERCANCELLED = 1
def expedition():
    CURRENTEXPEDITIONCHOICES = [WOLFDEN, TRIBE, TAWTON, ABEL]
    DESTINATION = input("Where do you send your people?(W,TR,T,A)")
    if DESTINATION = ("W"):
        PEOPLE -= 2
        FOOD += 50
        CASH += 20
        print("The meat of the wolves satiate, and their pelts sell for a nice amount,")
        print("however you lose two people")
    if DESTINATION = ("TR"):
        PEOPLE -= 4
        FOOD += 0
        CASH += 0
        print("Your people are taken prisoner, pray they don't come for the town")
        TRIBEVISIT = True
    if DESTINATION = ("T"):
        PEOPLE -= 0
        FOOD += 1
        CASH += 5
        print("Tawton is poor, after robbing a homeless person and scrounging some old food they return")
    if DESTINATION = ("A"):
        PEOPLE -= -1
        FOOD += 5
        CASH += 5
        print("The people of Abel are religious, they gift you food and money and send a missionary to stay")
        print("with you... unfortunately.
    
        

"""
AGE = 0
Height = 0
def Citizen():
    AGE = randint(18,50)
    GENDER = randint(0,1)
    if GENDER == 0:
        GENDER = M
    if GENDER == 1:
        GENDER = F
    #Height + PERSONALITY
    if GENDER == M:
        HEIGHT = randint(170,200)
        PERSONALITY = [AGGRESSIVE]
    if GENDER == F:
        HEIGHT = randint(150,180)
        PERSONALITY = [CARING]
    
        
TOTALCITIZENS = []
CITIZENSGENERATED = 0
while CITIZENSGENERATED < 10:
    CITIZENSGENERATED
"""

