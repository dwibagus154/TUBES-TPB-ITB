import csv

def load_tiket(): #Mengubah file menjadi array of array (data), CUMAN BUAT NGECEK PROGRAM
        ArsipTiket = open('tiket.csv','r',newline='')
        ReaderTiket = csv.reader(ArsipTiket,delimiter=',')

        TabTiketAwal = [line for line in ReaderTiket]

        return TabTiketAwal

def load_tikethilang(): #Mengubah file menjadi array of array (data), CUMAN BUAT NGECEK PROGRAM

        ArsipTiketHilang = open('tikethilang.csv','r',newline='')
        ReaderTiketHilang = csv.reader(ArsipTiketHilang,delimiter=',')

        TabTiketHilangAwal = [line for line in ReaderTiketHilang]

        return TabTiketHilangAwal

#INI PROGRAM BAGIAN GUANYA YA HEHEHEHE SISANYA CMN BUAT NGETES
def tiket_hilang(TabTiket,TabTiketHilang):
        #Fungsi yang dapat mengurangi jumlah tiket karen hiland dan menambah data baru pada arsip kehilangan tiket

        #KAMUS LOKAL
        #Username, Tanggal_Hilang, ID_Wahana: str
        #Jumlah_Hilang: int
        #tiket_hilang: array of data baru
        
        #ALGORITMA
        Username = str(input("Masukkan Username: "))
        Tanggal_Hilang = str(input("Tanggal kehilangan tiket: "))
        ID_Wahana = str(input("ID wahana: "))
        Jumlah_Hilang = int(input("Jumlah tiket yang dihilangkan: "))

        for row in TabTiket:
                if row[0]==Username and row[1]==ID_Wahana:
                        row[2] = str(int(row[2])-Jumlah_Hilang)
                        break
                
        tiket_hilang = [[Username, Tanggal_Hilang, ID_Wahana, Jumlah_Hilang]]
        TabTiketHilang = TabTiketHilang + tiket_hilang
        print(TabTiketHilang)
        
        return (TabTiket,TabTiketHilang)

def save(Tab,file_name): #CUMAN BUAT NGECEK PROGRAM
    Arsip = open(file_name,'w',newline='')
    WriterTiket = csv.writer(Arsip,delimiter=',')

    for line in Tab:
        WriterTiket.writerow(line)

    Arsip.close()

#ALGORITMA PROGRAM UTAMA - CUMAN BUAT NGECEK PROGRAM
TabTiket = load_tiket()
TabTiketHilang = load_tikethilang()
(TabTiket1,TabTiketHilang1) = tiket_hilang(TabTiket,TabTiketHilang)
save(TabTiket1,'tiket.csv')
save(TabTiketHilang1,'tikethilang.csv')
