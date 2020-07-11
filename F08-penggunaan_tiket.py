import csv
username = 'dwibagus01'
def main () :
    id_wahana = input ('Masukkan ID wahana: ')
    tanggal_penggunaan = input ('Masukkan tanggal hari ini: ') #dd/mm/yyyy
    tiket_guna = int(input('Jumlah tiket yang dgunakan: '))
    
    
    #mengecek kepemilikan
    miliktiket = open ("kepemilikan_tiket.csv",'r')
    reader = csv.reader(miliktiket,delimiter=',')

    tabtiket = [line for line in reader]
    
    
    found = True
    
    for line in tabtiket:
        if line[0] == username:
            if line[1] == id_wahana :
                if int(line[2]) > tiket_guna :
                    line[2] = str (int(line[2]) - tiket_guna)
                    found = False
                else :
                    found = True

    #
                
    if found == True :
        print ('Tiket Anda tidak valid dalam sistem kami')
   
    if found == False :
        #menulis ke file gunatiket
        gunatiket = open ("penggunaan.csv",'a')
        writer = csv.writer(gunatiket,delimiter=',')
        rekguna = (username,id_wahana,tanggal_penggunaan,tiket_guna)
        writer.writerow(rekguna)
        print ('Terima kasih telah bermain.')
        gunatiket.close()

        #menulis ke file kepemilikan '
        tiket = open("kepemilikan_tiket.csv", "w", newline = "")
        writer = csv.writer(tiket,delimiter=',')
        for line in tabtiket :
            writer.writerow(line)
        tiket.close()
        
        
main()
    

    
    
    
