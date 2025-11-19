#Following is a pure function, they have no side effects and return a value that only depends on their arguments, e.g.
#cos(x) will give the same number for the same value of x

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)



some_list = []

def impure(arg):
  some_list.append(arg)