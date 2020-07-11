import csv

                    #F01 bagian load file
def load():
    userfile = input("Masukkan nama File User: ")
    global user, wahana, beli, guna, tiket, refund, krit
    user = csv.reader(open(userfile))
    wahanafile = input("Masukkan nama File Wahana: ")
    wahana = csv.reader(open(wahanafile))
    belifile = input("Masukkan nama File Pembelian Tiket: ")
    beli = csv.reader(open(belifile))
    gunafile = input("Masukkan nama File Penggunaan TIket: ")
    guna = csv.reader(open(gunafile))
    tiketfile = input("Masukkan nama File Kepemilikan Tiket: ")
    tiket = csv.reader(open(tiketfile))
    refundfile = input("Masukkan nama File Refund Tiket: ")
    refund = csv.reader(open(refundfile))
    kritfile = input("Masukkan nama File Kritik dan Saran: ")
    krit = csv.reader(open(kritfile))

load()

#

                    #F02 bagian login user

#prosedur login

def login():
#Login dapat dilakukan baik oleh pemain maupun oleh admin. 
#Login hanya dapat dilakukan jika pengguna belum login.

#KAMUS LOKAL
# f : file of str
# reader = hasil pembacaan data csv
# username, password, cekrole : str
# name, uname, pw, role : array of str
# cek : bool

#ALGORITMA
    # buka file csv dan membaca isi file
    f = open("user.csv",'r')
    reader = csv.reader(f,delimiter=',')

    # input username dan password
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # akses data per kolom
    for row in reader:
        name = row[0]
        uname =  row[3]
        pw = row[4]
        role = row[5]
        cek = False
        # pengecekan username dan password
        if username == uname and password == pw:
            cek = True
            break
        
    if cek == True: # username dan password sesuai
        print ("Selamat bersenang-senang, " + name + '!')
        # pengecekan role
        if role == 'adm' :
            cekrole = "1" #role : admin
        else:
            cekrole = "2" #role : user
    else:
        print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    
    f.close()
login()

#





