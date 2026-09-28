from people import Person

#28/09/2026 12:00-14:00
#D00290718

#Exercise A2:

obj = Person()

left_handed = obj.left_handed
name = obj.first_name + " " + obj.second_name
if left_handed:
    print(name)
else:
    print(name.upper())

print("\nExercise A3:\n")
#Exercise A3:

p2 = Person()

first_n = input("Hi, what is your First Name: ")
last_n = input(f"{first_n}, What is your Last Name: ")
age = int(input("What age are you: "))
hand = int(input("Please choose:\n1 = Left handed\n2 = Right handed\n-> "))
if hand == 1:
    left_handed = True
elif hand == 2:
    left_handed = False
else:
    left_handed = None
    print("Error. Invalid input, you must select 1 or 2 only")

if left_handed != None:
    p2.first_name = first_n
    p2.second_name = last_n
    p2.age = age
    p2.left_handed = left_handed

    # "  display their name in all caps if they are left-handed, and display it normally otherwise."
    name = p2.first_name + " " + p2.second_name
    if p2.left_handed:
        print(name.upper())
    else:
        print(name)

# "Commit your code after your program is complete."