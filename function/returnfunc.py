def sum(arg1, arg2):
  total = arg1 + arg2
  print("Inside the function: {}".format(total))
  return total  # Mengembalikan hasil proses sum ke variable total sehingga bisa dicetak tanpa pemanggilan fungsi ulang

# Memanggil Fungsi
total = sum(10, 20)
print("Outside the function: {}".format(total))

print('\n')

def kuadrat(x):
  return x*x

a = 10
k = kuadrat(a)

print("Nilai kuadrat dari {} adalah: {}".format(a, k))
print(k)