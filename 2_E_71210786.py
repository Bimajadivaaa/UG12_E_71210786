#Membuat Program yang dapat menampilkan jadwal matakuliah berdasarkan Input.
#Memasukan input data
senin = ["kelas ke-1 Algoritma Graf", "kelas ke-3 Sistem Operasi", "kelas Ke-4 PAK", "kelas Ke-5 Praktikum INLAN"]
selasa = ["kelas ke-2 Matematika Teknik", "kelas ke-4 Bhs Indonesia", "kelas Ke-6 PKN"]
kamis = ["kelas ke-1 IMK", "kelas Ke-3 LogMat", "kelas ke-4 Praktekkom"]
jumat = ["kelas ke-2 Sistem Basis data", "kelas ke-4 Praktikum Sistem Basis Data", "kelas ke-6 INLAN"]
#Memasukkan String
Harikuliah = input("Hi Tutu, Silahkan Masukan hari yang ingin Anda telusuri :")
if Harikuliah == "senin" :
    ##Menggunakan fungsi range untuk menghasilkan list
    ## HK = Hari Kuliah
    for HK in range (len(senin)):
        ##Mencetak Jadwal hari senin
        print(senin[HK])
elif Harikuliah == "selasa":
    ##Menggunakan fungsi range untuk menghasilkan list
    ## HK = Hari Kuliah
    for HK in range (len(selasa)):
        ##Mencetak Jadwal hari selasa
        print (selasa[HK])
elif Harikuliah == "rabu":
    ##Mencetak Hari rabu tidak ada kelas
    print ("Hari rabu Anda tidak ada kelas")
elif Harikuliah == "kamis":
    ##Menggunakan fungsi range untuk menghasilkan list
    ## HK = Hari Kuliah
    for HK in range (len(kamis)):
        ##Mencetak Jadwal hari kamis
        print (kamis[HK])
elif Harikuliah == "jumat":
    ##Menggunakan fungsi range untuk menghasilkan list
    ## HK = Hari Kuliah
    for HK in range (len(jumat)):
        ##Mencetak Jadwal hari jumat
        print (jumat[HK])
