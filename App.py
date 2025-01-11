import database as db

# Only Managers can hire employee for simplicity I am starting with my myself as Manager i.e there is already 1 employee in the database

print("#####    WELCOME TO THE SHIFT APP    #####")
name = input("Please tell us your name: ")

if db.find_employee_id(name):
    print(f"Welcome back {name}")
else:
    exit()


