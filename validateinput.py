while True:
    print('Enter Your Age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select new Password (letters anf numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password only contain letters and numbers.')