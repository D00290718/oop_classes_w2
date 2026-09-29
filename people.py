
#29/09/2026 14:00-16:00
#D00290718

#Exercises: Constructors & Encapsulation File .pdf

class Person:

    def __init__(self, first_name, last_name, age, left_handed): #Exercise A1)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.left_handed = left_handed
        print(self.first_name, self.last_name, self.age, self.left_handed)

#Exercise A2)

f_name = input("What is your first name: ")
l_name = input("What is your last name: ")
age = input("What is your age: ")
print("Please choose an option below")
print("1 = Left handed")
print("2 = Right handed")

while True:
    option = int(input("\nEnter a number: "))
    if option == 1:
        left_handed = True
        break
    elif option == 2:
        left_handed = False
        break

obj = Person(f_name, l_name, age, left_handed)
