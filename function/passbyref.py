def changeme(mylist):
    mylist.append([1, 2, 3])
    print("Nilai di dalam fungsi: {}".format(mylist))


# Memanggil fungsi change me
mylist = [10, 20, 30]
changeme(mylist)
print("Nilai di luar fungsi: {}".format(mylist))

print('\n')


def changeme2(mylist2):
    mylist2 = [1, 2, 3, 4]  # fungsi untuk mereplace isi list
    print("Nilai di dalam fungsi: {}".format(mylist2))


# Memanggil fungsi changeme2
mylist2 = [10, 20, 30]
changeme2(mylist2)
print("Nilai di luar fungsi: {}".format(mylist2))
