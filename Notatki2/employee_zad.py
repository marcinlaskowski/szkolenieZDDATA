"""
Dodać nowy parametr/własciwosc - numer telefon
Metoda get_contact(), ktora wypisze imie nazwisko i telefon
"""


class Employee:
    raise_amount = 1.04  # zmienna klasowa

    def __init__(self, first, last, pay, phone):
        self.first = first
        self.last = last  # zmienne obiektowe
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        self.phone = phone

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def get_contact(self):
        return f'{self.fullname()} - {self.phone}'


if __name__ == '__main__':
    employee1 = Employee("Jan", "Kowalski", 5000, "333322334")
    print(employee1.get_contact())
