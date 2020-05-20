def printinfo(fixedarg, *args):  # *args merupakan variable penampung untunk inputan tuple
    print("Output: fixedarg {}".format(fixedarg))
    for a in args:
        print("Argumen posisi {}".format(a))


#  Pemanggilan fungsi
printinfo(10)
printinfo(70, 60, 50)

print('\n')


def printdata(*args, **kwargs):
    for a in args:
        print("Argumen posisi {}".format(a))
    for key, value in kwargs.items(): # Untuk memasukan dictioanry
        print("Argumen kata kunci {}: {}".format(key, value))


#  Pemanggilan fungsi
printdata()
printdata(1, 2, 3)
printdata(x=7, y=8, z=9)
printdata(1, 2, y=8, z=9)
printdata(*(2, 3), **{'x':7, 'y':8})