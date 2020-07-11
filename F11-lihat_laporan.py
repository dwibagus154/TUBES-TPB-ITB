import csv

def load_kritik(): #Mengubah file menjadi array of array (data), CUMAN BUAT NGECEK PROGRAM
    ArsipKritik = open('kritik.csv','r',newline='')
    ReaderKritik = csv.reader(ArsipKritik,delimiter=',')

    TabKritikAwal = [line for line in ReaderKritik]

    return TabKritikAwal

def panjang_Tab(Tab):
    #Menghitung panjang data Tab
    #Input: Array yang ingin dihitung banyak datanya
    #Output: Jumlah data pada suatu array

    #KAMUS LOKAL
    #count: int (count merupakan banyaknya data)
    
    count = 0
    for row in Tab:
        if Tab[0] != '':
            count += 1
    
    return count

def kolom_IDWahana(Tab):
    #Mengubah arsip kritik dan saran HANYA menjadi satu kolom, yaitu kolom ID_Wahana
    #Input: Arsip yang ingin diambil HANYA kolom ID_Wahana nya, yaitu arsip dari load_kritik()
    #Output: Array yang hanya berisi ID_Wahana saja

    #KAMUS LOKAL
    #TabBaru: array of str (array yang berisi ID_Wahana pada setiap rekaman)
    #row_ke: int (row_ke menyatakan baris ke berapa)
    
    TabBaru = ['' for i in range (panjang_Tab(Tab))]

    row_ke = 0
    for row in Tab:
        TabBaru[row_ke] = row[2]
        row_ke += 1
    
    return TabBaru

def sorting_IDWahana(Tab):
    #Mengurutkan ID_Wahana secara alfabetis. Sorting dilakukan dengan menggunakan selection sort
    #Input: Array yang diurutkan adalah array dari hasil fungsi kolom_IDWahana(Tab)
    #Output: Array yang sudah terurut ID_Wahana nya

    #KAMUS LOKAL
    #p: int (p atau pass menyatakan tahapan pengurutan)
    #i: int (indeks untuk pengulangan for)
    #Temp: int (memorisasi harga untuk penukaran)
    #IMin: int (indeks, dimana T[p..N] bernilai maksimum)
    
    if panjang_Tab(Tab)>1:
        for p in range (0,panjang_Tab(Tab)-1):
            IMin = p

            for i in range (p+1, panjang_Tab(Tab)):
                if (ord(Tab[IMin][0]) > ord(Tab[i][0])):
                    IMin = i
                elif (ord(Tab[IMin][0]) == ord(Tab[i][0])):
                    if (ord(Tab[IMin][1]) > ord(Tab[i][1])):
                        IMin = i
                    elif (ord(Tab[IMin][0]) == ord(Tab[i][0])):
                        if (ord(Tab[IMin][2]) > ord(Tab[i][2])):
                            IMin = i
                        elif (ord(Tab[IMin][2]) == ord(Tab[i][2])):
                            if (Tab[IMin][3]*100+Tab[IMin][4]*100+Tab[IMin][5]) > (Tab[i][3]*100+Tab[i][4]*100+Tab[i][5]):
                                IMin = i
                    
            Temp = Tab[IMin]
            Tab[IMin] = Tab[p]
            Tab[p] = Temp

    return Tab

def lihat_laporan(IDWahana_sorted,TabKritik):
    #Menampilkan kritik dan saran yang sudah mengurut berdasarkan ID_Wahana
    #Input: Array yang berisi HANYA ID_Wahana (sorted) dan array berisi rekaman2 data kritik
    #Output: Ditampilkan ke layar laporan kritik dan saran yang mengurut berdasarkan ID_Wahana

    #KAMUS LOKAL
    #row_ke: int (row_ke menyatakan rekaman tsb ada di baris ke berapa)

    row_ke = 0
    for row in IDWahana_sorted:
        for row in TabKritik:
            if IDWahana_sorted[row_ke] == row[2] and row[3] != '': #row[3] = '' menandakan bahwa rekaman tsb sudah dicetak
                print(row[2]+" | "+row[1]+" | "+row[0]+" | "+row[3])
                row[3] = '' #utk menandakan bahwa rekaman tsb sudah dicetak
                
        row_ke += 1


#PERCOBAAN !!!
lihat_laporan(sorting_IDWahana(kolom_IDWahana(load_kritik())),load_kritik())
