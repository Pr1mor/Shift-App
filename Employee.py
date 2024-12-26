class Employee:

    employees = []

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.employees.append(self)

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}"
