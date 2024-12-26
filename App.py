from Employee import Employee


print("#####    WELCOME TO SHIFT APP    #####")
name = input("Please enter your name: ")

def check_role():
    while True:
        role = input("Please tell us your role: ")
        if role == "Manager" or role == "Associate":
            return role

if name not in Employee.employees:
    print("It looks like you are new here!")
    Employee(name, check_role()) # adds the new Employee object
else:
    pass


