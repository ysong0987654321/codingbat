def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
    """
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front + front + front

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))
