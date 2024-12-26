from Employee import Employee

# Functions

def check_role():
    while True:
        role = input("Please tell us your role: ")
        if role == "Manager" or role == "Associate":
            return role
        
def getEmployee(name): 
    for em in Employee.employees:
        if em.name == name:
            return em 


# Main program

print("#####    WELCOME TO SHIFT APP    #####")
name = input("Please enter your name: ")

if name not in Employee.employees:
    print("It looks like you are new here!")
    Employee(name, check_role()) # adds the new Employee object
else:
    print(f"Welcome Back {name}")

employee = getEmployee(name)

while True: 
    print("""What would you like to do:
        1. View my Shifts
        2. Quit
    """)
    choice = int(input("> "))
    if choice == 1:
        employee.add_shift("Monday", "9:00", "12:00")
        employee.add_shift("Thursday", "17:00", "21:00")
        employee.add_shift("Saturday", "12:00", "18:00")
        employee.display_shifts()
    elif choice == 2:
        break



print("#####    Have a Heavenly Day     #####")