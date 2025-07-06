#The first file saving option is longest,
#Easiest to understand. Needs to 
#be converted to the new variables


#Another file saving version
#Archivable data for consulting of future ideas
DATA_INPUTTED=0
MODE = str(input("Input mode "))

#Tests here in case of a change in variables:
"""
Either Define a few names for a variable
Check which variables exist, those that don't are 
automatically removed from being written in the file and
at the bottom of the file, or when the program finishes it says
which ones were missed
"""
#File save code for data analysis
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

#Version 2 

#Another version of file saving
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

#Version 3(Release Version Saving):
"""
#Needs to be at beginning:
AMOUNT_WRITTEN=0
WhatToWriteToFile = "all"
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
        fp.write("")
        fp.close

#Needs to be within the while loop of the program
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
        #New Code:
        FILEINPUTDETERMINED = False
        #^^^^^^^^^^^^^^^^^^^^^^^^^^
        #Separate file saving from main code completely. Or the same way it is.
        while FILEINPUTDETERMINED == False:
            if WhatToWriteToFile == "":
                FILEINPUTDETERMINED = True
            if WhatToWriteToFile == "all":
                WhatToWriteToFile = "WYMIPOTRSALPWELP"
            if "WY" in WhatToWriteToFile:
                fp.write(" " + WY + " " + "\n" )
            if "MI" in WhatToWriteToFile:
                fp.write(" " + MI + " " + "\n")
            if "PO" in WhatToWriteToFile:
                fp.write(" " + PO + " " + "\n")
            if "TR" in WhatToWriteToFile:
                fp.write(" " + TR + " " + "\n")
            if "SALP" in WhatToWriteToFile:
                fp.write(" " + SALP + " " + "\n")
            if "WELP" in WhatToWriteToFile:
                fp.write(" " + WELP + " " + "\n")           
            FILEINPUTDETERMINED = True
        fp.write("\n")

"""
