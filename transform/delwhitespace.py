# hapus whithespace dengan lstrip() strip() rstrip()

spam = '   Hello World   '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('aSmp'))   # menghapus huruf yang ada sesuai dalam parameter, tidak peduli akan urutan
