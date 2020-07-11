import csv
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
