import csv

def load_user(): #Mengubah file menjadi array of array (data), CUMAN BUAT NGECEK PROGRAM
        ArsipUser = open('user.csv','r',newline='')
        ReaderUser = csv.reader(ArsipUser,delimiter=',')

        TabUserAwal = [line for line in ReaderUser]

        return TabUserAwal

def topup(TabUser):
        #Fungsi yang dapat menambahkan saldo pemain

        #KAMUS LOKAL
        #Username: str
        #Saldo: int
        
        #ALGORITMA
        Username = str(input("Masukkan username: "))
        Saldo = int(input("Masukan saldo: "))

        for row in TabUser:
                if row[3]==Username:
                        row[6] = str(int(row[6])+Saldo)
                        break

        return TabUser                

def save_user(TabUser): #CUMAN BUAT NGECEK PROGRAM
    ArsipUser = open('user.csv','w',newline='')
    WriterUser = csv.writer(ArsipUser,delimiter=',')

    for line in TabUser:
        WriterUser.writerow(line)

    ArsipUser.close()

#ALGORITMA PROGRAM UTAMA - CUMAN BUAT NGECEK PROGRAM
TabUser = load_user()
TabUserAkhir = topup(TabUser)
TabUserAkhir1 = topup(TabUserAkhir)
save_user(TabUserAkhir1)
