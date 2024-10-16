#Nomer 4
n = int(input("Masukkan nilai n: ")) #menampilkan pesan "Masukkan nilai n: " di layar dan menunggu pengguna untuk memasukkan nilai.

# Menggunakan loop untuk mencetak angka ganjil
print("Angka ganjil hingga", n, ":") # mencetak pesan "Angka ganjil hingga" diikuti oleh nilai n,
for i in range(1, n + 1): # Baris ini memulai sebuah loop for yang akan mengulangi proses untuk setiap angka dari 1 hingga n (inklusif).
    if i % 2 != 0:
        print(i) # mencetak nilai i ke layar.