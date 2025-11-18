#Calculations
condition = 0
number1 = 0
number2 = 0
print("What calculation would you like to do?")
print("A for Addition")
print("S for Subtraction")
print("M for Multiplication")
print("D for Division")
choice = input()
while condition == 0:
    if choice == "A":
        condition += 1
    elif choice == "S":
        condition += 2
    elif choice == "M":
        condition += 3
    elif choice == "D":
        condition += 4
    else:
        print("Invalid option")

while condition>0:
    number1=int(input("Pick your first number"))
    number2=int(input("Pick your second number"))
    if condition ==1:
        answer = (number1+number2)
        print(answer)
    elif condition ==2:
        answer = (number1-number2)
        print(answer)
    elif condition ==3:
        answer = (number1*number2)
        print(answer)
    elif condition ==4:
        answer = (number1/number2)
        print(answer)
    onward=int(input("pick new numbers(1)? repeat calculation(2)? finished calculating(3)?"))
    while onward>0:
        if onward ==1:
            del number1
            del number2
            del answer
            onward =0
        elif onward ==2:
            print(answer)
            onward =0
            condition =0
        else:
            onwar =0
            condition =0
