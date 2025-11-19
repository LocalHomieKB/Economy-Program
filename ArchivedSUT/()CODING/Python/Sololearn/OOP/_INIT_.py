class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def bark(self):
        print("Woof!")

felix = Cat("ginger",4)
print(felix.color)

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

Rec1 = Rectangle(7,8)
print(Rec1.width)