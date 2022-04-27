def without_end(str):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
    """
    print(str[1:-1])

without_end('Hello')
without_end('java')
without_end('coding')