class kalkulator:

    def __init__(self, i=12345):
        self.i = i

    def f(self):
        return 'Hello world'


# Membuat instance dari kalkulato
k = kalkulator(i=1024)

# Mencetak atribut i dari objek k
print(k.i)

# Memanggil metode f dari objek k
k.f()
