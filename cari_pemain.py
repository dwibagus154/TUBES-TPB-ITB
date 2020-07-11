import csv


def CariPemain():
    user = input('Masukkan username:')
    userfile = csv.reader(open('user.csv'))
    found = False
    for row in userfile:
        if user == row[3]:
            found = True
            print("Nama Pemain: ", row[0])
            print("Tinggi Pemain: ", row[2])
            print("Tanggal Lahir Pemain: ", row[1])
    if found == False:
        print("Pemain tidak ditemukan")

CariPemain()

