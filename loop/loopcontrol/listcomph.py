# traditional list loop insert
numbers = [1, 2, 3, 4]
square = []
for n in numbers:
  square.append(n**2) # membuat isi list number dipangkatkan lalu di input ke list square
print(square)

print('\n')

# List comprehension insert (syntax: new_list = [expression for_loop_one_or_more conditions] )
numbers = [1, 2, 3, 4]
square = [n**2 for n in numbers] # Membuat isi list square berdasar isi list number yg dipangkatkan, lebih ringkas
print(square)

# Search the same numbers in two different list (traditional method)
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []

for a in list_a:
  for b in list_b:
    if a == b:
      common_num.append(a)

print(common_num)

# With list comperhension loop search
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a==b] # Lebih ringkas
print(common_num)

print('\n')

# Convert all list into lower case
list_a = ["HeLLo", "WOrld", "In", "PytHon"]
small_list_a = [_.lower() for _ in list_a]  # Mengecilkan huruf yang ada didalam list
print(small_list_a)

print('\n')

# Kuis
list_a = range(1, 10, 2)  # Berisikan urutan angka dimulai dari 1 selisih 2 sampai 9
x = [[a**2, a**3] for a in list_a] # Setiap angka dipangkat 2 dan 3
print(x)
