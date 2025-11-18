#Generators behave in a similar way to for loops, iterating through variables, with the "yield" statement
#saving the number to the variable without replacing it. e.g. for countdown it releases i to the function
#without replacing the variable, allowing a "countdown"
def countdown():
  i=5
  while i > 0:
    yield i
    i-=1

for i in countdown():
  print(i)




def infinite_sevens():
  while True:
    yield 7
        
for n in infinite_sevens():
  print(n)