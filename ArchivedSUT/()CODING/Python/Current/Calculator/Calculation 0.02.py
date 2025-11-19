#Calculations
numberss = 0
number1 = 0
number2 = 0
mathtype=0
onward =0
print("What calculation would you like to do?")
print("A for Addition")
print("S for Subtraction")
print("M for Multiplication")
print("D for Division")
print("P for Powers")
while mathtype == 0:
    choice = input()
    numberss=0
    if choice == "A":
        mathtype += 1
    elif choice == "S":
        mathtype += 2
    elif choice == "M":
        mathtype += 3
    elif choice == "D":
        mathtype += 4
    elif choice == "P":
        mathtype += 5
    else:
        print("Invalid option")
    while numberss ==0:
        del number1
        del number2
        del onward
        number1=float(input("Pick your first number"))
        number2=float(input("Pick your second number"))
        if mathtype ==1:
            print(number1+number2)
        elif mathtype ==2:
            print(number1-number2)
        elif mathtype ==3:
            print(number1*number2)
        elif mathtype ==4:
            print(number1/number2)
        elif mathtype ==5:
            print(number1**number2)
        onward=int(input("pick new numbers(1)? Different calculation(2)? finished calculating(3)?"))
        while onward>0:
            if onward ==1:
                onward =0
            elif onward ==2:
                numberss += 1
                mathtype =0
                onward=0
            elif onward ==3:
                mathtype += 1
                numberss += 1
                onward=0
