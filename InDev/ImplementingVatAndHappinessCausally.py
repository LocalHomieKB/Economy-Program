#VAT:HAPPINESS
#4% + 5% Happiness
#5% +- 0% Happiness
#6% -5% Happiness
TESTING = True
VAT = ""
while TESTING == True:
    if VAT != int:
        VAT = int(input("Choose 4, 5, 6 for VAT"))
    while VAT != int:
        VAT = int(input("Choose 4, 5, 6 for VAT"))
        continue
        
PROGRAMLOOP = True
while PROGRAMLOOP == True:
    if VAT == 4:#%
        HappinessModifier = 5#% happiness
    if VAT == 5:#%
        HappinessModifier = 0#% happiness
    if VAT == 6:#%
        HappinessModifier = -5#% happiness

VAT * GoodConsumptionModifier = IncomeFromVAT
