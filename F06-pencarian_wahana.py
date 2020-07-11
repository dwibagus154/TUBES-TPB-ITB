import csv
def cari() :
    wahana = open ("wahana.csv",'r')
    reader2 = csv.reader(wahana,delimiter=',')

    tabwahana = [line2 for line2 in reader2]
    
    #validasi umur    
    umur = int (input ('batasan umur pemain: '))
    while not (umur ==1 or umur == 2 or umur == 3) :
        print ('Batasan umur tidak valid!')
        umur = int (input ('batasan umur pemain: '))
        
    #validasi tinggi 
    tinggi_badan = int (input ('batasan tinggi badan: '))
    while not (tinggi_badan ==1 or tinggi_badan == 2) :
        print ('Batasan tinggi badan tidak valid!')
        tinggi_badan = int (input ('batasan tinggi badan: '))
        
  
    #program utama   

    print ('Hasil pencarian: ')
    found = True
    while found == True :
        if umur == 1 :
            if tinggi_badan == 1 : 
                for line2 in tabwahana :
                    if line2[3] == 'anak-anak' and line2[4] == '>=170 cm' :
                        print (line2[i][0] + ' | ',line2[1] + ' | ' + lines[i][2])
                        found = False
                        break 
            else: # tinggi_badan == 2: 
                for line2 in tabwahana  :
                    if line2[3] == 'anak-anak' and line2[i][4] == 'tanpa batasan' :
                        print (line2[0] + ' | ',line2[i][1] + ' | ' + line2[i][2])
                        found = False
                        break 
        elif umur == 2 :
            if tinggi_badan == 1 :
                for line2 in tabwahana  :
                    if line2[3] == 'dewasa' and  line2[4] == '>=170 cm' :
                        print (line2[0] + ' | ',line2[1] + ' | ' + line2[2])
                        found = False
                        break 
            else: # tinggi_badan == 2:
                for line2 in tabwahana :
                    if line2[3]== 'dewasa' and line2[4] == 'tanpa batasan' :
                        print (line2[0] + ' | ',line2[1] + ' | ' + line2[2])
                        found = False
                        break 
        else : # umur == 3
            if tinggi_badan == 1 : 
                for line2 in tabwahana :
                    if  line2[3]  == 'semua umur' and  line2[4] == '>=170 cm' :
                        print (line2[0] + ' | ',line2[1] + ' | ' + line2[2])
                        found = False
                        break 
            else: # tinggi_badan == 2: 
                for line2 in tabwahana :
                    if  lines[i][3] == 'semua umur' and lines[i][4] == 'tanpa batasan' :
                        print (line2[0] + ' | ',line2[1] + ' | ' + line2[2])
                        found = False
                        break
        
        break
    if found == True:
        print ('Tidak ada wahana yang sesuai dengan pencarian kamu.')
      
cari()

#ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi
#Jenis batasan umur:
#1. Anak-anak (<17 tahun) 2. Dewasa (>=17 tahun) 3. Semua umur 

#Jenis batasan tinggi badan: 1. Lebih dari 170 cm 2. Tanpa batasan



