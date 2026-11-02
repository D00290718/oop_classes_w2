
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


class Users:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db_filename = "users_db.txt"
        self.users_db = {}
        with open(self.db_filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                username, password = line.split(",")
                self.users_db[username] = password

    def check_password(self):
        try:
            if self.users_db[self.username] == self.password:
                return True
            return False
        except:
            return None

    def update_password(self, new_password):
        try:
            self.users_db[self.username] = new_password
            text = ""
            for username in self.users_db:
                password = self.users_db[username]
                print(username,password)
                text += f"{username},{password}\n"
            with open(self.db_filename, "w") as f:
                f.write(text)
            return True
        except:
            return False

    @staticmethod
    def validate_password(password):
        valid_pw = True

        if len(password) < 8:
            valid_pw = False

        has_upper = False
        has_lower = False
        has_digit = False

        for letter in password:
            if letter.isupper():
                has_upper = True
            elif letter.islower():
                has_lower = True
            elif letter.isdigit(): 
                has_digit = True

        if not has_upper or not has_lower or not has_digit:
            valid_pw = False

        return valid_pw

"""
Create a class User that contains:

username
password
You should encapsulate this information appropriately.

Write a method check_password() that takes in a password and checks if it matches the value stored within this user. It should return True if the password matches and False otherwise.

Write a method validate_password() that takes in a piece of text and checks if it is upholds your system's password rule. The method should be a static method (i.e. should use @staticmethod) and you should include appropriate password rule logic here.

Write a method update_password() that takes in two pieces of text: the original password and the new password. If the original password matches the password currently stored, set the stored password to the new password and return True. Otherwise, return False.

Update your pizza_shop.py to:

Create a user object with hard-coded data and store it.
Repeatedly do the following until the user chooses to terminate the program:
Require that a user logs in before they can order anything.
Provide an option to log out. When they log out, the pizzas in their order are written to a receipt file with their username and the current timestamp, and the order dictionary is wiped.
"""