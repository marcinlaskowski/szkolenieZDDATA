from Zadania3.funkcje_zad1 import add
from random import randint
import datetime
import math

from Notatki3.employees import employee, developer

if __name__ == '__main__':
    print(add(1, 2))
    print(randint(1, 4))
    print(datetime.datetime.today())
    print(math.pow(3, 3))
    print(math.floor(10.6))
    print(math.ceil(11.9))

    employee = employee.Employee("Jan", "Kowalski", 1000)
    print(employee)
    dev = developer.Developer("Jan", "Kowalski", 1000, "Python")
    print(dev)
