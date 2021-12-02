#Membuat Program yang dapat menampilkan baris deret angka genap yang terdiri dari bilangan yang tidak habis dibagi 5 ataupun 9.
#Menggunakan Perulangan "For"
##Memasukkan String Awal deret
Awalderet1 = int(input("Masukkan awal deret :"))
##Memasukkan String Akhir deret
Akhirderet1 = int(input("Masukkan akhir deret :"))
##Menggunakan fungsi range untuk menghasilkan list
## DA = Deret Angka
for DA in range (Awalderet1 ,Akhirderet1):
    if (DA%2==0) and (DA%5 !=0) and (DA%9!=0):
    #Mencetak baris Angka Genap
        print(DA ," " ,end="")