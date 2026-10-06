
#Exercises: Using Classes and Working With Encapsulation File PDF
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

        #For
        self.pizza_prices = {
            "Small": 10,
            "Medium": 12,
            "Large": 15,
            "Extra-large": 18,
            "per_topping_charge": 0.85
        }

    #Exercise A3

    #Ex. A3 - Q1
    def display(self):
        a = ""
        counter = 1
        print(self.toppings)
        for topping in self.toppings:
            if counter == len(self.toppings):
                a += topping
            else:
                a += f"{topping},"
            counter += 1
        print(f"{self.__size} pizza with {a} toppings")

    #Ex. A3 - Q2
    def get_size(self):
        return self.__size

    # Ex. A3 - Q3
    def set_size(self, new_size):
        #If an inappropriate value is provided, the size should not be changed, and the method should return False
        if new_size not in self.allowed_sizes:
            return False
        self.__size = new_size
        return True

    # Ex. A3 - Q4
    def get_num_toppings(self):
        return len(self.toppings)


    # Ex. A3 - Q5
    def add_topping(self, new_topping):
        #a.
        self.toppings.append(new_topping)
        #b.
        return True

    # Ex. A3 - Q6

    def remove_topping(self, topping_to_remove):
        #a.
        try:
            self.toppings.remove(topping_to_remove)
            return True
        except ValueError:
            return False


    #Ex. B2

    def calc_price(self):
        pizza_cost = self.pizza_prices[self.__size] #This is without toppings
        amount_of_toppings = len(self.toppings)
        cost_per_topping = self.pizza_prices["per_topping_charge"]
        toppings_total_cost = amount_of_toppings * cost_per_topping
        final_pizza_cost = pizza_cost + toppings_total_cost
        return final_pizza_cost
