from employee import Employee


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if not employees:
            self.employees = set()
        else:
            self.employees = employees

    # Nowe metody
    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.fullname())
            # print(employee) # moze byc tak jesli jest nadpisana metoda __str__
