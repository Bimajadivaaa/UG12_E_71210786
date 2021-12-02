#Membuat Program yang memiliki fungsi nilai maksimal yang bisa menghasilkan nlai terkecil dan nilai terbesar dari sebuah deret bilangan yang berisi 5 angka.
### Membuat Tanpa menggunakan fungsi MAX dan MIN 
#Memasukkan Fungsi def
def hasil_1(deretangka):
    hasil_terbesar = deretangka[0]
    for i in deretangka:
      #Mencari Hasil yang terbesar
      if i > (hasil_terbesar):
        hasil_terbesar = i
    return hasil_terbesar
#Memasukkan Fungsi def
def hasil_2(deretangka):
    hasil_terkecil = deretangka[0]
    for i in deretangka:
      #Mencari Hasil yang terkecil
      if i < (hasil_terkecil):
        hasil_terkecil = i
    return hasil_terkecil
#Memasukkan Input Deret Bilangan 1
DeretBilangan1 = [3, 20, 100, -35, 50]
#Memasukkan Input Deret Bilangan 1
DeretBilangan2 = [3, 20, 90, 35, 75]
#Mencetak Deret Bilangan 1
print(DeretBilangan1)
#Mencetak Nilai terbesar & Terkecil pada Deret Bilangan 1
print("Nilai terbesar:", hasil_1(DeretBilangan1))
print("Nilai terkecil:", hasil_2(DeretBilangan1))
#Mencetak Deret Bilangan 2
print(DeretBilangan2)
#Mencetak Nilai terbesar & Terkecil pada Deret Bilangan 1
print("Nilai terbesar:", hasil_1(DeretBilangan2))
print("Nilai terkecil:", hasil_2(DeretBilangan2))