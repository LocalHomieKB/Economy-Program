# Goals for this program:
# A realistic simulation of a city - Not achieved

# The average score for the game is equal to playing it with no tax tampering whatsoever
# This is equal to:
# Your success in the simulation is based on your total score as well as your final year score
# Do better in these than in a simulation with no changes added, and you will be a winner

import os
import sys

sys.path.append(os.path.realpath('..'))

DataInputted = 0

Mode = str(input("Input mode "))

with open("FileNumber.txt", "r+") as fp:
    Content = fp.readlines()
    AmountWritten = int(Content[0])
    AmountWritten += 1
    fp.close()
with open("FileNumber.txt", "w+") as fp:
    fp.write(str(AmountWritten))
    fp.close()
AmountWritten = str(AmountWritten)

while DataInputted < 2:
    Year = 1960
    Choice = 0
    Choice1 = 0
    Choice2 = 0
    ImmigrationPercent = 0.016
    MigrationPercent = 0.00037
    Taxes = 0.05
    Population = 67000000
    WorkEfficiency = 0.6
    PublicSpending = 13414*Population
    Migration = int(MigrationPercent * Population)
    Immigration = int(ImmigrationPercent * Population)
    WorkingAgePopulation = 0.8 * Population
    UnemployedPopulation = 0.2 * Population
    RichPopulation = 0.1 * Population
    RichPopValue = RichPopulation * 100
    WorkingPopValue = (WorkEfficiency * WorkingAgePopulation) * (24 * 7) * 350
    TotalSalariesPaid = WorkingAgePopulation * 400
    TotalWelfare = UnemployedPopulation * 150
    TotalScore = 0
    ValueOfTown = WorkingPopValue + RichPopValue - TotalWelfare - TotalSalariesPaid
    while Year < 2040:
        Population = Population-Migration+Immigration
        Year += 1
        Migration = int(MigrationPercent * Population)
        WorkingAgePopulation = 0.8 * Population
        UnemployedPopulation = 0.2 * Population
        RichPopulation = 0.1 * Population
        ValueOfTown = WorkingPopValue + RichPopValue - TotalWelfare - TotalSalariesPaid
        TotalSalariesPaid = WorkingAgePopulation * 400
        TotalWelfare = UnemployedPopulation * 150
        PopulationStartOfYear = Population
        MilitarySpending = 0.2 * ValueOfTown
        #if Migration > 0:
        #    Population += Migration
        #elif Migration < 0:
        #    Population += Migration

        #if Population <= 10000:
        #    print("You lost, the town got too small. Try again.")
        #    Year = 2040

        #if Taxes > 0.05:
        #    MigrationPercent -= 0.004
        #    if Taxes > 0.055:
        #        MigrationPercent -= 0.0045
        #elif Taxes < 0.05:
        #    MigrationPercent += 0.004
        #    if Taxes < 0.03:
        #        MigrationPercent += 0.0045

        MigrationPercent = round(MigrationPercent, 4)
        #Crisis = random.uniform(0, 40)

        #if 0 <= Crisis <= 20:
        #    Population += 3000
        #elif 20 <= Crisis <= 40:
        #    Population -= 3000

        #CHOICE = random.randint(1, 2)
        # CHOICE = input("Do you increase(1) or decrease(2) taxes.")
        #if CHOICE == 1:
        #    Taxes += 0.005
        #    Choice1 += 1
        #elif CHOICE == 2:
        #    Taxes -= 0.005
        #    Choice2 += 1
        #else:
        #    Taxes = Taxes
        #    print("Choice is broken")

        PopulationEndOfYear = PopulationStartOfYear
        PopulationChange = (PopulationEndOfYear-PopulationStartOfYear)/PopulationStartOfYear

        print("The year ", Year),
        print("Migration", Migration),
        print("Population", Population),
        print("Tax rate", round((Taxes * 100), 2), "%"),
        print("Migration percent", MigrationPercent),
        if ValueOfTown > 1000000000:
            print("Value of the town ", int(ValueOfTown)/1000000000, "billion"),
        else:
            print("Value of the country ", int(ValueOfTown))
        print("Salaries paid this year ", int(TotalSalariesPaid)),
        print("Welfare paid this year ", int(TotalWelfare)),
        print("You increased taxes ", Choice1, "times.")

        TotalScore += ValueOfTown

        # time.sleep(2)

    print("You changed taxes ", Choice1, "times.")
    if Choice1 > 5:
        print("Perhaps too much...")
        print(Choice1)
    if Choice2 > 5:
        print("Perhaps too little...")
        print(Choice2)

    print(TotalScore)
    RoundTaxes = round((Taxes * 100), 2)

    YAR = "Final year " + str(Year)
    if TotalScore>1000000000:
        TOTLSCR = "Total Score " + str(round((int(TotalScore)/1000000000), 2)) + " billions"
    else:
        TOTLSCR = "Total Score " + str(TotalScore)
    MAR = "Migration in final year " + str(Migration)
    PAR = "Population in final year " + str(Population)
    TAXR = "Tax rate in final year" + str(RoundTaxes) + "%"
    MARPR = "Migration percent in final year " + str(MigrationPercent)
    VALT = "Value of the town in final year " + str(ValueOfTown)
    TOTLSAL = "Salaries paid in final year " + str(TotalSalariesPaid)
    TOTALWEL = "Welfare paid in final year " + str(TotalWelfare)
    TAXINC = "Tax changes " + str(Choice1)

    Name = "Scores" + AmountWritten + Mode + ".txt"
    os.chdir('C:\\Users\\kbudz\\PycharmProjects\\Economy\\EconomySimulationFiles\\EconomyLogFiles')
    with open(Name, 'a') as fp:
        fp.write("\n")
        if Mode == "all":
            Mode = "TSTMTPTTTMPTVTSPTWPTINC"
        if 'TS' in Mode:
            with open(("TotalScore" + Name), "a") as tsfp:
                tsfp.write(str(TOTLSCR))
                tsfp.close()
            with open(("Tax" + Name), "a") as trfp:
                trfp.write(str(TAXR))
                trfp.close()
        if 'TM' in Mode:
            fp.write("\n")
            fp.write(str(MAR))
        if 'TP' in Mode:
            fp.write("\n")
            fp.write(str(PAR))
        if 'TT' in Mode:
            fp.write("\n")
            fp.write(str(TAXR))
        if 'TMP' in Mode:
            fp.write("\n")
            fp.write(str(MARPR))
        if 'TV' in Mode:
            fp.write("\n")
            fp.write(str(VALT))
        if 'TSP' in Mode:
            fp.write("\n")
            fp.write(str(TOTLSAL))
        if 'TWP' in Mode:
            fp.write("\n")
            fp.write(str(TOTALWEL))
        if 'TINC' in Mode:
            fp.write("\n")
            fp.write(TAXINC)
        fp.write("\n")

        fp.close()

    DataInputted += 1
    Year = 1960
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
# if MigrationPercent > 0.1:
#    MigrationPercent = 0.05
#    POPULATION += 10
#    print("Migration reset to 0.05,Consider balancing taxes.")
# the very first event based scripts
# if TAXES<0.03:
#    TAXES=0.05
#    MoneyAvailable-200
#    print("Taxes reset to 0.05, are you trying to go broke or something?")

# GDP based option. Goal is to get as many people as possible

