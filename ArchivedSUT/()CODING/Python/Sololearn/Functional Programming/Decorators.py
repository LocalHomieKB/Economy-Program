def decor(func):
    def wrap():
        print("=========")
        func()
        print("=========")
    return wrap

def print_text():
    print("Hello World!")

decorated = decor(print_text)
decorated()

def print_text():
    print("Hello world!")

print_text = decor(print_text)

@decor
def print_text():
    print("Hello world!")