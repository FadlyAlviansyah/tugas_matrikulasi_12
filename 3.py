#TODO Buatlah algoritma untuk mengkonversi jam-menit-detik ke total detik. Data jam- menit-detik diinput dari user. Contoh, misalnya data jam-menit-detiknya adalah 1 jam 30 menit 40 detik, maka besarnya total detik adalah 5440 detik. Analisis: input: jam (j), menit (m), detik (d) output: total detik (total) Rumus: ingat bahwa 1 jam = 3600 detik dan 1 menit = 60 detik. maka total detik = jam x 3600 + menit x 60 + detik.

jam = int(input("Input jam: "))
menit = int(input("Input menit: "))
detik = int(input("Input detik: "))

total = jam * 3600 + menit * 60 + detik

print("Total detik adalah: " + str(total) + " detik")