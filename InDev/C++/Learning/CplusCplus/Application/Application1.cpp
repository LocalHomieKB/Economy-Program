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

vector<string> COMODITY_LIST = {"Beer", "Whiskey", "Revolvers", "Colts", "Horses", "Wagons"};
vector<int> COMMODITY_LIST_PRICE = {1,2,1,2,1,2}; 
//^//this list is proportional to commodities list from left to right
string NEIGHBOUR_TOMB = "Tombstone";
string NEIGHBOUR_DENIS = "St Denis";
string NEIGHBOUR_ARMA = "Armadillo";

//Population
//Important buildings
//Production
//Commodites in demand

// SCRIPT SPECIFIC VARIABLES
bool EPIDEMIC = {false}; // If true, the program will run in epidemic mode.
int EPIDEMIC_RECOVERY = {3}; 
//The town is boosted for this many turns after it ends
int EPIDEMIC_COUNTDOWN = {3}; 
// Each epidemic will last this many days, with the countdown starting after 
// the first year

//PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
string SCRIPTS_PREDEF_1 ="TOMBSTONE_TRADE_1";
vector<int> SCRIPTS_PREDEF_1_EFFECTS = int POPULATION += 1, int CASH_INCOME += 1, int COLTPRICE += 1, int TOMBTRADEDEMAND += 1 ;
//Not sure how to do this, when script one occurs, i want pop and cash income to go up, price of colts which tombstone will buy
//to go up, and the likelihood of a tombstone trader to buy colts to go up.
//We could as shown below with an if for each script, cons - takes longer to code and more lengthy.
string SCRIPTS_PREDEF_2 ="STDENIS_TRADE_1";
string SCRIPTS_PREDEF_3 ="ARMADILLO_TRADE_1";
string SCRIPTS_PREDEF_4 ="TownScandal";
//SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
string SCRIPTS_SEMIPREDEF_1 = "Epidemic";
string SCRIPTS_SEMIPREDEF_2 = "TaxRateChange";
string SCRIPTS_SEMIPREDEF_3 = "GoodYear";
string SCRIPTS_SEMIPREDEF_4 = BadYear";


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