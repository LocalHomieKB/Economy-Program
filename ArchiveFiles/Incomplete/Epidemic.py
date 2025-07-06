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