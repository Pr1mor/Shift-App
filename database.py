import sqlite3

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


def add_shift(name, start, end):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    id = find_employee_id(name)

    if id:
        c.execute("INSERT INTO shifts (employee_id, start_shift, end_shift) VALUES (?,?,?)", (id, start, end))
    else:
        print(f"Employee ({name}) not found")

    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("SELECT * FROM employees")

    employees = c.fetchall()
    for employee in employees:
        print(employee)

    conn.commit()
    conn.close()



def show_shifts(name):
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    id = find_employee_id(name)

    if id:
        c.execute("SELECT * FROM shifts WHERE (employee_id) = (?)", (id,))

        shifts = c.fetchall()
        for shift in shifts:
            print(shift)

    else:
        print(f"Employee ({name}) not found")

    conn.commit()
    conn.close()


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
    

def delete_all():
    conn = sqlite3.connect("employee.db")
    c = conn.cursor()

    c.execute("DROP TABLE employees")
    c.execute("DROP TABLE shifts")

    conn.commit()
    conn.close()