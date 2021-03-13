class Employee:
    raise_amount = 1.04  # zmienna klasowa

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last  # zmienne obiektowe
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


if __name__ == '__main__':
    employee1 = Employee("Jan", "Kowalski", 5000)
    print("Jan", employee1.raise_amount)
    employee2 = Employee("Agnieszka", "Kowalska", 4000)
    print("Agnieszka", employee2.raise_amount)

    print("Employee", Employee.raise_amount)

    Employee.raise_amount = 1.1
    print("Zmiana Employee.raise_amount = 1.1")

    print("Employee", Employee.raise_amount)
    print("Jan", employee1.raise_amount)
    print("Agnieszka", employee2.raise_amount)

    employee1.raise_amount = 3.0
    print("Zmiana employee1.raise_amount = 3.0")

    print("Employee", Employee.raise_amount)
    print("Jan", employee1.raise_amount)
    print("Agnieszka", employee2.raise_amount)

    Employee.raise_amount = 1.2
    print("Zmiana Employee.raise_amount = 1.2")

    print("Employee", Employee.raise_amount)
    print("Jan", employee1.raise_amount)
    print("Agnieszka", employee2.raise_amount)