# this is the python file for practice python exercises

# Exercise 1
from unittest import result


name = input('What is your name? ')
age = int(input('How old are you? '))
year = 2014 - age + 100
print(name + ', you will be 100 years old in the year ' + str(year))

# Exercise 2
num = input('Enter a number: ')
mod = num % 2
if mod > 0:
    print('You picked an odd number.')
else:
    print('You picked an even number.')

# Exercise 3
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in lst:
    if i< 5: print(i)

print( [ i for i in lst if i<5 ] )

# Exercise 4
__author__ = 'jeffreyhunt'

num = int(input('Please choose a number: '))

listRange = list(range(1,num+1))
divisorList = []
for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

# Exercise 6:
word=input('Please enter a word')
word=str(word)
result=word[::-1]
print(result)
if word == result:
    print('This word is a palindrome')
else:
    print('This word is not a palindrome')

# Exercise 7
b = [element for element in i if element % 2 == 0]

# Exercise 8: difficult one
import sys

user1 = input('What\'s your name?')
user2 = input('And your name?')
user1_answer = input('%s, do yo want to choose rock, paper or scissors?' % user1)
user2_answer = input('%s, do you want to choose rock, paper or scissors?' % user2)

def compare(u1, u2):
    if u1 == u2:
        return('It\'s a tie!')
    elif u1 == 'rock':
        if u2 == 'scissors':
            return('Rock wins!')
        else:
            return('Paper wins!')
    elif u1 == 'scissors':
        if u2 == 'paper':
            return('Scissors win!')
        else:
            return('Rock wins!')
    elif u1 == 'paper':
        if u2 == 'rock':
            return('Paper wins!')
        else:
            return('Scissors win!')
    else:
        return('Invalid input! You have not entered rock, paper or scissors, try again.')

print(compare(user1_answer, user2_answer))

# Exercise 9:
import random

rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != 'exit':
    guess = input('Enter a guess between 1 to 9')

    if guess == 'exit':
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print('Too low')
    elif guess > rd:
        print('Too high')
    else:
        print('Right!')
        print('You took only', c, 'tries!')
input()

# Exercise 10:
import random
 
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in a if i in b]