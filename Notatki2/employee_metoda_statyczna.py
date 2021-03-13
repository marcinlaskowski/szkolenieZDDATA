from datetime import datetime, timedelta


def is_workday(day):
    return day.weekday() not in (5, 6)


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

    # Metoda klasowa
    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)


if __name__ == '__main__':
    date = datetime.today()
    # employee1 = Employee("Jan", "Kowalski", 5000)
    print(Employee.is_workday(date))

    date = date + timedelta(days=4)
    print(date)
    print(date.weekday())
    print(Employee.is_workday(date))
