for letter in 'Python':
  if letter == 'h':
    pass
    print("This is pass block")
  print("Current letter is {}".format(letter))

print('\n')

for letter in 'Python':
  if letter.isupper():
    pass
    print("Pass block")
  else:
    print("Lower case letter: {}".format(letter))

print('\n')
'''
var1=""
while(var1!="exit"):
    var1=input("Please enter an integer (type exit to exit): ") # Program akan error karena hanya menerima inputan int
    print(int(var1))
'''

print('\n')

import sys

data = ''

while(data != 'exit'):
  try:
    data = input("Please enter an integer (Type exit to exit): ")
    print("Got integer: {}".format(int(data)))
  except:
    if data == 'exit':
      pass  # keluar dengan baik tanpa ada error
    else:
      print("error {}".format(sys.exc_info()[0]))