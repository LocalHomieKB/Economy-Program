##The basic lines of code to find out the workout done, amounts of reps and sets as well
##For finding out the workout an array of names along with abbreviations may have to be memorised, later versions should contain a way for the program to scan the name and
##And try to guess what workout the user is referring to
##Its critical the process is quick to encourage people to do it every day


##Firstly the program should record the date and time of the workout done
##Also an option to edit an old workout

NEWWORKOUT = False
NEW=input(print("New workout? yes/no"))
if NEW == "yes":
    NEWWORKOUT==True

###if NEWWORKOUT==False:
    ##ask the date of the workout
    ##Ask the time if more than one recorded on the day
    ##Edit either a new workout to add or an recorded one to remove (may be difficult)

DATE=input(print("What date was the workout done?"))
##Code to ensure INT entered is necessary
TIME=input(print("Is the time recorded? (if yes enter afterwards)"))
if TIME == "yes":
    TIME=input()
else:
    TIME == "0"

f= open("WORKOUTS.txt","w+")
f.write("Add a new workout?")
## TO DO:
#Option to enter the workout performed as the code its been defined previously, the program takes the code, and either finds it in the txt file or lets the user enter
#a new workout