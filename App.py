from Employee import Employee

# Functions

def create_employee_file(name, role):
    with open(EMPLOYEE_LIST, "a") as af:
            af.write(f"{name}\n")
            with open(f"{name}.txt", "w") as wf:
                wf.write(f"{name}\n{role}\n")


# Reads the name.txt file and creates the employee based on that name, role and shifts
def create_employee(name):
    try:
        with open(f"{name}.txt", "r") as rf:
            employee_name = rf.readline().strip() # Extracting Name
            employee_role = rf.readline().strip() # Extracting Role

            employee = Employee(employee_name, employee_role)

            # Extracting Shifts
            for line in rf: 
                shift = line.strip().split(" ")
                employee.add_shift(shift[0], shift[1], shift[2])
            return employee
    
    except FileNotFoundError:
        print(f"{name}.txt does not exist")
    except Exception as e:
        print(f"An expection as occured {e}")


# Only Managers can call this function
def addingShift():
    employee_name = input("Please tell us the name of the employee: ")
    try:
        with open(f"{employee_name}.txt", "a"):
            day = ""
            while len(day) != 3:
                day = input("Tell us the day (only first 3 letters): ")

    except FileNotFoundError:
        print(f"The employee: {employee_name} does not exists")
    except Exception as e:
        print(f"An error has occured {e}")


def manager_tools(manager):
    while True:
        print("""What would you like to do:
        1. View My Shifts
        2. Add Shifts
        3. Quit
    """)
        choice = input("> ")

        if choice == "1":
            manager.display_shifts()
        elif choice == "2":
            addingShift()
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
        manager_tools(employee)
    elif employee.role == "Associate":
        pass

    

except FileNotFoundError:
    print(f"{EMPLOYEE_LIST} does not exist!")
except Exception as e:
    print(f"An error has occured {e}") 

print("\n#####    Have a Heavenly Day     #####\n")