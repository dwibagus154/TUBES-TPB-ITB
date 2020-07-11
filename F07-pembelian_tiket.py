import csv

username = 'dwibagus01'
def beli_tiket () :
    id_wahana = input ('Masukkan ID wahana: ')
    tanggal_pembelian = input ('Masukkan tanggal hari ini: ') #dd/mm/yyyy
    tiket_beli = int(input('Jumlah tiket yang dibeli: '))

    #mencek nilai tinggi badan dan berat badan
    file = open("user.csv")
    r = csv.reader(file, delimiter=",")

    tabuser = [line3 for line3 in r]
    
    for line3 in tabuser:
        if line3[3] == username :
            tinggi_pemain = int(line3[2])
            tanggal_lahir = line3[1]
            saldo = int(line3[6]) 

    #mencari harga umur        
    n = int(tanggal_pembelian [6])*1000 + int(tanggal_pembelian [7])*100 + int(tanggal_pembelian [8])*10 + int(tanggal_pembelian [9])
    y = int(tanggal_lahir[6])*1000 + int(tanggal_lahir[7])*100 + int(tanggal_lahir[8])*10 + int(tanggal_lahir[9])
    umur = n-y
    if (umur==17):
        b1 = int(tanggal_pembelian [3])*10 + int(tanggal_pembelian [4])
        a1 = int(tanggal_lahir[3])*10 + int(tanggal_lahir[4])
        #cek bulannya
        if (b1<a1) :
            umur = 16
        elif (a1==b1):
            #cek tanggalnya
            a2 = int(tanggal_lahir[0])*10 + int(tanggal_lahir[1])
            b2 = int(tanggal_pembelian [0])*10 + int(tanggal_pembelian [1])
            if b2<a2 :
                umur = 16

    #
    
    #mengcek wahana 
    wahana = open ("wahana.csv",'r')
    reader2 = csv.reader(wahana,delimiter=',')

    tabwahana = [line2 for line2 in reader2]
    
    for line2 in tabwahana :
        if line2[0] == id_wahana :
            nama_wahana = line2[1]
            harga_tiket = int(line2[2])
            batasan_umur = line2[3]
            batasan_tinggi = line2[4]
            break
    #
    
    found = True
    while found == True :
        if saldo < (harga_tiket * tiket_beli):
            found = False
            print ('Saldo Anda tidak cukup')
            print ('Silakan mengisi saldo Anda')
            break 
        
        if batasan_umur == 'anak-anak' :
            if umur >= 17 :
                found = False
                print ('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                print ('Silakan menggunakan wahana lain yang tersedia.')
                break
        elif batasan_umur == 'dewasa' :
            if umur < 17 :
                found = False
                print ('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                print ('Silakan menggunakan wahana lain yang tersedia.')
                break

        if batasan_tinggi == '>= 170 cm' :
            if tinggi_pemain < 170 :
                found = False
                print ('Anda tidak memenuhi persyaratan untuk memainkan wahana ini.')
                print ('Silakan menggunakan wahana lain yang tersedia.')
                break
        break 
            
    if found == True :
        #menulis ke file kepemilikan '
        miliktiket = open ("kepemilikan_tiket.csv",'r')
        reader = csv.reader(miliktiket,delimiter=',')

        tabtiket = [line for line in reader]
    
    
        found1 = True
    
        for line in tabtiket:
            if line[0] == username:
                if line[1] == id_wahana :
                    line[2] = str (int(line[2]) + tiket_beli)
                    found1 = False
                    break
                else :
                    found1 = True
        if found1 == True :
            miliktiket = open ("kepemilikan_tiket.csv",'a')
            writer = csv.writer(miliktiket,delimiter=',')
            rekmilik = (username,id_wahana,tiket_beli)
            writer.writerow(rekmilik)

        else :
            tiket = open("kepemilikan_tiket.csv", "w", newline = "")
            writer = csv.writer(tiket,delimiter=',')
            for line in tabtiket :
                writer.writerow(line)
            tiket.close()
        
        #

        #mengganti file user
        file = open("user.csv")
        r = csv.reader(file, delimiter=",")

        tabuser = [line3 for line3 in r]
    
        for line3 in tabuser:
            if line3[3] == username :
                line3[6] = str(int(line3[6])-((tiket_beli)*int(harga_tiket)))
                break
        writer = csv.writer(open("user.csv", "w", newline = ""))
        for line3 in tabuser:
            writer.writerow(line3) 
                            

        #
        #menulis ke data pembelian 
        belitiket = open ("pembelian_tiket.csv",'a')
        writer = csv.writer(belitiket,delimiter=',')
        rekbeli = (username,tanggal_pembelian,id_wahana,tiket_beli)
        writer.writerow(rekbeli)
        print ('Selamat bersenang-senang di ',nama_wahana,'.')

        
        
    
beli_tiket()    
    
            
