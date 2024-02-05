"""
for this i would need:
consumption events ( consumes food -5 food)
bandit events (steals food -5 food)
production ( whiskey making +10 food +20 money)
leadership ( hire sheriff -10 money bandits skip next days raid)
population ( endorse a visit from a travelling circus -10 food bandits skip next two raids)

variables food money
consumption
bandit
production
leadership or population or skip

let’s simply make this small part of the program, that’s it, no more events,
 no randomising just this simple static little visual text based game.
"""

"""
IMPORT SECTION
"""

from random import randint

""" 
NTRO AND DEFINITIONS
"""

print("Your people have 10 days to survive in the wild west... Good Luck")

FOOD = 30
MONEY = 50
PEOPLE = 10
DAYS = 7
BANDITSTRENGTH = 3 #(0 = lowest 3 = highest)

"""
PROGRAM LOOP
"""

while DAYS >= 0:
        if FOOD >= 5:
            print("Your people eat")
            FOOD -= 5
        else:
            print("Your people starve")
            PEOPLE -= 1

        BANDITEVENT = randint(0,1)
        if BANDITEVENT == 0:
            print("The bandits raid you")
            BANDITEVENTSUCCESS = randint(0,2)
            if BANDITEVENTSUCCESS:
                if BANDITEVENTSUCCESS == 2:
                    print("The bandits succeed in stealing your food")
                    FOOD -= 5
                else:
                    BANDITCHOICE = input("You beat back the bandits, do you rob them for food?(Y/N)")
                    if BANDITCHOICE == ("Y"):
                        FOOD += 3
                    else:
                        print("The defeat of the bandits discourages some from further raiding")
                        BANDITSTRENGTH -= 1
        if BANDITSTRENGTH == 0:
            print("With the bandits defeated your people can live indefinetly longer in the punishing wild west")
            DAYS = 0 
            