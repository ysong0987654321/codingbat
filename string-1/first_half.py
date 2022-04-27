def first_half(str):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
    """
    print(str[:len(str)/2])

first_half('WooHoo')
first_half('HelloThere')
first_half('abcdef')