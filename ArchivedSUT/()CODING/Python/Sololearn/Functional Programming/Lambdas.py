#
def polynomial(x) :
    return x**2 + 5*x + 4
print(polynomial(-4))

print((lambda x: x**2 + 5*x + 4) (-4))
#

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))

#This could be done with a Lambda

result = list(map(lambda x: x+5, nums))
print(result)

#

res = list(filter(lambda x: x%2==0, nums))
print(res)