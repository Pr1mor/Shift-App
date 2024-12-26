class Shift: 
    def __init__(self, day,start_time, end_time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time


    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"


class Employee:

    employees = []

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.employees.append(self)
        self.shifts = []


    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}"
    
    def add_shift(self, day, start_time, end_time):
        self.shifts.append(Shift(day, start_time, end_time))
    
    def display_shifts(self):
        print(f"Shifts for {self.name}")
        for shift in self.shifts:
            print(shift)
    

