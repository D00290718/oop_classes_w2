from people import Employee

#29/09/2026 14:00-16:00
#D00290718

#NEW WORKSHEET - Exercises: Constructors & Encapsulation File PDF

#Exercise B2):

employees = {}

for i in range(2):
    print(f"\n\nEmployee {i+1}/5")

    #q1 and #q2
    while True:
        employee_id = int(input("Employee ID: "))
        if employee_id in employees:
            print("That ID already exists! Try again...")
        else:
            break

    #q3.
    e_name = input("Employee Full Name: ")
    e_salary = int(input("Employee Salary: "))
    e_job_title = input("Employee Job Title: ")
    e_age = input("Employee Age: ")

    employees[employee_id] = {
        "full_name": e_name,
        "salary": e_salary,
        "job_title": e_job_title,
        "age": e_age
    }

print("\n")
#Once your collection contains 5 Employees, your program should:
#1. Locate the Employee with the lowest net pay and display its details.

lowest_net_pay = 999999
lowest_net_pay_employeeid = 0

for employee_id in employees:
    employee_data = employees[employee_id]
    salary = employee_data["salary"]
    first_name, last_name = employee_data["full_name"].split(" ")
    job_title = employee_data["job_title"]


    obj = Employee(employee_id, first_name, last_name, salary, job_title)
    ans = obj.calc_net_pay()
    if ans < lowest_net_pay:
        lowest_net_pay = ans
        lowest_net_pay_employeeid = employee_id

print("The employee with the lowest net pay:")
print(f"Net Pay: {lowest_net_pay}")
print("- EMPLOYEE DETAILS: ")
_ = employees[lowest_net_pay_employeeid]
for thing in _:
    print(f"{thing}: {_[thing]}")

#2. Locate the Employee with the highest bonus pay and display its details.

print("\n\n")

highest_bonus_pay = 0
highest_bonus_pay_employeeid = 0

for employee_id in employees:
    employee_data = employees[employee_id]
    salary = employee_data["salary"]
    first_name, last_name = employee_data["full_name"].split(" ")
    job_title = employee_data["job_title"]


    obj = Employee(employee_id, first_name, last_name, salary, job_title)
    ans = obj.calc_bonus()
    if ans > highest_bonus_pay:
        highest_bonus_pay = ans
        highest_bonus_pay_employeeid = employee_id

print("The employee with the highest bonus pay:")
print(f"Bonus Pay: {highest_bonus_pay}")
print("- EMPLOYEE DETAILS: ")
_ = employees[highest_bonus_pay_employeeid]
for thing in _:
    print(f"{thing}: {_[thing]}")