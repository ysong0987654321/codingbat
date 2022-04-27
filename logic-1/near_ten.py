def near_ten(num):
    """
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
    """
    within = num%((num/10)*10) if num >= 10 else num
    return within in [8,9,0,1,2]

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))

# difficult one, referenced answer key in codingbat