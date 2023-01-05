"""
Provides an in depth simulation of an economy akin to the UK
"""
# Goals for this program:
# A realistic simulation of a city - Not achieved
# The average score for the game is equal to playing it with no tax tampering whatsoever
# This is equal to:TOTAL_SCORE = 90348800000
# VALUE_OF_TOWN = 1129360000
# Your success in the simulation is based on your total score as well as your final year score
# Do better in these than in a simulation with no changes added, and you will be a winner
# The only variable that needs changing should be the OS directory. Usually a subfolder exists
# below the economy folder but my understanding of GitHub prevents me from doing this.
# Any questions should be directed to my GitHub project. Constructive criticism is appreciated
# , especially from a data analysis standpoint as that is the direction this project is
# going towards
import os
import random
os.chdir("/workspaces/Economy-Program/EconomySimulationFiles")
DATA_INPUTTED = 0
MODE = str(input("Input mode "))
with open("File_Number.txt", "r+", encoding="utf-8") as fp:
    Content = fp.readlines()
    AMOUNT_WRITTEN = int(Content[0])
    AMOUNT_WRITTEN += 1
    fp.close()
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
    fp.write(str(AMOUNT_WRITTEN))
    fp.close()
AMOUNT_WRITTEN = str(AMOUNT_WRITTEN)
while DATA_INPUTTED < 2:
    YEAR = 1960
    CHOICE = 0
    CHOICE1 = 0
    CHOICE2 = 0
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
    - TOTAL_SALARIES_PAID)
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
        fp.close()
    DATA_INPUTTED += 1
    YEAR = 1960
