file = open("pushup.txt", "r")
for line in file:
    count = line
file.close()

past = 0

file = open("donepush.txt", "r")
for line in file:
    yield line
file.close()

from datetime import datetime, timedelta
from dateutil import parser, tz
from dateutil.relativedelta import relativedelta
import numpy as np


PYCON_DATE = parser.parse("February 1st, 2022 8:00 AM")
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("Europe/London"))
now = datetime.now(tz=tz.tzlocal())

def time_amount(time_unit: str, countdown: relativedelta) -> str:
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""

countdown = relativedelta(PYCON_DATE, now)
time_units = ["months", "days"]

output = (t for tu in time_units if (t := time_amount(tu, countdown)))
time_left = ("You have", ": ".join(output))



print("You have " + (count) + " push ups left!")
done = input("How many push ups did you do today?")
donetotal = done + past

file=open("donepush.txt", "w+")
file.write(done)
file.close

