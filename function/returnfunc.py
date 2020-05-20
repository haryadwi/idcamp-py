def sum(arg1, arg2):
  total = arg1 + arg2
  print("Inside the function: {}".format(total))
  return total  # Mengembalikan hasil proses sum ke variable total sehingga bisa dicetak tanpa pemanggilan fungsi ulang

# Memanggil Fungsi
total = sum(10, 20)
print("Outside the function: {}".format(total))