import numpy as np
def WealthEvent(SALARY):
    SYMBOLCHANGE = np.random.choice(['POSITIVE','NEGATIVE'], 10, p =[0.5,0.5])
    if 'POSITIVE' in SYMBOLCHANGE:
        SYMBOLCHANGE = 1
    else:
        SYMBOLCHAMGE = -1
    PERCENTAGECHANGE = np.random.choice(['1p','2p','3p','4p','5p','6p','7p','8p','9p', '10p'], 10, 
                     p =[0.5,0.25,0.125,0.0625,0.03125,0.015625,0.0078125,0.0039,0.00195,0.00098])
    if '1p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.01 * SYMBOLCHANGE)
    elif '2p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.02 * SYMBOLCHANGE)
    elif '3p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.03 * SYMBOLCHANGE)
    elif '4p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.04 * SYMBOLCHANGE)
    elif '5p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.05 * SYMBOLCHANGE)
    elif '6p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.06 * SYMBOLCHANGE)
    elif '7p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.07 * SYMBOLCHANGE)
    elif '8p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.08 * SYMBOLCHANGE)
    elif '9p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.09 * SYMBOLCHANGE)
    elif '10p' in PERCENTAGECHANGE:
        return SALARY + ((SALARY) * 0.1 * SYMBOLCHANGE)