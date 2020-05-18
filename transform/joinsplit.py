# metode join() da split() dari String

# join()
print(', '.join(['Cats', 'Rats', 'Bats']))
print(' '.join(['My', 'name', 'is', 'Jawir']))
print('CUK'.join(['My', 'name', 'is', 'Jawir']))

# split()
print('My name is Jawir'.split())
print('MyCUKnameCUKisCUKJawir'.split('CUK'))
print('My name is Jawir'.split('a'))

# split per line
a = '''Dear Alice,
How are you been? I am fine.
There is container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerly,
Bob
'''

print(a.split('\n'))
