def decimalToBinary(num):
    if not isinstance(num, int):
        return "Must be an integer"

    if num == 0:
        return 0
    else:
        return num%2 + 10 * decimalToBinary(int(num/2))


result = decimalToBinary(-13)
print(result)