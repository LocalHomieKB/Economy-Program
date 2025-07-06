#For simulating the economy around the simulation
PERIOD = ("a")
TRADERS = randint(2,5) # For a random market x there will exist 2 to 5 traders who have an interest in it:
#Shorting it or investing in it may be decided later, this is a visual template.
COMMODITIES = randint(2,20) # For a random market x there exists 2 to 20 commodities that can be interacted with.
def TIME():
    CURRENTTIME = 0
    for i in PERIOD:
        CURRENTTIME += 1