#prosedur tambah_wahana
def tambah_wahana():
#Admin dapat menambahkan wahana baru ke dalam manajemen wahana.

#KAMUS LOKAL
# f : file of string
# reader = hasil pembacaan data csv
# idwahana, wahana, harga, umur, tinggi : str
# wahana = array berisi hasil input
# total = array gabungan data awal dengan hasil input

#ALGORITMA
    # buka file csv dan membaca isi file
    f = open('wahana.csv')
    reader = f.readlines()
    
    print("Masukkan Informasi Wahana yang ditambahkan: ")
    
    #input informasi wahana
    idwahana = input("Masukkan ID Wahana: ")
    wahana = input ("Masukkan Nama Wahana:")
    harga = input("Masukkan Harga Tiket: ")
    umur = input("Batasan umur: ")
    tinggi = input("Batasan tinggi badan: ")
    print("Info wahana telah ditambahkan!")
    
    #hasil input disimpan dalam array
    wahana = [idwahana+";"+wahana+";"+harga+";"+umur+";"+tinggi+'\n']
    
    #array gabungan data awal dengan hasil input
    total = reader + wahana

    f.close()
tambah_wahana()