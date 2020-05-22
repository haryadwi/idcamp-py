class Kalkulator:

    def __init__(self, i=12345):
        self.i = i

    def f(self):
        return 'Hello world'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)
    
    @classmethod
    def kali_angka(cls, angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)

# Membuat instance dari kalkulator
k = Kalkulator(i=1024)
# Mencetak atribut i dari objek k
print(k.i)

print('\n')

# Pemanggilan dari class tambah angka
print(Kalkulator.tambah_angka(1, 2))

print('\n')

# Pemanggilan dari objek tambah angka
k = Kalkulator # Instansiasi dari class Kalkulator
print(k.tambah_angka(1, 2))

print('\n')

# Pemanggilan static method dari class kali angka
a = Kalkulator.kali_angka(3, 4)
print(a)

print('\n')

# Pemanggilan static method dari objek kali angka
k = Kalkulator()
a = k.kali_angka(3, 4)
print(a)