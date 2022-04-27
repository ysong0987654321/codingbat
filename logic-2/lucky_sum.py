def lucky_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
    """
    sum = 0
    list = [a, b, c, 13]
    for n in list[:list.index(13)]:
        sum += n
    return sum

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))