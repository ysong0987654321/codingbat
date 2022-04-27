def sum_double(a, b):
    """
    Given two int values, return their sum. Unless the two values are the same, then return double their sum.
    """
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))