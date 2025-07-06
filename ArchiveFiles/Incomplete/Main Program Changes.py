import time
from time import sleep
import random
from random  import randint
import sys
from sys import exit

print("Working Name is currently Simulacra or EconomyProgram1.11")
#old Comment:"One simulation should be based on the 
#economy of Greece before during and after the Troika program"

#<No runnable code before this point>

#Relatively Streamlined Main program code
while YEAR != 1970:
    POPULATION_START_OF_YEAR = POPULATION
    print("Year ", (YEAR))
    YEAR += 1
    LITERACY += TOTAL_WELFARE * 0.00001 - LITERACY * 0.01 + 0.005
    PUBLIC_SPENDING = 0.1 * GDP
    HEALTHCAREEFFICIENCY = ((PUBLIC_SPENDING / 1000000) / 2 + 0.4)
    POPULATION += 100
    WORKING_AGE_POPULATION = (0.6 * POPULATION) - (HOMELESSRATE * POPULATION)
    UNEMPLOYED_POPULATION = (0.1 * POPULATION) + (HOMELESSRATE * POPULATION)
    TOTAL_SALARIES_PAID = WORKING_AGE_POPULATION * 5
    TOTAL_WELFARE = (UNEMPLOYED_POPULATION * 2) + (HOMELESSRATE * POPULATION * 4)
    TAXINCOME = POPULATION * 10
    CAPITAL_AVAILABLE = TAXINCOME - TOTAL_WELFARE - TOTAL_SALARIES_PAID - PUBLIC_SPENDING 
    POPULATION_END_OF_YEAR = POPULATION
    """
    #END OF YEAR CHECKS
    #Need more scripts without using too much space
    """
    if YEAR % 2 == 0:
        script_process(TAXINCOME)
    PACEUNDECIDED = True
    while PACEUNDECIDED == True:
        if PACE == 0:
            PACEUNDECIDED = False
        else:
            time.sleep(PACE)
            PACEUNDECIDED = False
    """
    """
    if ECONOMICDEVELOPMENT > 0.5:
        IMMIGRATION_RATE += 0.01
        HOMELESSRATE -= 0.001
    