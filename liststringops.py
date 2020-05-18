'''
l = [1, 2, 3, 3, 4, 4, 4, 4, 5, 6]  # tipe data list
s = set(l)  # menjadikan tipe data set, saat di print tidak ada angka yang sama
x = "Hello, World"

print(l)
print(len(l))  # menghitung jumlah list

print(s)
print(len(s))  # menghitung jumlah set

print(x)
print(len(x))  # menghitung jumlah string pada x
'''

# Penggabungan dan replikasi pada list
'''
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

arr = [0] * 10
print(len(arr))
print(arr)
'''

# Range
'''
# 1 parameter
for i in range(9):  # Membuat deret bilangan dari 0 sebanyak n bilangan
    print(i)

print('\n')
# 2 parameter
for i in range(3, 9):  # Membuat deret bilangan dari n hingga sebelum p
    print(i)

print('\n')
# 3 parameter
for i in range(1, 9, 2):  # Membuat deret bilangan dari n hingga sebelum p dengan selisih q
    print(i)
'''

# In dan Not In
'''
# Untuk mengetahui nilai objek dalam list, hasil output boolean true/false
print('howdy' in ['hello', 'hey', 'howdy', 'heyas'])

print('\n')
spam = ['hello', 'hey', 'howdy', 'heyas']
print('cat' in spam)

print('\n')
print('howdy' not in spam)

print('\n')
print('cat' not in spam)
'''

# Assingment lebih dari 1 variabel
'''
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)
print(color)
print(disposition)

print('\n')
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat  # Dengan cara ini bisa memasukan sekaligus

print(cat)
print(size)
print(color)
print(disposition)

a, b = 'Alice', 'Bob'  # Dapat juga digunakan untuk menukar isi variabel
print(a)
print(b)


print('\n')
a, b = b, a
print(a)
print(b)
'''

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
