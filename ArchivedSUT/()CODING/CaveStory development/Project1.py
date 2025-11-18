def addition():
    try:
        print(firstnumber + secondnumber)
    except:
        print("An error occured")

def multiply():
    try:
        print(firstnumber * secondnumber)
    except:
        print("An error occured")

def divide():
    try:
        print(firstnumber / secondnumber)
    except:
        print("An error occured")

def subtract():
    try:
        print(firstnumber - secondnumber)
    except:
        print("An error occured")


firstnumber = input("Put in your first number")
secondnumber = input("Input your second number") 
choice = input("What calculation would you like today?")
if choice == ("add") or ("+") or ("Addition"):
    addition()
elif choice == ("multiply") or ("*"):
    multiply()
elif choice == ("minus") or ("subtract") or ("-"):
    subtract()
elif choice == ("divide") or ("/") or ("division"):
    divide()
else:
    print("Please try again")
