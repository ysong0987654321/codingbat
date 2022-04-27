def left2(str):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
    """
    print(str[2:]+str[:2])

left2('Hello')
left2('java')
left2('Hi')