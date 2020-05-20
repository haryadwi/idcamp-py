total = 0  # Variable global


def sum(arg1, arg2):
    # Penjumlahan 2 parameter
    total = arg1 + arg2
    print("Inside the function: {}".format(total))
    return total


# Pemanggilan fungsi
sum(10, 20)
print("Outside the function: {}".format(total))

print('\n')


def jml(arg1, arg2):
    global total  # Definisi bahwa ini variable global
    total = arg1 + arg2
    print("Inside the function local total: {}".format(total))
    return total


# Pemanggilan fungsi
jml(10, 20)
print("Outside thr function global total: {}".format(total))
