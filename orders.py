
#Exercises: Using Classes and Working With Encapsulation FilePDF
#06/10/26 14:00-16:00


# Exercise A1 Initial class

class Pizza:

    def __init__(self, toppings, size = "Medium"): #Exercise A2 - Constructor


        self.toppings = toppings

        self.allowed_sizes = ["Small", "Medium", "Large", "Extra-large"]

        #If the value supplied is invalid, it should be set to a default value of your choosing
        if size not in self.allowed_sizes:
            self.__size = "Medium"
        else: #If the value supplied is valid, it should be stored
            self.__size = size

