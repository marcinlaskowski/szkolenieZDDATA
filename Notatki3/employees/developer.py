# from employees.employee import Employee
# # from employee import Employee
from Notatki3.employees.employee import Employee


class Developer(Employee):
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language

    # Nadpisanie, override
    def fullname(self):
        return f'{self.last} - {self.programming_language}'
