#TODO Buatlah Algoritma dalam bentuk pseudocode untuk mencari bilangan terbesar dari 3 bilangan dengan aturan bilangan

bil1 = input("Input bilangan 1: ")
bil2 = input("Input bilangan 2: ")
bil3 = input("Input bilangan 3: ")

if(bil1 > bil2 and bil1 > bil3):
  print("Bilangan terbesar adalah " + bil1)
elif(bil2 > bil1 and bil2 > bil3):
  print("Bilangan terbesar adalah " + bil2)
elif(bil3 > bil1 and bil3 > bil2):
  print("Bilangan terbesar adalah " + bil3)
else:
  print("Ada bilangan yang sama!")