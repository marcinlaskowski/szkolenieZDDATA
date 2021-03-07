
def my_max(sentence):
    largest = 0
    for number in sentence:
        if number > largest:
            largest = number

    return largest

if __name__ == "__main__":
    # range 0,1,2,3
    # for liczba in range(100):
    #     print(liczba)
    #
    # for i in [0,1,2]:
    #     name = input("Jak masz na imię?")
    #     print(f"Hej {name}")

    # Zakladamy dodatnie liczby
    numbers = [2, 3, 45, 12, 34]
    print("Largest: ", my_max(numbers))
