# cetak judul program
print('menentukan Nilai maksimum dua bilangan')

# menentukan input user
a = int(input("masukan bilangan pertama: "))
b = int(input("masukan bilangan kedua: "))

# menentukan Nilai Bilangan dengan
if a > b:
    maks = a
else:
    maks = b
# cetak Nilai maksimum
print('Nilai terbesar adalah %d' % maks)
