"""
Provides an in depth simulation of an economy akin to the UK
"""
# Goals for this program:
# A realistic simulation of a city - Not achieved
# The average score for the game is equal to playing it with no tax tampering whatsoever
# This is equal to:TOTALSCORE = 90348800000
# VALUEOFTOWN = 1129360000
# Your success in the simulation is based on your total score as well as your final year score
# Do better in these than in a simulation with no changes added, and you will be a winner
# The only variable that needs changing should be the OS directory. Usually a subfolder exists
# below the economy folder but my understanding of GitHub prevents me from doing this.
# Any questions should be directed to my GitHub project. Constructive criticism is appreciated
# , especially from a data analysis standpoint as that is the direction this project is
# going towards

import os
import sys

sys.path.append(os.path.realpath('..'))

DATAINPUTTED = 0
MODE = str(input("Input mode "))

with open("FileNumber.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNTWRITTEN = int(Content[0])
    AMOUNTWRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNTWRITTEN))
    fp.close()
AMOUNTWRITTEN = str(AMOUNTWRITTEN)

while DATAINPUTTED < 2:
    YEAR = 1960
    CHOICE = 0
    CHOICE1 = 0
    CHOICE2 = 0
    IMMIGRATIONPERCENT = 0.016
    MIGRATIONPERCENT = 0.00037
    TAXES = 0.05
    POPULATION = 67000000
    WORKEFFICIENCY = 0.6
    PUBLICSPENDING = 13414*POPULATION
    MIGRATION = int(MIGRATIONPERCENT * POPULATION)
    IMMIGRATION = int(IMMIGRATIONPERCENT * POPULATION)
    WORKINGAGEPOPULATION = 0.8 * POPULATION
    UNEMPLOYEDPOPULATION = 0.2 * POPULATION
    RICHPOPULATION = 0.1 * POPULATION
    RICHPOPULATIONVALUE = RICHPOPULATION * 100
    WORKINGPOPULATIONVALUE = (WORKEFFICIENCY * WORKINGAGEPOPULATION) * (24 * 7) * 350
    TOTALSALARIESPAID = WORKINGAGEPOPULATION * 400
    TOTALWELFARE = UNEMPLOYEDPOPULATION * 150
    TOTALSCORE = 0
    VALUEOFTOWN = WORKINGPOPULATIONVALUE + RICHPOPULATIONVALUE - TOTALWELFARE - TOTALSALARIESPAID
    while YEAR < 2040:
        POPULATION = POPULATION-MIGRATION+IMMIGRATION
        YEAR += 1
        MIGRATION = int(MIGRATIONPERCENT * POPULATION)
        WORKINGAGEPOPULATION = 0.8 * POPULATION
        UNEMPLOYEDPOPULATION = 0.2 * POPULATION
        RICHPOPULATION = 0.1 * POPULATION
        VALUEOFTOWN = WORKINGPOPULATIONVALUE + RICHPOPULATIONVALUE - TOTALWELFARE - TOTALSALARIESPAID
        TOTALSALARIESPAID = WORKINGAGEPOPULATION * 400
        TOTALWELFARE = UNEMPLOYEDPOPULATION * 150
        POPULATIONSTARTOFYEAR = POPULATION
        MILITARYSPENDING = 0.2 * VALUEOFTOWN
        #if MIGRATION > 0:
        #    POPULATION += MIGRATION
        #elif MIGRATION < 0:
        #    POPULATION += MIGRATION

        #if POPULATION <= 10000:
        #    print("You lost, the town got too small. Try again.")
        #    YEAR = 2040

        #if TAXES > 0.05:
        #    MIGRATIONPERCENT -= 0.004
        #    if TAXES > 0.055:
        #        MIGRATIONPERCENT -= 0.0045
        #elif TAXES < 0.05:
        #    MIGRATIONPERCENT += 0.004
        #    if TAXES < 0.03:
        #        MIGRATIONPERCENT += 0.0045

        MIGRATIONPERCENT = round(MIGRATIONPERCENT, 4)
        #Crisis = random.uniform(0, 40)

        #if 0 <= Crisis <= 20:
        #    POPULATION += 3000
        #elif 20 <= Crisis <= 40:
        #    POPULATION -= 3000

        #CHOICE = random.randint(1, 2)
        # CHOICE = input("Do you increase(1) or decrease(2) taxes.")
        #if CHOICE == 1:
        #    TAXES += 0.005
        #    CHOICE1 += 1
        #elif CHOICE == 2:
        #    TAXES -= 0.005
        #    CHOICE2 += 1
        #else:
        #    TAXES = TAXES
        #    print("CHOICE is broken")

        POPULATIONENDOFYEAR = POPULATIONSTARTOFYEAR
        POPULATIONCHANGE = (POPULATIONENDOFYEAR-POPULATIONSTARTOFYEAR)/POPULATIONSTARTOFYEAR

        WY = print("The year ", YEAR),
        MI = print("MIGRATION", MIGRATION),
        PO = print("POPULATION", POPULATION),
        TR = print("Tax rate", round((TAXES * 100), 2), "%"),
        MP = print("MIGRATION percent", MIGRATIONPERCENT),
        if VALUEOFTOWN > 1000000000:
            VALT = print("Value of the town ", int(VALUEOFTOWN)/1000000000, "billion"),
        else:
            print("Value of the country ", int(VALUEOFTOWN))
        SALP = print("Salaries paid this year ", int(TOTALSALARIESPAID)),
        WELP = print("Welfare paid this year ", int(TOTALWELFARE)),
        print("You increased taxes ", CHOICE1, "times.")

        TOTALSCORE += VALUEOFTOWN

        # time.sleep(2)

    print("You changed taxes ", CHOICE1, "times.")
    if CHOICE1 > 5:
        print("Perhaps too much...")
        print(CHOICE1)
    if CHOICE2 > 5:
        print("Perhaps too little...")
        print(CHOICE2)

    print(TOTALSCORE)
    RoundTaxes = round((TAXES * 100), 2)

    YAR = "Final year " + str(YEAR)
    if TOTALSCORE>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TOTALSCORE)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TOTALSCORE)
    MAR = "MIGRATION in final year " + str(MIGRATION)
    PAR = "POPULATION in final year " + str(POPULATION)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "MIGRATION percent in final year " + str(MIGRATIONPERCENT)
    VALT = "Value of the town in final year " + str(VALUEOFTOWN)
    TOTLSAL = "Salaries paid in final year " + str(TOTALSALARIESPAID)
    TOTALWEL = "Welfare paid in final year " + str(TOTALWELFARE)
    TAXINC = "Tax changes " + str(CHOICE1)

