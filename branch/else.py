amount = int(input("Enter Amount: "))

if amount < 1000:
  discount = amount * 0.05
  print("Discount ", discount)
else:
  discount = amount * 0.10
  print("Discount ", discount)

print("Net Payable: ", amount - discount)

print('\n')
angka = int(input("Masukan Angka: "))

if angka % 2 == 0:
  print("Merupakan Bilangan Genap.")
else:
  print("Merupakan Bilangan Ganjil")
