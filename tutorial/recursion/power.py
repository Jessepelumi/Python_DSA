def power(base, exp):
    if not isinstance(base, int):
        return "The base must be an integer"
    elif not isinstance(exp, int):
        return "The exponent must be an integer"
    elif exp == 0:
        return 1
    else:
        return base * power(base, exp-1)
    
result = power(2, 3)
print(result)