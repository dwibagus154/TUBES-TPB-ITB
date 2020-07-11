import csv
def jumlah_tiket():
    csv_tiket = csv.reader(open('tiket.csv'), delimiter=";")
    wahana = csv.reader(open('wahana.csv'), delimiter=";")
    uname = input('Masukkan username: ')
    print("Riwayat :")
    
    for row in csv_tiket:
        if uname == row[0]:
            for j in wahana:
                if j[0] == row[0]:
                    print (row[1] + " | " + j[1] + " | " + row[2])
jumlah_tiket()