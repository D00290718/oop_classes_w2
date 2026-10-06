
#Exercises: Using Classes and Working With Encapsulation File PDF
#06/10/26 14:00-16:00

#Exercise B1 Initial program

from datetime import datetime

#1.
from orders import Pizza

#2.
orders = {}

#3.
username = input("What is your Username: ")

#4.
while True: #Repeatedly asks the user if they want to order a pizza.
    option = input("\nDo you want to order a pizza? (y/n): ")
    if option.lower() == "n":
        break
    else:

        #a.
        while True:
            pizza_nickname = input("Pizza Nickname: ")
            if pizza_nickname in orders:
                print("- ERROR - That nickname is taken. Choose another.")
            else:
                break

        #b.
        print("Please choose one of the following sizes: Small, Medium, Large, Extra-large")
        pizza_size = input("What is your pizza size: ")

        #c.

        option2 = input("Do you want toppings? (y/n): ")
        option2 = option2.lower()

        if option2 == "y":
            print("Please enter a topping. Send 'stop' when you are done with toppings.")
            toppings = []
            while True:
                _ = input(f"Topping {len(toppings)+1}: ")
                if _.lower() == "stop":
                    break
                toppings.append(_)

        else: #c. (i)
            toppings = ["tomato sauce", "cheese"]

        #d.

        obj = Pizza(toppings, pizza_size)

        obj.display()

        orders[pizza_nickname] = [pizza_size, toppings]

print()
#When the user is finished adding pizzas to their order:

#This is just for testing so i don't need fill it out all the time
#orders = {'1': ['Large', ['pepperoni', 'cheese', 'mushrooms', 'chicken']], '2': ['Extra-large', ['tomato sauce', 'cheese']], '3': ['Small', ['chicken', 'bacon', 'pepperoni']]}

#calculate the cost of each pizza in the user’s order dictionary
#q1.
for order_id in orders:

    pizza_info = orders[order_id]
    pizza_size = pizza_info[0]
    pizza_toppings = pizza_info[1]

    obj = Pizza(pizza_toppings, pizza_size)
    cost_of_pizza = obj.calc_price()
    #print(pizza_size, pizza_toppings)
    orders[order_id].append(cost_of_pizza)
    #print(f"Cost of Pizza: {cost_of_pizza}")

#q2. (a)

def most_expensive_pizza(): #. Consider writing a function to identify the most expensive pizza

    amount = 0
    most_expensive_id = -1

    for order_id in orders:
        pizza_info = orders[order_id]
        pizza_cost = pizza_info[2]
        if amount < pizza_cost:
            amount = pizza_cost
            most_expensive_id = order_id
    return most_expensive_id

most_expensive_order_id = most_expensive_pizza()

#q2.
print("-- MOST EXPENSIVE PIZZA : ")
pizza_info = orders[str(most_expensive_order_id)]
pizza_size = pizza_info[0]
pizza_toppings = pizza_info[1]
pizza_cost = pizza_info[2]
print(f"Pizza Cost: €{pizza_cost}")
print(f"Pizza Size: {pizza_size}")
print(f"Pizza Toppings: {pizza_toppings}")


#Q3.
print()
total_bill = 0
for order_id in orders:
    pizza_info = orders[order_id]
    pizza_cost = pizza_info[2]
    total_bill += pizza_cost

print(f"-- TOTAL BILL FOR ALL {len(orders)} PIZZAS: €{round(total_bill)}")

print(datetime.now())


#Stretch exercise:

#1.

print(orders)

text = f""
for order_id in orders:
    pizza_info = orders[str(order_id)]
    pizza_size = pizza_info[0]
    pizza_toppings = pizza_info[1]
    pizza_cost = pizza_info[2]
    text += f"Pizza Nickname: {order_id}\n"
    text += f"    - Size: {pizza_size}\n"
    text += f"    - Toppings: {pizza_toppings}\n"
    text += f"    - Cost: €{pizza_cost}\n"

text += f"TOTAL COST - €{total_bill}"
timestamp = str(datetime.now())
#Need to fix timestamp as some letters cant be saved as file
timestamp = timestamp.replace(":", "")
timestamp = timestamp.split(".")[0]
filename = f"{username}_{timestamp}.txt"

with open(filename, "w") as f:
        f.write(text + "\n")

#need to fix a bug - when a user enters lowercase pizza as example, pizza shop doesnt understand
# orders.py is perfect