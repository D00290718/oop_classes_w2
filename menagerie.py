from inheritance import Animal, Dog
import random as rand #q5.


#1) Create a list called animals
animals_objs = []

#2) Create 3 hard-coded Animal objects and add them to your lists

obj1 = Animal(dob="01-10-2025", weight="10", name="Cathal")
obj2 = Animal(dob="05-07-2026", weight="7", name="David")
obj3 = Animal(dob="22-01-2024", weight="4", name="Peter")

animals_objs.append(obj1)
animals_objs.append(obj2)
animals_objs.append(obj3)

#3) Create 2 user-defined Animal objects and add them to your list

if 1== 2:
    for i in range(2):
        print()
        print(f"Dog {i+1}/2")
        dob = input("Enter a DOB in format (dd-mm-yyyy): ")
        weight = input("enter weight in KG: ")
        weight = weight.lower().replace("kg", "")
        name = input("Enter a name (optional): ")
        u_obj = Animal(dob=dob, weight=weight, name=name)
        animals_objs.append(u_obj)

#4) Create 4 hard-coded Dog objects and add them to your list

dog_obj1 = Dog(dob="05-12-2023", weight="6", breed="bulldog", name="Andrew", personality="Angry")
dog_obj2 = Dog(dob="21-03-2022", weight="12", breed="german_shepherd", name="Dara", personality="Angry")
dog_obj3 = Dog(dob="12-01-2019", weight="25", breed="shih_tzu", name="John", personality="Chill")
dog_obj4 = Dog(dob="06-03-2026", weight="5", breed="golden_retriever", name="craig", personality="happy")


animals_objs.append(dog_obj1)
animals_objs.append(dog_obj2)
animals_objs.append(dog_obj3)
animals_objs.append(dog_obj4)

#5) Shuffle the contents of the list

rand.shuffle(animals_objs)

#6) Display the contents of the list

print(f"\n--- 6) Display the contents of the list")

for thing in animals_objs:
    print(thing)

#7) Print the names of only the animals (dogs OR Animals) aged 2 or under


print(f"\n--- 6) Print the names of only the animals (dogs OR Animals) aged 2 or under")

for thing in animals_objs:
    age = thing.calc_age()
    if age <= 2:
        print(f"Age {age} | Name: {thing.name}")