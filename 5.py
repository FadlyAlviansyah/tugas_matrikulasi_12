#TODO Buatlah Algoritma (Bentuk Flowchart) untuk mencetak bilangan ganjil dan genap 1 s.d 50 menggunakan While atau For (Note : Untuk setiap bilangan yang dicetak diberi keterangan jenis bilangan, contoh : 1 bilangan ganjil 2 bilangan genap ) 

for i in range(1, 51):
  if i % 2 == 0:
    print(i, " bilangan genap")
  else:
    print(i, " bilangan ganjil")