# Sort

x = [2, 5, 3.14, 1, -7]
x.sort()    # Mengurutkan dari nilai terkkecil ke terbesar
print(x)

print('\n')
y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
y.sort()    # Mengurutkan huruf pertama dari awal asc
print(y)

print('\n')
y.sort(reverse=True)    # Mengurutkan huruf pertama dari akhir desc
print(y)

print('\n')
m = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
m.sort()    # Huruf uppercase akan diurutkan terlebih dahulu
print(m)

print('\n')
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)    # Mengurutkan berdasar huruf tanpa memperhatikan upper case
print(spam)
