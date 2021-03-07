if __name__ == "__main__":

    number = 0
    while number <= 10:
        print(number)
        number += 1

        if number == 5:
            break

    number = 0
    while number <= 10:
        number += 1

        if number % 2 == 0:
            continue

        print(number)
