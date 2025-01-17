import database as db
from datetime import datetime

# Only Managers can hire employee for simplicity I am starting with my myself as Manager i.e there is already 1 employee in the database


# Functions


# This function returns a string of the format (YYYY-MM-DD). It will keep asking until the format is correct
def get_shift_time():
    while True:
        try:
            user_input = input("Please enter the time in the format (YYYY-MM-DD HH:MM): ")
            shift_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
            return shift_time
        except ValueError:
            print("Incorrect format. Please use the format (YYYY-MM-DD HH:MM)")
        

def manager_tools(manager_name):
    while True:
        userChoice = input("""\nWhat would you like to do
            1. View my shifts
            2. View other employee shifts
            3. Add Shift
            4. Remove Shift
            5. Quit
\n> """)
        print()
        if userChoice == "1":
            db.show_shifts(manager_name)
        elif userChoice == "2":
            db.show_all()
            employee_name = input("Whose shift would you like to see (name): ")
            print()
            db.show_shifts(employee_name)
        elif userChoice == "3":
            employee_name = input("Enter the employee's name you want to add shift for: ")
            print("Please enter the start time")
            start_time = get_shift_time()
            print("Please enter the end time")
            end_time = get_shift_time()

            db.add_shift(employee_name, start_time, end_time)

        elif userChoice == "4":
            employee_name = input("Enter the employee's name you want to remove shift for: ")
            db.show_shifts(employee_name)
            shift_id = input("Please enter the Shift ID for the shift you want to remove: ")
            db.remove_shift(employee_name, shift_id)
            db.show_shifts(employee_name)
       
        elif userChoice == "5":
            break
        else:
            print("Incorrect Input\n")


def associate_tools(name):
    while True:
        userChoice = input("""\nWhat would you like to do
            1. View my shifts
            2. Quit
\n> """)
        print()
        if userChoice == "1":
            db.show_shifts(name)
        elif userChoice == "2":
            break
        else:
            print("Incorrect Input")


# Main Program

print("#####    WELCOME TO THE SHIFT APP    #####")
name = input("Please tell us your name: ")

if db.find_employee_id(name):
    print(f"Welcome back {name}")
else:
    exit()


employee_role = db.find_employee_role(name)

if employee_role:
    if employee_role == "Manager":
        manager_tools(name)
    else:
        associate_tools(name)

else:
    print(f"Employee ({name}) not found")