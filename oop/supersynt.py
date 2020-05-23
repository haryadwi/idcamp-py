class Kalkulator:
  ''' Kelas kalkulator sederhana tidak boleh diubah '''

  def __init__(self, nilai=0):
    self.nilai = nilai

  def tambah_angka(self, angka1, angka2):
    self.nilai = angka1 + angka2
    if self.nilai > 9:
      print('Kalkulator sederhana melebihin batas angka: {}'.format(self.nilai))
    return self.nilai

class KalkulatorKali(Kalkulator): 
  ''' Mewarisi kelas kalkulator sederhana '''

  def kali_angka(self, angka1, angka2):
    self.nilai = angka1 * angka2
    return self.nilai
  
  '''Override methods untung menghilangkan warning dari metode tambah angka kalkulator sederhana'''
  def tambah_angka(self, angka1, angka2):
    self.nilai = angka1 + angka2
    return self.nilai

class KalkulatorTambah(Kalkulator):
  ''' Mewarisi kelas kalkulator sederhana '''

  def tambah_angka(self, angka1, angka2):
    if angka1 + angka2 <= 9: # Fitur yang sudah baik di kelas dasar
      super().tambah_angka(angka1, angka2) # Panggil fungsi dari Kalkulator lalu diisi oleh nilai
    else: # Fitur baru yang ingin diperbaiki  dari keterbatasan kelas dasar (fitur baru Kalkulator tambah)
      self.nilai = angka1 + angka2
    return self.nilai

# Pemanggilan class kalkulator kali
kk = KalkulatorKali()
a = kk.kali_angka(2, 3) # Memeliki objek kali angka fitur aseli Kalkulator kali
print(a)
b = kk.tambah_angka(5, 6) # Memiliki objek tambah angka fitur warisan dari Kalkulatot sederhana
print(b)

# Pemanggilan class kalkulati tambah
kt = KalkulatorTambah()
a = kt.tambah_angka(6, 6)
print(a)