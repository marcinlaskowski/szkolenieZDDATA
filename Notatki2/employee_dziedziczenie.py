class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Nadpisuja odwołanie sie w print obiektu
    def __str__(self):
        # return f'{self.first} {self.last}'
        return self.fullname()


class Developer(Employee):
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language

    # Nadpisanie, override
    def fullname(self):
        return f'{self.last} - {self.programming_language}'

    # Użycie metody rodzica
    # def fullname(self):
    #     return f'{super().fullname()} - {self.programming_language}'


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


if __name__ == "__main__":
    employee = Employee("Jan", "A", 4000)
    print(employee)

    # print(type(employee))
    developer = Developer("Adam", "B", 5000, "Python")
    print(developer)
    # print(developer.pay)
    # print(developer.programming_language)
    # print(type(developer))

    print("------------")
    # print(employee.fullname())
    # print(developer.fullname())

    kowalski = Manager("Artur", "Kowalski", 6000)
    print("Przed")
    kowalski.print_employees()
    kowalski.add_employee(developer)
    print("Po dodaniu")

    kowalski.print_employees()

    print(kowalski.fullname())
