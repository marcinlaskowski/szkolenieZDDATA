def funkcja():
    a = 100
    b = 200
    return a, b


if __name__ == "__main__":
    print(funkcja())
    wynik = funkcja()
    print(wynik[0])
    print(wynik[1])

    x, y = funkcja()
    print(x)
    print(y)
