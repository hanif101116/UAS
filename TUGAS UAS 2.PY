# Program Sederhana dengan 30 Baris

# 1. Import modul untuk mendapatkan input dari pengguna
nama = input("Masukkan nama Anda: ")

# 2. Sapa pengguna
print("Halo, " + nama + "! Selamat datang di program sederhana.")

# 3. Input bilangan pertama
bilangan1 = float(input("Masukkan bilangan pertama: "))

# 4. Input bilangan kedua
bilangan2 = float(input("Masukkan bilangan kedua: "))

# 5. Operasi penjumlahan
hasil_penjumlahan = bilangan1 + bilangan2
print("Hasil penjumlahan:", hasil_penjumlahan)

# 6. Operasi pengurangan
hasil_pengurangan = bilangan1 - bilangan2
print("Hasil pengurangan:", hasil_pengurangan)

# 7. Operasi perkalian
hasil_perkalian = bilangan1 * bilangan2
print("Hasil perkalian:", hasil_perkalian)

# 8. Operasi pembagian
# Tambahkan penanganan kesalahan untuk pembagian oleh nol
try:
    hasil_pembagian = bilangan1 / bilangan2
    print("Hasil pembagian:", hasil_pembagian)
except ZeroDivisionError:
    print("Error: Pembagian oleh nol tidak diizinkan.")

# 9. Perulangan untuk menampilkan angka 1-5
print("Angka 1-5:")
for i in range(1, 6):
    print(i, end=" ")

# 10. Perulangan while untuk menghitung mundur
print("\nHitung mundur dari 3:")
counter = 3
while counter > 0:
    print(counter, end=" ")
    counter -= 1

# 11. Fungsi sederhana
def pangkat_dua(angka):
    return angka ** 2

# 12. Panggil fungsi dengan parameter
angka_input = float(input("\nMasukkan angka untuk dipangkatkan dua: "))
hasil_pangkat_dua = pangkat_dua(angka_input)
print("Hasil pangkat dua:", hasil_pangkat_dua)

# 13. Pernyataan kondisional sederhana
if hasil_pangkat_dua > 10:
    print("Hasil pangkat dua lebih dari 10.")
else:
    print("Hasil pangkat dua 10 atau kurang.")
