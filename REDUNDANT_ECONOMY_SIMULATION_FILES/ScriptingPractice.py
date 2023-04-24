import random
from random import randint

A1="One"
A2="Two"
A3="Three"
A4="Four"
B1="Five"
B2="Six"
B3="Seven"
B4="Eight"
C1="ELECTION"
C2="TAXRATECHANGE"
C3="INTERESTRATECHANGE"
C4="Twelve"
PRE_DEFINED_SCRIPTS = [A1,A2,A3,A4]
SEMI_PRE_DEFINED_SCRIPTS = [B1,B2,B3,B4]
NAMED_SCRIPTS = [C1,C2,C3,C4]
SCRIPT_NUMBER = random.randint(1,12)
SCRIPTS = (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4)
CHOSEN_SCRIPT = SCRIPTS[SCRIPT_NUMBER-1]
if "One" in CHOSEN_SCRIPT:
    print("One  /"
          "                    ") # Description
                                  # Description part 2
if "Two" in CHOSEN_SCRIPT:
    print("Two   /"
          "                    ") # Description
                                  # Description part 2
if "Three" in CHOSEN_SCRIPT:
    print("Three   /"
          "                    ") # Description
                                  # Description part 2
if "Four" in CHOSEN_SCRIPT:
    print("Four   /"
          "                    ") # Description
                                  # Description part 2
if "Five" in CHOSEN_SCRIPT:
    print("Five   /"
          "                    ") # Description
                                  # Description part 2
if "Six" in CHOSEN_SCRIPT:
    print("Six   /"
          "                    ") # Description
                                  # Description part 2
if "Seven" in CHOSEN_SCRIPT:
    print("Seven   /"
          "                    ") # Description
                                  # Description part 2
if "Eight" in CHOSEN_SCRIPT:
    print("Eight   /"
          "                    ") # Description
                                  # Description part 2          
if "ELECTION" in CHOSEN_SCRIPT:
    print("Election time!/"
          "The new prime minister is ...") # Should be integrated with political leader variable at some point
                                           # Calculated by party popularity defined by money, nepotism whatverthefuck...
if "TAXRATECHANGE" in CHOSEN_SCRIPT:
    print("Tax Rate Change/"
          "                    ") # Description
                                  # Description part 2
if "INTERESTRATECHANGE" in CHOSEN_SCRIPT:
    print("Interest rate change/"
          "                    ") # Description
                                  # Description part 2
if "Twelve" in CHOSEN_SCRIPT:
    print("twelve/"
          "                    ") # Description
                                  # Description part 2


