
#29/09/2026 14:00-16:00
#D00290718

#NEW WORKSHEET - Exercises: Constructors & Encapsulation File PDF

#Exercise B2):

employees = []

for i in range(5):
    print(f"\n\nEmployee {i+1}/5")

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

        employees.append(employee_id)
        #NOT FINISHED, NEED TO GO so will work on this later.