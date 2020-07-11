#prosedur riwayat_wahana
import csv
def riwayat_wahana():
#Admin bisa melihat riwayat penggunaan wahana. 

#KAMUS LOKAL
# csv_tiket = hasil pembacaan data csv
# row : str
# wahana : str
    

#ALGORITMA
    # buka file csv dan membaca isi file
    csv_tiket = csv.reader(open('penggunaan.csv'), delimiter=";")
    
    #input ID wahana
    wahana = input('Masukkan ID Wahana: ')
    print("Riwayat :")
    
    #pengulangan untuk mencari wahana ber-ID sama dengan masukan
    for row in csv_tiket: 
        if wahana == row[2]: 
            #output dengan Format: Tanggal_Bermain | Username Pengguna | Jumlah Tiket
            print (row[0] + "|" + row[1] + "|" + row[3])
riwayat_wahana()