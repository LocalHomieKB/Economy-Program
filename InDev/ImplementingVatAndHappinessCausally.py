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