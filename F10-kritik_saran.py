import csv

Username = 'hohoho' #CUMAN BUAT NGECEK PROGRAM

def load_kritik(): #Mengubah file menjadi array of array (data), CUMAN BUAT NGECEK PROGRAM
    ArsipKritik = open('kritik.csv','r',newline='')
    ReaderKritik = csv.reader(ArsipKritik,delimiter=',')

    TabKritikAwal = [line for line in ReaderKritik]

    return TabKritikAwal

#SEBENERNYA PROGRAMNYA YANG INI AJA HEHEHE SISANYA BUAT TRIAL DOANG
def kritik_saran(TabKritik):
    #Fungsi yang akan mengembalikan array TabKritik yang sudah ditambah dengan data baru dari masukan user

    #KAMUS LOKAL
    #kritik_baru: array of data
    #ID_Wahana, Tanggal_Kritik, Isi_Kritik: string
    
    #ALGORTIMA
    #Inisialisasi array kritik_baru
    kritik_baru = ['' for i in range(4)]

    #Program menerima masukan dari user
    ID_Wahana = input("Masukkan ID Wahana: ")
    Tanggal_Kritik = input("Masukkan tanggal pelaporan: ")
    Isi_Kritik = input("Kritik/saran Anda: ")

    #Masukan dari user diubah menjadi bentuk array
    kritik_baru = [[Username, Tanggal_Kritik, ID_Wahana, Isi_Kritik]]

    #Menambahkan data baru ke TabKritik
    TabKritik = TabKritik + kritik_baru

    return TabKritik

def save_kritik(TabKritik): #CUMAN BUAT NGECEK PROGRAM
    ArsipKritik = open('kritik.csv','w',newline='')
    WriterKritik = csv.writer(ArsipKritik,delimiter=',')

    for line in TabKritik:
        print (line)
        WriterKritik.writerow(line)

    ArsipKritik.close()

#ALGORITMA PROGRAM UTAMA - CUMAN BUAT NGECEK PROGRAM
TabKritik = load_kritik()
TabKritikAkhir = kritik_saran(TabKritik)
TabKritikAkhir1 = kritik_saran(TabKritikAkhir)
save_kritik(TabKritikAkhir1)
