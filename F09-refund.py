import csv
username = 'dwibagus01'
def refund ():
    
    id_wahana = input ('Masukkan ID wahana: ')
    tiket_refund = int(input('Jumlah tiket yang di-refund: '))
    tanggal_refund = input ('masukkan tanggal hari ini: ') #dd/mm/yyyy


    #mengecek kepemilikan
    miliktiket = open ("kepemilikan_tiket.csv",'r')
    reader = csv.reader(miliktiket,delimiter=',')

    tabtiket = [line for line in reader]
    
    
    found = True
    
    for line in tabtiket:
        if line[0] == username:
            if line[1] == id_wahana :
                if int(line[2]) > tiket_refund :
                    line[2] = str (int(line[2]) - tiket_refund)
                    found = False
                else :
                    found = True

    #



    #mengcek harga tiket
    wahana = open ("wahana.csv",'r')
    reader2 = csv.reader(wahana,delimiter=',')

    tabwahana = [line2 for line2 in reader2]

    for line2 in tabwahana :
        if line2[0] == id_wahana:
            harga_tiket = line2[2]
            break
    print((tiket_refund)*int(harga_tiket))
    #     

    if found == True :
        print ('Anda tidak memiliki tiket terkait.')

    if found == False :
        #menulis ke dalam refund 
        refundtiket = open ("refund.csv",'a')
        writer = csv.writer(refundtiket,delimiter=';')
        rek_refund = (username,tanggal_refund,id_wahana,tiket_refund)

        writer.writerow(rek_refund)
        print ('Terima kasih telah bermain.')
        #

        #mengubah nilai user
        file = open("user.csv")
        r = csv.reader(file, delimiter=",")

        tabuser = [line3 for line3 in r]
        for line3 in tabuser:
                if line3[3] == username:
                        line3[6] = str(int(line3[6])+((tiket_refund)*int(harga_tiket)))
                        break
            
        writer = csv.writer(open("user.csv", "w", newline = ""))
        for line3 in tabuser:
            writer.writerow(line3)
        #
        
        #menulis ke file kepemilikan '
        tiket = open("kepemilikan_tiket.csv", "w", newline = "")
        writer = csv.writer(tiket,delimiter=',')
        for line in tabtiket :
            writer.writerow(line)
        tiket.close()
        
refund()


    
    



