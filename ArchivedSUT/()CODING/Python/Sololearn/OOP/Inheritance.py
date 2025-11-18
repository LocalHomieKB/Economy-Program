class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat(Animal):  # Cat (a subclass), inherits from Animal (a superclass)
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def woof(self):
        print("Woof!")

fido = Dog("Fido", "Brown")
print(fido.color)
fido.woof()

class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print("Grrr...")

class Dog(Wolf):
    def bark(self):
        print("Woof") # If inherited attributes match, the subclass's (Dog) attributes
                      # Overrule
husky = Dog("Max" ,"grey")
husky.bark()

class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c =C()
c.method()
c.another_method()
c.third_method()

class A:
    def spam(self):
        print(1)
    
class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()