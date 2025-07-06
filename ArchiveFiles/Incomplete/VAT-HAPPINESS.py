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

#This citizen simulation should be done to simulate an average salary, average lifespan and other things
#To make it usable there will have to be a upper and lower bound based on the normal distribution of the said
#Variables

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


#Next steps
#To implement fully VAT And Happiness
#add VAT to variables
#add Happiness to variables
#Create an option to introduce VAT yourself, program it so that by putting x% vat, it will
#Use a suitable amount of happiness change, and suitable change in vatincome. Search
#up how much goods a person in a country like the UK uses, another for a second class country like
#Greece, and then perhaps a 3rd class
#More range for happiness, below 60 or above 80 a bigger impact is needed on the economy
#Buying habits
#Emigration
#All of these should be negatively impacted
#VAT:HAPPINESS
#4% + 5% Happiness
#5% +- 0% Happiness
#6% -5% Happiness

#Assuming each family of the sample buys a bottle of wine once a week for a
#yea, this code shows how the amount of Income from VAT changes with changes
#to % changes in VAT

"""

Year = 2023
Month = 5
while Year != 2024 and Month != 5:
    HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier)
    TotalIncomeFromVAT += VAT * (GoodConsumptionModifier * Population)
    Month += 1
    if Month == 12:
        Year += 1
        Month = 1

HAPPINESSRESULT(HappinessModifier)
FINANCIALRETURN = ("The government imposed a " , (VAT) , "% Value Added Tax, this earned\
 them " , (TotalIncomeFromVAT) , "from the sale of wine alone")
SOCIALRETURN = ("The citizens felt " , (HappinessResult) , "With the current \
                state of affairs")
                
print(FINANCIALRETURN)
print(SOCIALRETURN)

Introduce tests per each chunk of code, e.g. setup, variable introduction, running, functions
file saving, each should have a few in a "Testing" file, but not in release to speed it up
Need to speed up the running of the code, file saving can be made optional, by using an aditional
line of options:
Release, Testing
Release runs the code and dialogue ONLY
Testing also runs the tests and saves to a file your stats.
Filesaving = false for release essentially
"""

TESTING = True
VAT = ""
Population = 5000
GoodConsumptionModifier = 52
HappinessModifier = 65
TotalIncomeFromVAT = 0

VAT = int(input("Choose 4, 5, 6 for VAT "))        
VATLoop = True
while VATLoop == True:
    if VAT == 4:#%
        HappinessModifier += 5#% happiness
        VATLoop = False
    if VAT == 5:#%
        HappinessModifier += 0#% happiness
        VATLoop = False
    if VAT == 6:#%
        HappinessModifier += -5#% happiness
        VATLoop = False
    else:
        VATLoop = False
"""
while TESTING == True:
    if VAT != int:
        #
    while VAT != int:
        VAT = int(input("Choose 4, 5, 6 for VAT"))
        continue
"""

def HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier):
    if HappinessModifier == 60:
        Population -= GoodConsumptionModifier
        HappinessModifier -= 0.5
    if HappinessModifier == 65:
        Population += GoodConsumptionModifier
        HappinessModifier += 0.5
    if HappinessModifier == 70:
        Population += GoodConsumptionModifier * 1.2
        HappinessModifier += 0.75
        
def HAPPINESSRESULT(HappinessModifier):
    global HappinessResult
    if HappinessModifier <= 50:
        HappinessResult = ("Unhappy")
    if 50 <= HappinessModifier <= 70:
        HappinessResult = ("Satisified")
    if HappinessModifier <= 50    :
        HappinessResult = ("Overjoyed")

