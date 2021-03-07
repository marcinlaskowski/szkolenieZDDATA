def my_sum(sentence):
    result = 0
    for number in sentence:
        result = result + number
        # 2 opcja
        # result += number
        print(number)
        print("result", result)

    return result


if __name__ == "__main__":
    numbers = [2, 3, 45, 12, 34]
    print("Result: ", my_sum(numbers))
