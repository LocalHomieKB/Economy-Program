#Lambda essentially simplifies functions, but isn't compulsory to coding

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)