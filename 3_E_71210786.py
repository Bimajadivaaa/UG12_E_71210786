#Membuat Program yang dapat membuat output berupa bentuk bangun datar belah ketupat sesuai dengan panjang diagonal 
#Memasukkan String
IA = int(input("Masukkan Angka :"))
BatasAngka=IA;
###Menggunakan fungsi range untuk menghasilkan list
for i in range (0,IA):
	for model in range (-2, BatasAngka+1):
		#Mencetak list
		print(" ",end="")
	for bangundatar in range(0, i+1):
		#Mencetak list
		print("* ", end="")
	BatasAngka-=1
	#Mencetak bangun datar belah ketupat
	print("")

BatasAngka=IA;
###Menggunakan fungsi range untuk menghasilkan list
for i in range (1,IA):
	for model in range(-4, i):
		#Mencetak list
		print(" ",end="")
	for bangundatar in range (1,BatasAngka):
		#Mencetak list
		print("* ",end="")
	BatasAngka-=1
	#Mencetak bangun datar belah ketupat
	print("")