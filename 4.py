#TODO Buatlah algoritma untuk mengkonversi total detik ke bentuk jam-menit-detik. Data total detik diinput oleh user. Contohnya, misalnya data total detiknya adalah 5440 detik, maka outputnya adalah 1 jam 30 menit 40 detik.

total_detik = int(input("Input total detik: "))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("Total konversi adalah:")
print("Jam: ", jam)
print("Menit: ", menit)
print("Detik: ", detik)