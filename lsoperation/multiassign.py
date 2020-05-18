# Assignment lebih dari 1 variabel

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size, color, disposition)
print(cat)

print('\n')
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat  # Dengan cara ini bisa memasukan sekaligus

print(cat)
print(size, color, disposition)

print('\n')
a, b = 'Alice', 'Bob'  # Dapat juga digunakan untuk menukar isi variabel
print(a)
print(b)


print('\n')
a, b = b, a
print(a)
print(b)
