#TODO Susun algoritma (flowchart) dan program dengan PHP untuk menginput 10 buah bilangan yang merupakan nilai ujian siswa, kemudian cetak nilai tertinggi yang didapat siswa, serta mencetak ada berapa orang siswa yang mendapat nilai tertinggi tersebut.

total_nilai = []

for i in range(10):
  nilai = int(input(f"Input nilai ujian siswa ke-{i+1}: "))
  total_nilai.append(nilai)

nilai_terbesar = max(total_nilai)

hitung_nilai_terbesar = total_nilai.count(nilai_terbesar)

print(f"Nilai tertinggi adalah: {nilai_terbesar}")
print(f"Jumlah siswa yang mendapat nilai {nilai_terbesar}: {hitung_nilai_terbesar}")