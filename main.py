first_name = input("Enter First Name : ")
last_name = input("Enter Last Name :")
Address = input("Enter address : ")
apartment = input("Enter apratment number : ")
age = int(input("Enter Age : "))
experience = int(input("Enter Experience : "))
position = input("Enter The Position : ")
salary = input("Enter The Salary : ")

print("=========================================")
Employee = last_name + " " + last_name
print("Employee : ", Employee)
Employee_age = f"{age}"
print("Age : ", Employee_age)
Employee_position = position.title()
print("Position : ",Employee_position)
Employee_salary = f"${salary}"
print("Salary : ", Employee_salary)
Employee_experience = f"{experience} Years "
print("Experience : ", Employee_experience)
Employee_address = Address + apartment
print("Address : ", Employee_address)
Employee_code = 'DEV-2025-JD-001'

print("=========================================")
print("Code Breakdown")
Employee_department = Employee_code[0:3]
print("Department : ", Employee_department)
Employee_year = Employee_code[4:8]
print("Year : ",Employee_year)
Employee_initials = Employee_code[9:11]
print("Initials : ", Employee_initials)
Employee_number = Employee_code[-3:]
print("Employee Number : ", Employee_number)
