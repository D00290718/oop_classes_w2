
#28/09/2026 12:00-14:00
#D00290718

#Exercise b1:

class Rectangle:

    def __init__(self):
        #Reminder: Whenever you create a method in a class, you need to:
        self.length = 50
        self.width = 50
        self.colour = "green"

    def method(self):
        format = f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]"
        print(format)

if __name__ == "__main__":
    obj = Rectangle()

    print(f"Length: {obj.length}")
    print(f"Width: {obj.width}")
    print(f"colour: {obj.colour}")

    obj.method()

#Exercise B2

#Commit your code after your class is complete, including your method.

