# Fungsi-Python-Dani-Fricilia
#Program Kalkulator Sederhana
#Job Sheet 4 Dasar Pemrograman

def luas_bujur_sangkar(sisi) :
    luas = sisi * sisi
    return luas
def keliling_bujur_sangkar(sisi) :
    keliling = 4 * sisi
    return keliling
def luas_persegi_panjang(panjang,lebar) :
    luas = panjang * lebar
    return luas
def keliling_persegi_panjang(panjang,lebar):
    keliling = 2 * (panjang + lebar) 
    return keliling
def luas_segitiga(alas,tingi) :
    luas = 0.5 * alas * tinggi
    return luas
def keliling_segitiga(a, b, c) :
    keliling = a + b + c
    return keliling
def luas_lingkaran(radius) :
    luas = 3.14 * radius * radius
    return luas
def keliling_lingkaran(radius) :
    keliling = 2 * 3.14 * radius
    return keliling
pilihan = 1
while pilihan !=0:
    print('PEMBELAJARAN MATEMATIKA SEDERHANA')
    print('SILAHKAN PILIH OPSI')
    print('1. Luas bujur sangkar')
    print('2. Keliling bujur sangkar')
    print('3. Luas persegi panjang')
    print('4. Keliling persegi panjang')
    print('5. Luas segitiga')
    print('6. Keliling segitiga')
    print('7. Luas Lingkaran')
    print('8. Keliling Lingkaran')
    print('0. exit')
