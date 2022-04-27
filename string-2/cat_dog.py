def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return str.count("cat") == str.count("dog")

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))