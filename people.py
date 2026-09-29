
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

#ON new worksheet, Exercise B1

class Employee:

    def __init__(self, iid, first_name = "Sam", last_name = "Delaney", _salary = 65000, job_title = "Manager"):

        self.first_name = first_name
        self.last_name = last_name
        self.id = iid
        self._salary = _salary
        self.job_title = job_title

    #q3.
    def get_salary(self):
        return self._salary

    #q4.
    def display(self):
        format = f"Employee[ id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, salary: {self._salary} ]"
        return format

    #q5.
    def calc_net_pay(self):
        #a.
        tax_owed = 0.42 * self._salary
        #b.
        yearly_take_home_pay = self._salary - tax_owed
        #c.
        monthly_take_home_pay = yearly_take_home_pay / 12
        #d.
        return monthly_take_home_pay

    #q6.
    def calc_bonus(self):
        if "manager" in self.job_title.lower():
            bonus = 0.15
        elif "intern" in self.job_title.lower():
            bonus = 0.02
        else:
            bonus = 0.06
        return self._salary * bonus


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
