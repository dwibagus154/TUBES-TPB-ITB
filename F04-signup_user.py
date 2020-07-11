#prosedur sign_up
def signup():
#Pendaftaran pemain hanya dapat dilakukan oleh admin dan tidak diizinkan memasukkan username yang sudah terdaftar. 

# KAMUS LOKAL
# f : file of string
# reader = hasil pembacaan data csv
# Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, Role, Saldo : str
# user = array berisi hasil input
# total = array gabungan data awal dengan hasil input

#ALGORITMA
    # buka file csv dan membaca isi file
    f = open('user.csv')
    reader = f.readlines()
    
    ##input data
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan pemain (cm): ")
    Username = input("Masukkan username pemain: ")
    #pengecekan username yang sudah terdaftar
    for row in f:
        while Username == row[3]:
            Username = input("Username sudah dipakai. Masukkan username lain: ")
    Password = input("Masukkan password pemain: ")
    Role = "user"
    Saldo = "0"
    
    #hasil input disimpan dalam array
    user = [Nama+";"+Tanggal_Lahir+";"+Tinggi_Badan+";"+Username+";"+Password+";"+Role+";"+Saldo+'\n']

    #array gabungan data awal dengan hasil input
    total = reader + user
    
    f.close()
    print("Selamat menjadi pemain, Willy Wangky. Selamat bermain.")

signup()