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

print('\n')

try:
  with open('tapi_bohong.py') as file:
    print(file.read())
except (FileNotFoundError) as em:
    print("File Tidak Ditemukan")
    print("Pesan Sistem: {}".format(em))

print('\n')

# Multi Exception Handling
d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except ValueError:
    print('nilai tidak sesuai')

try:
    print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')
try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:
    print('penangan kesalahan: {}'.format(e))

