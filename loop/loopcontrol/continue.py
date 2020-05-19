for letter in 'Python':
    if letter == 'h':  # Huruf h akan dilewat saat perulangan
        continue
    print("Current letter: {}".format(letter))

print('\n')

for a in [0, 1, -1, 2, -2, 3, -3]:
    if a <= 0:  # Bilangan negatif pada list tidak akan diulang
        continue    
    print("Elemen Positif: {}".format(a))

print('\n')

var = 10

while var > 0:
  var = var - 1
  if var == 5: # Angka 5 akan di lewat saat pengulangan
    continue
  print("Current variable value: {}".format(var))