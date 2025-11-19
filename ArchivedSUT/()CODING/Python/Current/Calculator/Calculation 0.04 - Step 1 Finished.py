#Calculations
import math
import sys
mathtype=0
onward =0
programactive = True
numberss=0
choice = 0
while programactive == True:
    number1 = 0
    number2 = 0
    numberS = 0
    
    # Picking the Calculation type
    if choice == 0:
        print("What calculation would you like to do?")
        print("1 for Addition")
        print("2 for Subtraction")
        print("3 for Multiplication")
        print("4 for Division")
        print("5 for Powers")
        print("6 for Square root")

        choice = int(input())
        if choice <6:
            calculating = True
            rooting = False
        elif choice == 6:
            calculating = False
            rooting = True

    # The actual calculation
    if numberss ==0:
        if calculating == True:
            number1=float(input("Pick your first number"))
            number2=float(input("Pick your second number"))
        if choice<6:
            if choice ==1:
                print(number1+number2)
            elif choice ==2:
                print(number1-number2)
            elif choice ==3:
                print(number1*number2)
            elif choice ==4:
                print(number1/number2)
            elif choice ==5:
                print(number1**number2)
        elif rooting == True:
            numberS = int(input("What number would you like to squareroot?"))
            print(math.sqrt(numberS))
        numberss=1
        onward=int(input("pick new numbers(1)? Different calculation(2)? finished calculating(3)?"))

    # What happens after
    if onward>0:
        # Same calculation new numbers
        if onward ==1:
            onward =0
            choice = 1
            numbers = 0
        # New calculation new numbers
        elif onward ==2:
            onward=0
            choice = 0
            numberss = 0
        # Ends program
        elif onward ==3:
            exit()
           
