def printinfo(fixedarg, *args): # *args merupakan variable penampung untunk inputan tuple
  print("Output: fixedrag {}".format(fixedarg))
  for a in args:
    print("Argumen posisi {}".format(a))

#  Pemanggilan fungsi
printinfo(70)
printinfo(70, 60, 50)