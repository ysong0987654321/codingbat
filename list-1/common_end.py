def common_end(a, b):
    """ 
    Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
    """
    print(a[0] == b[0] or a[-1] == b[-1])

common_end([1, 2, 3], [7, 3])
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])