
#29/09/2026 14:00-16:00
#D00290718


#New Exercise sheet: Constructors & Encapsulation File PDF

class Rectangle:

    #Exercise A3) on the new worksheet :
    def __init__(self, length, width, colour = "blue"):
        #Reminder: Whenever you create a method in a class, you need to:
        self.length = length
        self.width = width
        self.colour = colour

    def display(self): #Ex. B2 function
        format = f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]"
        return format #Had to add this so that Ex. B4 would work.

    #EXERCISE B3 FUNCTION
    def calc_area(self):
        area = self.length * self.width
        return area


if __name__ == "__main__":
    #Exercise A3) on new worksheet:
    length = 50
    width = 40
    obj = Rectangle(length, width)

    print(f"Length: {obj.length}")
    print(f"Width: {obj.width}")
    print(f"colour: {obj.colour}")

    print(obj.display())

    #Ex. B3 :

    area = obj.calc_area()
    print(f"Area of rectangle LxW = {area}")


#Commit your code after your method is complete and functions correctly.


