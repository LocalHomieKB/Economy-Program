def decor(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()
#This is optional, but can be useful ^^

@decor
def print_text():
    print("Hello world")

#Does the same thing^^