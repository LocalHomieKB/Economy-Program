import time
AVAILABLE=15
CURRENT=3
MAX=5
MIN=2
LIGHT=0
action=LIGHT=-1
if CURRENT>=MIN:
    LIGHT=60
    if CURRENT>=3:
        LIGHT=80
        if CURRENT>=4:
            LIGHT=100
print(LIGHT)
A=0
while A!=30:
    def periodic(scheduler, interval, action, actionargs=()):
        scheduler.enter(interval, 0.02, periodic,
                        (scheduler, interval, action, actionargs))
        action(actionargs)
    print(LIGHT)
    if AVAILABLE!=0:
        LOGADD=input("Do you add a log(1Y 2N)?")
        if LOGADD=="1":
            CURRENT+=1
        if LOGADD=="end":
            exit()
    if CURRENT>=MIN:
        LIGHT=60
        if CURRENT>=3:
            LIGHT=80
            if CURRENT>=4:
                LIGHT=100
    A+=1          
