# Exercise 22
with open('data/stopwords.txt') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

# Exercise 24:
a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))