# The save to file functions are in progress, though it's possible to print all to a file, comparative pairs
# direct to an Excel file would be easiest to recursively compare.

    Name = "Scores" + AMOUNTWRITTEN +   MODE + ".txt"
    os.chdir('C:\\Users\\kbudz\\PycharmProjects\\Economy\\EconomySimulationFiles\\EconomyLogFiles')
    with open(Name, 'a', encoding="utf-8") as fp:
        fp.write("\n")
        if MODE == "all":
            MODE = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in  MODE:
            with open(("TOTALSCORE" + Name), "a", encoding="utf-8") as tsfp:
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

        fp.close()

    DATAINPUTTED += 1
    YEAR = 1960
# Draft choices
# print("    3)Invest in infrastructure?")
# CHOICE=input("What option do you take?")
#        elif CHOICE==3:
#   INFRASTRUCTURE+=1
#    MoneyAvailable-=1000
#    CHOICE3+=1
#   print(CHOICE3T)
#    print("Infrastructure",INFRASTRUCTURE)
# CHOICE3=0
# print(CHOICE3)
# print(INFRASTRUCTURE)
# CHOICE3T="Increase Infrastructure"
# INFRASTRUCTURE=0

# Compatibility for variable change at beginning and any point of program

# Time simulation weekly

# The choice to interrupt, pause simulation to make choices

#  Saviour events:
# if MIGRATIONPERCENT > 0.1:
#    MIGRATIONPERCENT = 0.05
#    POPULATION += 10
#    print("MIGRATION reset to 0.05,Consider balancing taxes.")
# the very first event based scripts
# if TAXES<0.03:
#    TAXES=0.05
#    MoneyAvailable-200
#    print("TAXES reset to 0.05, are you trying to go broke or something?")

# GDP based option. Goal is to get as many people as possible

