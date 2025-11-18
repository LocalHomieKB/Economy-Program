import random
import sys
random.seed
Year=1960
YEARCURRENT=1960
CHOICE=0
CHOICE1=0
CHOICE2=0
MIGRATIONPERCENT=0.03
TAXES=0.05
POPULATION=40000#Similar to Newbury West Berkshire
CHANGE=input("Change any variables? \n")
MONEYAVAILABLE=0
open('LOGFORYEAR.txt', 'w').close()
while Year<2020:
    POPULATION1=POPULATION
    YEARCURRENT+=1
    #if MIGRATIONPERCENT>0.1:
    #    MIGRATIONPERCENT=0.05
    #    POPULATION+=10
    #    print("Migration reset to 0.05,Consider balancing taxes.")
        #the very first event based script^^
    #if TAXES<0.03:
    #    TAXES=0.05
    #    MONEYAVAILABLE-200
    #    print("Taxes reset to 0.05, are you trying to go broke or something?")
    MCYC=0
    TCYC=0
    POPCYC=0
    CHOCYC=0
    SALARY=32573#average salary in ENGLAND --ons.gov.uk
    MIGRATION=int(MIGRATIONPERCENT*POPULATION)
    GDP=((POPULATION*0.6)*SALARY)
    MONEYAVAILABLE+=(GDP*TAXES)
    while MCYC==0:
        if MIGRATION>0:
            POPULATION=POPULATION+MIGRATION
        elif MIGRATION<0:
            POPULATION=POPULATION+MIGRATION
        MCYC=1
    while TCYC==0:
        if TAXES>0.05:
            MIGRATIONPERCENT-=0.004
            if (TAXES>0.055)==True:
                MIGRATIONPERCENT-=0.0045
        elif TAXES<0.05:
            MIGRATIONPERCENT+=0.004
            if (TAXES<0.03)==True:
                MIGRATIONPERCENT+=0.0045
        MIGRATIONPERCENT=round(MIGRATIONPERCENT,4)
        TCYC=1
    CRISIS=random.uniform(0, 40)
    while POPCYC==0:
        if (0<=CRISIS<=20):
            POPULATION+=30
        #nothing happens between 20 and 60 currently
        elif (20<=CRISIS<=40):
            POPULATION-=30
        POPCYC=12
    while CHOCYC==0:
        CHOICE=random.randint(1,2)
        #CHOICE=input("Do you increase(1) or decrease(2) taxes.")
        if CHOICE=="1":
            TAXES+=0.005
            CHOICE1+=1
            print("Increase taxes")
        elif CHOICE=="2":
            TAXES-=0.005
            CHOICE2+=1
            print("Decrease taxes")
        CHOCYC=1
    Year+=1
    POPULATION2=POPULATION
    POPULATIONCHANGE=POPULATION2-POPULATION1
    print("The year ",Year)
    print("Money available",int(MONEYAVAILABLE))
    print("Migration",MIGRATION)
    print("Population",POPULATION)
    print("Population change this year",POPULATIONCHANGE)
    print("Tax rate",round((TAXES*100),2),"%")
    print("Migration percent",(MIGRATIONPERCENT))
    if POPULATION<=10000:
        print("You lost, the town got too small. Try again.")
        Year=2040
    print("\n")
    
    
print("You increased taxes ",CHOICE1, "times.")
if CHOICE1>5:
    print("Perhaps too much...")
if CHOICE2>5:
    print("Perhaps too little...")
print(CHOICE2)

print(YEARCURRENT)
print((round(GDP,2)))

#Draft choices
       # print("    3)Invest in infrastructure?")
       # CHOICE=input("What option do you take?")
        #        elif CHOICE==3:
        #   INFRASTRUCTURE+=1
        #    MONEYAVAILABLE-=1000
        #    CHOICE3+=1
         #   print(CHOICE3T)
            #    print("Infrastructure",INFRASTRUCTURE)
            #CHOICE3=0
            ##print(CHOICE3)
#print(INFRASTRUCTURE)
        #CHOICE3T="Increase Infrastructure"
    #INFRASTRUCTURE=0