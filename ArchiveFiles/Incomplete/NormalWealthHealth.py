#Simulating the wealth of citizens
import numpy as np
import os
import sys
TESTS= False
def WealthEvent():
    SYMBOLCHANGE = 0
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 1, p =[0.5,0.5])
    global PERCENTAGECHANGE
    global HOLDINGSALARY
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHANGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 1, 
                     p =[0.5,0.25,0.125,0.06,0.03,0.02,0.008,0.004,0.002,0.001])
    if '1p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        HOLDINGSALARY += ((HOLDINGSALARY) * 0.1 * SYMBOLCHANGE)
    #Tests
    if TESTS == True:
        print(HOLDINGSALARY)
        print(SYMBOLCHANGE)
        print(PERCENTAGECHANGE)
class Citizen:
    def __init__(self, s):
        self.salary = s