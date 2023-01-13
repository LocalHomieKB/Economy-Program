"""
An interactive tech demo to teach economics.
Goals for this program:
Your success in the simulation is based on your total score as well as your final year score
Do better in these than in a simulation with no changes added, and you will be a winner
The only variable that needs changing should be the OS directory. Usually a subfolder exists
below the economy folder but my understanding of GitHub prevents me from doing this.
Any questions should be directed to my GitHub project. Constructive criticism is appreciated
especially from a data analysis standpoint as that is the direction this project is going towards
The average score for the game is equal to playing it with no tax tampering whatsoever
This is equal to:TOTAL_SCORE = 90348800000 VALUE_OF_TOWN = 1129360000
"""

import time
from time import sleep
import random

WORKING_NAME = "Simulacra" # One simulation should be based on the economy of Greece before during and after the Troika program
POPULATION = 5000
WEEKLY_UPDATES = False
YEARLY_UPDATES = False

#Scan the variable INPUT_SCOPE before the program runs to
def SCOPE(INPUT_SCOPE):
    INPUT_SCOPE = input("Choose either Weekly or Yearly"\
    "If Weekly the program runs for a year with weekly updates of 52"\
    "If Yearly the programs runs for 20 years with yearly updates of 20")

def CRIME(CRIME_RATE):
    if SCOPE == YEAR:
        CRIME = 520
    elif SCOPE == WEEK:
        CRIME = 52 # criminal events a year, converitble to weeks if needed

def datainputter(TAXES,POPULATION,WORK_EFFICIENCY,PUBLIC_SPENDING,
            IMMIGRATION_RATE,WORKING_AGE_POPULATION,UNEMPLOYED_POPULATION,
            TOTAL_SALARIES_PAID,TOTAL_WELFARE,YEAR,CRIME,LITERACY,GDP,YEARLY_MORTALITY_RATE,
            ASSETS, HEALTHCARE)
    #Natural year by year evolution must be influenced by scripts, events so on
    #The random events are either in file, or out of file retrieved by open...
    while YEAR<2020 or KeyboardInterrupt:
        print("Year ", (YEAR))
        YEAR += 1
        LITERACY += TOTAL_WELFARE * 0.001 - LITERACY * 0.01
        PUBLIC_SPENDING = 0.4 * GDP
        HEALTHCARE = (1000 * PUBLIC_SPENDING * 1)
        YEARLY_MORTALITY_RATE = ((((2/3) * 0.0076 * POPULATION)"""Elderly Death""" + (0.0024 * POPULATION))
        """Health Related Deaths""" / POPULATION)
        IMMIGRATION_RATE = 0.005 * POPULATION - (CRIME * 1000) + (HEALTHCARE * 1000) - (YEARLY_MORTALITY_RATE * POPULATION)
        POPULATION =(1000 * IMMIGRATION_RATE * 0.06) - (YEARLY_MORTALITY_RATE)
        CRIME = 0.07952 * POPULATION
        WORKING_AGE_POPULATION = 0.8 * POPULATION
        GDP = WORK_EFFICIENCY * (0.6 * POPULATION) + ASSETS
        TOTAL_SALARIES_PAID = POPULATION * 0.6 * 400
        TOTAL_WELFARE = UNEMPLOYED_POPULATION * 150
        time.sleep(PACE)

#Beginning of program load
while not "1 2 3" in PACE:
    PACE = input("Slow or Fast or rapid Pace(input 1 or 2 or 3)"\
        "If slow then data updates every 3 seconds"\
        "If fast then data updates every 0.5 seconds"\
        "If rapid then data has no update and simply gives you final results ASAP(for data collection")

datainputter(YEAR = 1960,
    TAXES = 0.05,
    POPULATION = 67000000,
    WORK_EFFICIENCY = 0.6,
    LITERACY = 0.8)
A1=""
A2=""
A3=""
A4=""
B1=""
B2=""
B3=""
B4=""
C1="ELECTION"
C2=""
C3=""
C4=""
PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
SEMI_PRE-DEFINED_SCRIPTS = [B1,B2,B3,B4]
NAMED_SCRIPTS = [C1,C2,C3,C4]
def pick_script(SCRIPT)
    SCRIPT = random.(0:13)
    CHOSEN_SCRIPT = SCRIPT/12
    if SCRIPT<=1:
    elif 1<SCRIPT<=2
    elif 2<SCRIPT<=3

if "Election" in CHOSEN_SCRIPT:
    print("Election time!/"
          "The new prime minister is ...") # Should be integrated with political leader variable at some point
                                           # Calculated by party popularity defined by money, nepotism whatverthefuck...