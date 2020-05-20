z = 0
#1 / z

# Hasil RUN
'''
1 / z
ZeroDivisionError: division by zero
'''

try:
  x = 1 / z
  print(x)
except ZeroDivisionError:
  print("Tidak bisa membagi angka dengan nilai Nol")