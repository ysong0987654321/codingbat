def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
    """
    print(a[1:]+b[1:])

non_start('Hello', 'There')
non_start('java', 'code')
non_start('shotl', 'java')