# Write a program to calculate the GCD (or HCF) of 2 numbers

def gcd(x, y):
    # assert int(x) == x and int(y) == y, "The numbers must be integers only"
    if not isinstance(x, int):
        return "Must be an integer"
    if not isinstance(y, int):
        return "Must be an integer"

    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1

    
    if y == 0:
        return x
    elif x%y == 0:
        return y
    else:
        return gcd(y, x%y)
    
result = gcd(18,-48.2)
print(result)