import numpy as np
import os
import sys
TESTS= False
def WealthEvent():
    SYMBOLCHANGE = 0
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
    global PERCENTAGECHANGE
    global HOLDINGSALARY
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHANGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
                     p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
    if '1p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
    #Tests
    if TESTS == True:
        print(HOLDINGSALARY)
        print(SYMBOLCHANGE)
        print(PERCENTAGECHANGE)
class Citizen:
    def __init__(self, s):
        self.salary = s
#Showing Python the path to my code        
directory = "citizensalarystorage"
parent_dir = "C:/Users/kbudz/Documents/GitHub/Economy-Program"
path = os.path.join(parent_dir, directory)
os.chdir(path) # This code assigns the current directory to the path seen above
#Helping with organisation

#Making the program accessible with sleep, a choice of continuing the citizen simulation,
#Citizen simulation will print the amount of years of simulation, each iteration
#Is one year.It can also let you create new citizens. Each citizen group should have their own name
#e.g. Citizens
print("New Simulation (N) \n Load Simulation (L) \n Exit (E)")
CHOICE = str(input())
SIMULATIONCHOSEN = False
NUMBEROFPREVIOUSSIMULATIONS = 0
while SIMULATIONCHOSEN == False:
    if "N" in CHOICE:
         NUMBEROFPREVIOUSSIMULATIONS += 1 # amount before this one
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")
    elif "L" in CHOICE:
         FILEWRITING = str("NEWCITIZENSALARIES.txt")
    elif "E" in CHOICE:
        sys.exit()
    else:
         FILEWRITING = str("NEWCITIZENSALARIES" + str((NUMBEROFPREVIOUSSIMULATIONS)) + ".txt")

# The following code can be used to make new directories exclusively even any parent directories:
# os.mkdir(path)
P1 = Citizen(30000)
P1.salary= 30000
with open(FILEWRITING, "w+", encoding="utf-8") as NCS:
                NCS.write("")
                NCS.close()
with open("CITIZENSALARIES.txt", "r", encoding="utf-8") as fp:
        CURRENTCITIZENCOUNT = 0
        while CURRENTCITIZENCOUNT < 20:
            CITIZENID = str(("P",str(CURRENTCITIZENCOUNT)))
            CITIZENID = Citizen(fp.readline())
            #Salary change
            HOLDINGSALARY = P1.salary
            WealthEvent()
            with open("NEWCITIZENSALARIES.txt", "a+", encoding="utf-8") as NCS:
                NCS.write(str(HOLDINGSALARY))
                NCS.write("\n")
                NCS.close()
            #End of Salary change

            #Need a test to see how many citizen numbers were printed, if below a certain
            #amount, the file is discarded and the while loop ended.
            #Try (name file), except if (CITIZENCOUNT < 20)

            CURRENTCITIZENCOUNT += 1
        fp.close()