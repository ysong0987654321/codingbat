def sum67(nums):
    """
    Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    count = 0
    blocked = False
  
    for n in nums:
        if n == 6:
            blocked = True
            continue
        if n == 7 and blocked:
            blocked = False
            continue
        if not blocked:  
            count += n
  
    return count

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))

# difficult to do, took a few tries but similar to class quiz