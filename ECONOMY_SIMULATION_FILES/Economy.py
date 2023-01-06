"""
An interactive tech demo to teach economics.
Goals for this program:
Your success in the simulation is based on your total score as well as your final year score
Do better in these than in a simulation with no changes added, and you will be a winner
The only variable that needs changing should be the OS directory. Usually a subfolder exists
below the economy folder but my understanding of GitHub prevents me from doing this.
Any questions should be directed to my GitHub project. Constructive criticism is appreciated
especially from a data analysis standpoint as that is the direction this project is going towards
The average score for the game is equal to playing it with no tax tampering whatsoever
This is equal to:TOTAL_SCORE = 90348800000 VALUE_OF_TOWN = 1129360000
"""

import random
from math import sin
from math import log

WORKING_NAME = "Simulacra" # One simulation should be based on the economy of Greece before during and after the Troika program
POPULATION = 5000
WEEKLY_UPDATES = False
YEARLY_UPDATES = False

#Scan the variable INPUT_SCOPE before the program runs to 
def SCOPE(INPUT_SCOPE):
    INPUT_SCOPE = input("Choose either Weekly or Yearly"\
    "If Weekly the program runs for a year with weekly updates of 52"\
    "If Yearly the programs runs for 20 years with yearly updates of 20")

PACE = input("Slow or Fast or rapid Pace"\
    "If slow then data updates every 3 seconds"\
    "If fast then data updates every 0.5 seconds"\
    "If rapid then data has no update and simply gives you final results ASAP(for data collection")
def CRIME(CRIME_RATE):
    if SCOPE == YEAR:
        CRIME = 520
    elif SCOPE == WEEK:
        CRIME = 52 # criminal events a year, converitble to weeks if needed
def datainputter(IMMIGRATION_PERCENT,MIGRATION_PERCENT,TAXES,POPULATION,WORK_EFFICIENCY,
            PUBLIC_SPENDING,MIGRATION,IMMIGRATION,WORKING_AGE_POPULATION,UNEMPLOYED_POPULATION,
            RICH_POPULATION,RICH_POPULATION_VALUE,WORKING_POPULATION_VALUE,TOTAL_SALARIES_PAID,
            TOTAL_WELFARE,TOTAL_SCORE,VALUE_OF_TOWN,YEAR,CRIME,LITERACY,GDP,YEARLY_MORTALITY_RATE):
    YEAR=1960
    while YEAR<2020 or KeyboardInterrupt:
        YEAR+=1
        LITERACY = 0.8 #Should be impacted positively by gdp, public spending, employment, rich pop,
                       #Welfare, high taxes.Affects work efficeincy positively as well as class movement,
                       #Mortality goes down, values which impact it positvely also are impacted positvely
                       #By it. Negatively impacted by crime, mortality, migration of skilled workers(not yet
                       # implemented) Unemployment decreases it directly. 
        CRIME = (1520 - (LITERACY*125) )
        #1000 can represent the base weighted value figure of variable importance. Anything else less important goes below this.
        IMMIGRATION_PERCENT = 1000 * LITERACY + 1000 
        MIGRATION_PERCENT = 1000 * CRIME
        IMMIGRATION = 1000 * IMMIGRATION_PERCENT
        MIGRATION
        YEARLY_MORTALITY_RATE = CRIME*0.15*POPULATION + 0.02*POPULATION
        POPULATION = (IMMIGRATION-MIGRATION) - YEARLY_MORTALITY_RATE
        #Immigration percent to be weighed according to importance. Initially it will be:
        #1.00 for most importance, 0.8 for high, 0.5 for medium, 0.3 for low, 0 for no importance e.t.c
        IMMIGRATION_PERCENT=0.16*LITERACY

            #Immigration_percent is dependent on literacy,GDP,employment_rate
            # (lower=high_immigration) total_welfare(higher better), taxes.
            #  In order of importance highest to lowest. With high mid and low being referred to.
            #  Immigrants will be defined as separate classes of high, mid, low and refugee.
            # for lower class population: total welfare, literacy, taxes, employment_rate, GDP
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
DATA_INPUTTED=0
MODE = str(input("Input mode "))
while DATA_INPUTTED < 2:
    YEAR = 1960
    IMMIGRATION_PERCENT = 0.016
    MIGRATION_PERCENT = 0.00037
    TAXES = 0.05
    POPULATION = 67000000
    WORK_EFFICIENCY = 0.6
    PUBLIC_SPENDING = 13414*POPULATION
    MIGRATION = int(MIGRATION_PERCENT * POPULATION)
    IMMIGRATION = int(IMMIGRATION_PERCENT * POPULATION)
    WORKING_AGE_POPULATION = 0.8 * POPULATION
    UNEMPLOYED_POPULATION = 0.2 * POPULATION
    RICH_POPULATION = 0.1 * POPULATION
    RICH_POPULATION_VALUE = RICH_POPULATION * 100
    WORKING_POPULATION_VALUE = (WORK_EFFICIENCY * WORKING_AGE_POPULATION) * (24 * 7) * 350
    TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 400
    TOTAL_WELFARE = UNEMPLOYED_POPULATION * 150
    TOTAL_SCORE = 0
    VALUE_OF_TOWN = (WORKING_POPULATION_VALUE + RICH_POPULATION_VALUE - TOTAL_WELFARE
    -TOTAL_SALARIES_PAID)
    while YEAR < 2040:
        POPULATION = POPULATION-MIGRATION+IMMIGRATION
        YEAR += 1
        MIGRATION = int(MIGRATION_PERCENT * POPULATION)
        WORKING_AGE_POPULATION = 0.8 * POPULATION
        UNEMPLOYED_POPULATION = 0.2 * POPULATION
        RICH_POPULATION = 0.1 * POPULATION
        VALUE_OF_TOWN = (WORKING_POPULATION_VALUE + RICH_POPULATION_VALUE - TOTAL_WELFARE
        - TOTAL_SALARIES_PAID)
        TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 400
        TOTAL_WELFARE = UNEMPLOYED_POPULATION * 150
        POPULATION_START_OF_YEAR = POPULATION
        MILITARY_SPENDING = 0.2 * VALUE_OF_TOWN
        if POPULATION <= 10000:
            print("You lost, the town got too small. Try again.")
            YEAR = 2040
        if TAXES > 0.05:
            MIGRATION_PERCENT -= 0.004
            if TAXES > 0.055:
                MIGRATION_PERCENT -= 0.0045
        elif TAXES < 0.05:
            MIGRATION_PERCENT += 0.004
            if TAXES < 0.03:
                MIGRATION_PERCENT += 0.0045
        MIGRATION_PERCENT = round(MIGRATION_PERCENT, 4)
        Crisis = random.uniform(0, 40)
        if 0 <= Crisis <= 20:
            POPULATION += 3000
        elif 20 <= Crisis <= 40:
            POPULATION -= 3000

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