from Employee import Employee

# Functions

def create_employee_file(name, role):
    with open(EMPLOYEE_LIST, "a") as af:
            af.write(f"{name}\n")
            with open(f"{name}.txt", "w") as wf:
                wf.write(f"{name}\n{role}\n")


def create_employee(name):
    try:
        with open(f"{name}.txt", "r") as rf:
            employee_name = rf.readline().strip()
            employee_role = rf.readline().strip()

            employee = Employee(employee_name, employee_role)
            return employee
    
    except FileNotFoundError:
        print(f"{name}.txt does not exist")
    except Exception as e:
        print(f"An expection as occured {e}")
    
def manager_tools():
    while True:
        print("""What would you like to do:
        1. View My Shifts
        2. Add Shifts
        3. Quit
    """)
        choice = input("> ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Enter correct input!")

# Main program

print("\n#####    WELCOME TO SHIFT APP    #####\n")
name = input("Please enter your name: ")
EMPLOYEE_LIST = "Employee.txt"

try:
    with open(EMPLOYEE_LIST, "r") as f:
        employees = set(line.strip() for line in f)
    
    if name in employees:
        print(f"Welcome back {name}")
    else:
        print(f"You are new here {name}")
        role = input("What is your role dear? ")
        create_employee_file(name, role)
        

    employee = create_employee(name)
    if employee.role == "Manager":
        manager_tools()

    

except FileNotFoundError:
    print(f"{EMPLOYEE_LIST} does not exist!")
except Exception as e:
    print(f"An error has occured {e}") 

print("\n#####    Have a Heavenly Day     #####\n")