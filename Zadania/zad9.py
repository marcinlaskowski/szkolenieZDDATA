"""
9. Pętle.Wygeneruj ciąg liczb od 0 do 10 pętlą while,
następnie próbuj wygenerować od 10 do 0 również pętlą while.
"""

if __name__ == "__main__":

    number = 0
    while number <= 10:
        print(number)
        number += 1

    number = 10
    while number >= 0:
        print(number)
        number -= 1
