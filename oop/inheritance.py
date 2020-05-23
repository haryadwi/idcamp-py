class Kalkulator:
  ''' Kelas kalkulator sederhana '''

  def __init__(self, nilai=0):
    self.nilai = nilai

  def tambah_angka(self, angka1, angka2):
    self.nilai = angka1 + angka2
    if self.nilai > 9:
      print('Kalkulator sederhana melebihin batas angka: {}'.format(self.nilai))
    return self.nilai

class Kalkulatorkali(Kalkulator): 
  ''' Mewarisi kelas kalkulator sederhana '''

  def kali_angka(self, angka1, angka2):
    self.nilai = angka1 * angka2
    return self.nilai

# Pemanggilan class kalkulator kali
kk = Kalkulatorkali()
a = kk.kali_angka(2, 3) # Memeliki objek kali angka fitur aseli Kalkulator kali
print(a, '\n')

b = kk.tambah_angka(2, 3) # Memiliki objek tambah angka fitur warisan dari Kalkulatot sederhana
print(b)