'''
feeling =  input('How are you?')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
'''

# metode isX dari string untuk pengecekan
'''
print('hello'.isalpha()) # mengembalikan nilai true apabila string berisi hanya huruf dan tidak kosong
print('hello123'.isalnum()) # true apabila string berisikan huruf atau angka dan tidak kosong
print('123'.isdecimal()) # true apabila string berisikan hanya angka/numerik dan tidak kosong
print(' '.isspace()) # true apabila string berisikan spasi tab dll dan tidak kosong
print('Castle Of Glass'.istitle()) # true apabila berisikan kata awalan huruf kapital dan huruf kecil dst
'''

# metode startsWith() dan endsWith() dari String
'''
print('Hello World!'.startswith('Hello'))
print('Hello World!'.endswith('World!'))
'''

# metode join() da split() dari String
"""
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
"""

# metode teks rata kanan/kiri/tengah
'''
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))
'''

# hapus whithespace dengan lstrip() strip() rstrip()
'''
spam = '   Hello World   '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('aSmp'))   # menghapus huruf yang ada, tidak peduli akan urutan
'''

# mengganti string/substring dengan replace()
string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "Geeks")) # merubah geeks menjadi Geeks perhatikan huruf g dan G

string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "GeeksForGeeks", 3)) # merubah geeks menjadi GeeksForGeeks untuk 3 geeks pertama