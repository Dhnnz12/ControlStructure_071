#Nomer 5

n = int(input("Masukkan nilai n: ")) #menampilkan pesan "Masukkan nilai n: " di layar dan menunggu pengguna untuk memasukkan nilai.

# Menggunakan loop untuk mencetak desain angka
for i in range(1, n + 1): # Baris ini memulai loop for yang akan mengiterasi variabel i dari 1 hingga n (inklusif). Fungsi range(1, n + 1) menghasilkan urutan angka mulai dari 1 hingga n.
    for j in range(i): # Baris ini memulai loop for kedua, yang akan mengiterasi variabel j dari 0 hingga i-1. Jadi, jumlah iterasi untuk loop ini adalah sama dengan nilai i
        print(i, end=" ") # Baris ini mencetak nilai i, tetapi dengan argumen end=" " yang digunakan untuk menghindari pemindahan baris setelah mencetak.
    print()