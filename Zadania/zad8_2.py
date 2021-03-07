"""
8. Pętle. Napisz program, który dla 10 kolejnych liczb
naturalnych wyświetli
ich ich wartość do sześcianu. Spróbuj zrobić to pętla for,
 następnie pętla while.
"""

if __name__ == "__main__":

    for number in range(1, 11):
        print(number ** 3)

    number = 1
    while number <= 10:
        print(number ** 3)
        number += 1
