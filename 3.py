#3
# menampilkan pesan "Masukkan nilai n: " di layar dan menunggu pengguna untuk memasukkan nilai
n = int(input("Masukkan nilai n: "))

a, b = 0, 1 # Baris ini mendefinisikan dua variabel, a dan b. Variabel a diinisialisasi dengan 0 (angka pertama dalam deret Fibonacci), dan b diinisialisasi dengan 1 (angka kedua dalam deret Fibonacci).
hasil = [] # Baris ini mendeklarasikan sebuah list kosong bernama hasil
9
for i in range(n): # Baris ini memulai sebuah loop for yang akan berjalan sebanyak n kali. Fungsi range(n) menghasilkan urutan angka dari 0 hingga n-1.
    hasil.append(a)
    a, b = b, a + b

print("Deret Fibonacci hingga", n, ":", hasil) #untuk menampilkan string "Deret Fibonacci hingga", diikuti oleh nilai n,dan list hasil yang berisi angka-angka dalam deret Fibonacci yang telah dihasilkan.