import random

class Country:
    def __init__(self,name, GDP, IR, IMPORT, EXPORT, POP):
        self.name=name#name
        self.GDP=GDP*1000000000#trillions
        self.IR=IR #%
        self.IMPORT=IMPORT*100000000 #billions
        self.EXPORT=EXPORT*100000000 #billions
        self.POP=POP#millions
c1=Country("United Garudos",3.187,3,159.3,96.7,67.33)#Republic of conservative democrats, since
#Forgotten grudges or wars. Simply develop economy
c2=Country("Salaam",0.75, 3,0,)
#a too small
#b competitive interest
#

dir(c1)
