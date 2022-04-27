# this is the python file for practice python exercises

# Exercise 11:
num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print('prime')
		else:
			print('NOT prime')
	else:
		print('NOT prime')
	
is_prime(num)

# Exercise 12:
def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

list_ends([5, 10, 15, 20, 25])

# Exercise 13:
def fibonacci():
    num = int(input('How many numbers that generates?:'))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()

# did this for one of the exercises in class

# Exercise 14:

# Exercise 15:
def reverseWord(w):
    return ' '.join(w.split()[::-1])

reverseWord('Marshall')

# Exercise 16:
import random

s = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
passlen = 8
p =  ''.join(random.sample(s,passlen ))
print(p)

# Exercise 20:
def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False
  
if __name__=='__main__':
  lst = [2, 4, 6, 8, 10]
  print(find(lst, 5)) # prints False
  print(find(lst, 10)) # prints True
  print(find(lst, -1)) # prints False
  print(find(lst, 2)) # prints True
