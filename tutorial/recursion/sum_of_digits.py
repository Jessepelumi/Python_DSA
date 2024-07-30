# Write a program to sum up the digits in a number
# Example: 1234 -> 10

def sumOfDigits(n):
    if not isinstance(n, int):
        return "Must be an integer"
    elif n < 10:
        return n
    else:
        return (n%10) + sumOfDigits(n//10)
    
result = sumOfDigits(1234)
print(result)