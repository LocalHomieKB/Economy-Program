#include <iostream>
#include <string>
#include <vector>
using namespace std;

int DAYSIMULATION(int food)
{

}

int food = 10;
int danger = 1;
int population = 10; //random ass number
int food = 210; //one per head for 2 weeks surplus
int trade = 10;//placeholder

int main()
{
//Caravan headed by leader enters your town
//Should this be a linear or more open experience.

/*Function CARAVAN_NEWS
introduces elements of 
danger on a scale of 1 to 5, like defcons essentially.
population
food
trade
*/

//Store each caravan news event as a string based vector, the actual string segment will go as planned, the int will
//be converted after the fact

//CNEWS_1 go in this order:
// News, danger, pop, food, trade
vector<string> CNEWS_1 = {"Caravan bearing grave news enters your town, word of bandits roaming scare your citizens", 
    "Two", "one", "zero" , "zero" };

vector<string> CNEWS_DECISION1 = {"How do you respond?", "Expand watch", "Send patrols", "Ignore"} ;



cout << "Start of day(6am)" << endl;
//Chance to explore, set production, set construction
cout << CNEWS_1.front();//This should really be a general CNEWS that then randomly selects from a list of CNEWS
cout << "Midday(12am)" << endl;
// Caravan news segment
cout << "Evening(6pm)" << endl;
// Results of exploration, new visitors
cout << "Middnight(12pm)" << endl;
// this segment stretching to early morning are for wildlife attacks and bandit raids
/*
# This is the order the code needs to be in, at least this early in.
# 	1.	movement of people in and out of town 7am
# 	2.	movement within town 7am
# 	3.	movement of people within town out of town 7am
# 	4.	Caravan events 7-12pm
# 	5.	Item gathering events 7-2pm
# 	6.	Town planning(building + emergency events)2-5pm
# 	7.	final movement out of town 2-7pm
# 	8.	Final movement into town 5-10pm
*/

}
    //food loop check
    
    //danger
    //people
    //events
    //trade
    //events
    //population growth(2.4times base at most)
    //one unit of food per person at most
    //Rival towns
    //criminals
    //bounties
    //AI Caravans
    //  Its rules:
        

#COM_LIST = ["Beer", "Whiskey", "Revolvers", "Colts", "Horses", "Wagons"]
#COM_PRICE = [1,2,1,2,1,2]#this list is proportional to commodities list from left to right



# #This code generates a neighbour, stores, assigns, removes from list
# NEIGHBOURLIST = ["Tombstone", "St Denis"]
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
""