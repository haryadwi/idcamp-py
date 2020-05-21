'''
import hello2
'''

# Impor file
import hello  # Pastikan berada dalam direktori yang sama
# Alternatif impor file
from hello import world
# Panggil fungsi 1
hello.world()  # Tuliskan nama module lalu titik lalu nama fungsi yang ingin digunakan

print('\n')

# Pemanggilan fungsi 2
world()

print('\n')

# Cetak variable nama dari file hello
print(hello.nama)

print('\n')

# Memanggil kelas
masjaw = hello.Reviewer("Masjaw", "Python")
# Memanggil fungsi yang ada dalam kelas
masjaw.review()
