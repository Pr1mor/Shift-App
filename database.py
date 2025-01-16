import sqlite3
from datetime import datetime, timedelta

def create_database():

    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS employees (

                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                employee_role TEXT NOT NULL
)""")

    c.execute("""CREATE TABLE IF NOT EXISTS shifts (
              
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER NOT NULL,
                start_shift TEXT NOT NULL,
                end_shift TEXT NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
)""")

    conn.commit()
    conn.close()


# For simplicity do not add multiple employee with the same name
def add_employee(name, role):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("INSERT INTO employees (employee_name, employee_role) VALUES (?, ?)", (name, role,))

    conn.commit()
    conn.close()

# Make sure shifts are valid i.e start time < end time day is the same and shifts dont overlap
def add_shift(name, start, end):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    id = find_employee_id(name)

    if id:
        isValid = check_shifts(id, start, end)
        if isValid:

            start_time = start.strftime("%Y-%m-%d %H:%M")
            end_time = end.strftime("%Y-%m-%d %H:%M")
            c.execute("INSERT INTO shifts (employee_id, start_shift, end_shift) VALUES (?,?,?)", (id, start_time,end_time))
            print("Shift added successfully")
    else:
        print(f"Employee ({name}) not found")

    conn.commit()
    conn.close()


# checks if the 2 shifts are valid or not i.e (same day, start < end and no overlapping of shifts)
def check_shifts(id, start, end):

    if start.date() != end.date():
        print("Error: Both the start and end timings should be on the same day")
        return False
    
    elif start >= end:
        print("Error: Start time should be earlier than end time")
        return False

    else:
        # check for overlaping of shifts
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()

        c.execute("SELECT start_shift, end_shift FROM shifts WHERE (employee_id) = (?)", (id,))
        shifts = c.fetchall()
        start_time = start.strftime("%Y-%m-%d %H:%M")
        end_time = end.strftime("%Y-%m-%d %H:%M")
        
        for existing_start, existing_end in shifts:
            if start_time < existing_end and end_time > existing_start:
                print("Error: The new shift overlaps with the existing one")
                return False

        conn.commit()
        conn.close()

    return True

def show_all():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("SELECT * FROM employees")

    employees = c.fetchall()
    print("ID\tName\t\tRole")
    for employee in employees:
        print(f"{employee[0]}\t{employee[1]}\t\t{employee[2]}")

    conn.commit()
    conn.close()



def show_shifts(name):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    id = find_employee_id(name)

    if id:
        c.execute("SELECT start_shift, end_shift FROM shifts WHERE (employee_id) = (?) ORDER BY start_shift", (id,))

        shifts = c.fetchall()

        print(f"Showing shifts for Employee {id} ({name})")
        print("Date\t\tStart\t\tEnd")
        for shift in shifts:
            format_shift(shift)

    else:
        print(f"Employee ({name}) not found")

    conn.commit()
    conn.close()


def format_shift(shift_tuple):

    start_time = datetime.strptime(shift_tuple[0], "%Y-%m-%d %H:%M") # 2025-01-01 08:00
    end_time = datetime.strptime(shift_tuple[1], "%Y-%m-%d %H:%M")   # 2025-01-01 15:00

    date = start_time.strftime("%Y-%m-%d") # 2025-01-01
    start_time = start_time.strftime("%H:%M") # 08:00
    end_time = end_time.strftime("%H:%M")   # 15:00

    print(f"{date}\t{start_time}\t\t{end_time}")


def find_employee_id(name):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("SELECT id FROM employees WHERE (employee_name) = (?)", (name,))
    id = c.fetchone()

    conn.commit()
    conn.close()

    if id:
        return id[0]
    else:
        return None
    

def find_employee_role(name):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("SELECT employee_role FROM employees WHERE (employee_name) = (?)", (name,))
    role = c.fetchone()

    conn.commit()
    conn.close()

    if role:
        return role[0]
    else:
        return None
    

def delete_all():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("DROP TABLE employees")
    c.execute("DROP TABLE shifts")

    conn.commit()
    conn.close()


def help():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("DELETE FROM shifts WHERE id = 4")

    conn.commit()
    conn.close()