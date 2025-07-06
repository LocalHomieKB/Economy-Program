import time
from time import sleep
import random
from random  import randint
AMOUNT_WRITTEN=0
MODE = "all"
with open("FileNumber.txt", "w+", encoding="utf-8") as fp:
        fp.write("")
        fp.close
YEAR = 1960
TAXINCOME = 50000
POPULATION = 5000
WORK_EFFICIENCY = 0.6
PUBLIC_SPENDING = 20000
IMMIGRATION_RATE = 0.05
WORKING_AGE_POPULATION = 3000
UNEMPLOYED_POPULATION = 500
TOTAL_SALARIES_PAID = 15000
LITERACY = 0.5
TOTAL_WELFARE = 1000
GDP = 100000
YEARLY_MORTALITY_RATE = 0.035
HEALTHCAREEFFICIENCY = 0.6
ECONOMICDEVELOPMENT = 0.5
HOMELESSRATE = 0.05
while YEAR != 1970:
    POPULATION_START_OF_YEAR = POPULATION
    print("Year ", (YEAR))
    YEAR += 1
    LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
    PUBLIC_SPENDING = 0.1 * GDP
    HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4)
    POPULATION += 100
    WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
    UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
    TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
    TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
    TAXINCOME = POPULATION * 10
    CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
    POPULATION_END_OF_YEAR = POPULATION
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
        fp.close() #run time 0.251 seconds, should be quicker, what can we
        # speed up? File system removal, on the go variable changes
        
#VAT:HAPPINESS
#4% + 5% Happiness
#5% +- 0% Happiness
#6% -5% Happiness

#Assuming each family of the sample buys a bottle of wine once a week for a
#yea, this code shows how the amount of Income from VAT changes with changes
#to % changes in VAT
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
        GoodConsumptionModifier += 1
        VATLoop = False
    if VAT == 5:#%
        HappinessModifier += 0#% happiness
        GoodConsumptionModifier += 0
        VATLoop = False
    if VAT == 6:#%
        HappinessModifier += -5#% happiness
        GoodConsumptionModifier += -1
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

YearsRun = 0
while (YearsRun < 12):
    HAPPINESSCHECK(Population, HappinessModifier, GoodConsumptionModifier)
    TotalIncomeFromVAT += VAT * (GoodConsumptionModifier * Population)
    YearsRun += 1

HAPPINESSRESULT(HappinessModifier)
VAT = (str(VAT))
TotalIncomeFromVAT = (str(TotalIncomeFromVAT))
FINANCIALRETURN = "The government imposed a " + (VAT) + "% Value Added Tax, this earned\
 them " + (TotalIncomeFromVAT) +  " from the sale of wine alone"
SOCIALRETURN = "The citizens felt " + (HappinessResult) + " With the current \
state of affairs"
                
print(FINANCIALRETURN)
print(SOCIALRETURN)
print(HappinessModifier)

