# printme()  # Fungsi kosong tidak terdefinisikan

def printinfo(name, age):
    print("Name: ", name)
    print("Age: ", age)


printinfo(age=24, name="Masjaw")

print('\n')

# Fungsi dengan default argumen


def printdata(usia, nama="Member"): # Default argumen diletakan setelah argumen yang tidak memiliki nilai default
    print("Nama: ", nama)
    print("Usia: ", usia)


printdata(nama="Jawir", usia=25)
printdata(usia=24)
