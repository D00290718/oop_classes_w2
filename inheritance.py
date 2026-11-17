#Exercises: Inheritance FilePDF 
from datetime import date , datetime
from types import NotImplementedType
class Animal:
    # __init__() - this should require the weight and date of birth but leave the name as an optional parameter
    def __init__(self, dob, weight, name="Sam"):
        self.name = name
        dob = dob.replace("-", "")
        self.dob = dob
        self.weight = weight
        self.dob_obj = datetime.strptime(self.dob, "%d%m%Y").date()

    # calculates the age of the animal based on subtracting its date of birth from the current date  when the program is run.
    def calc_age(self):
        birthDate = self.dob_obj
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age

    # This should display the data of the animal in a well-formatted manner.
    def display(self):
        msg = f"Name: {self.name}\nDOB: {self.dob}\nWeight: {self.weight}"
        return msg

    def __str__(self) -> str:
        return f"{self.name} is {self.calc_age()} years old and weighs {self.weight}kg."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{{name={self.name}, weight:{self.weight}, dob={self.dob}"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Animal):
            return NotImplemented

        if self.dob != other.dob:
            return False

        if self.weight != other.weight:
            return False

        if self.name.lower() != other.name.lower():
            return False

        return True

class Dog(Animal):
    def __init__(self, dob, weight, breed, name="Sam", personality="Happy"):
        dob = dob.replace("-", "")
        super().__init__(dob, weight, name)
        self.breed = breed
        self.personality = personality

    def display(self):
        msg = f"Name: {self.name}\nDOB: {self.dob}\nWeight: {self.weight}\nBreed: {self.breed}\nPersonality: {self.personality}"
        return msg


class Person:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    # calculates the age of the person based on subtracting the date of birth from the current date

    def calc_age(self):
        birthDate = self.dob
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        return age



#o#bj = Animal("08042002", "67kg", "Sam")
#obj.display()
#p#rint(obj.calc_age())

#print("abc")

#obj2 = Dog("08042002", "67kg", name="Sam", breed="retriever")
#obj2.display()