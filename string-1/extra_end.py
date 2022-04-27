def extra_end(str):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
    """
    print(str[-2:]*3)

extra_end('Hello')
extra_end('ab')
extra_end('Hi')