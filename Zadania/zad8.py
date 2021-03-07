"""
Słowniki. Mając dane dotyczące osób (imię, nazwisko, ulubiony sport, płeć, wiek) wykonaj poniższe podpunkty.
Adam, Nowak, siatkówka, mężczyzna, 25
Agata, Kowalska, pływanie, kobieta, 42
Mateusz, Markowski, koszykówka, mężczyzna, 29
Magda, Popławska, siatkówka, kobieta, 32

Stwórz zmienne typu słownik opisujące każdą osobę.
Pamiętaj, aby zachować takie same nazwy kluczy.
Zmień wiek dla pierwszej osoby na 32
Stwórz listę wszystkich osób.
Usuń z listy ostatni element

"""

# Stwórz zmienne typu słownik opisujące każdą osobę.

person1 = {
    "name": "Adam",
    "surname": "Nowak",
    "sport": "siatkówka",
    "gender": "mężczyzna",
    "age": 25
}

person2 = {
    "name": "Agata",
    "surname": "Kowalska",
    "sport": "pływanie",
    "gender": "kobieta",
    "age": 42
}

# TODO person2, person2, person 4

print(person1["name"])
# Zmien wiek
person1['age'] = 60
print(person1['age'])

# Stwórz listę wszystkich osób.
people = [person1, person2]
print(people)

# Usuń z listy ostatni element
del people[-1]

# lub people.pop(-1)