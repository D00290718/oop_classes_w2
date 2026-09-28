
#28/09/2026 12:00-14:00
#D00290718

#Exercise b1:

class Rectangle:

    def __init__(self):
        #Reminder: Whenever you create a method in a class, you need to:
        self.length = 50
        self.width = 50
        self.colour = "green"

    def display(self): #Ex. B2 function
        format = f"Rectangle[length={self.length}, width={self.width}, colour={self.colour}]"
        return format #Had to add this so that Ex. B4 would work.

    #EXERCISE B3 FUNCTION
    def calc_area(self):
        area = self.length * self.width
        return area


if __name__ == "__main__":
    obj = Rectangle()

    print(f"Length: {obj.length}")
    print(f"Width: {obj.width}")
    print(f"colour: {obj.colour}")

    print(obj.display())

    #Ex. B3 :

    area = obj.calc_area()
    print(f"Area of rectangle LxW = {area}")


#Commit your code after your method is complete and functions correctly.


