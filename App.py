import database as db

# Only Managers can hire employee for simplicity I am starting with my myself as Manager i.e there is already 1 employee in the database


# Functions


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
            pass
        elif userChoice == "4":
            pass
        elif userChoice == "5":
            break
        else:
            print("Incorrect Input\n")


def associate_tools(name):
    while True:
        userChoice = input("""What would you like to do
            1. View my shifts
            2. Quit
""")

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