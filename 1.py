# 1.Write a PYTHON program to evaluate the student performance

# Membuat Program Python untuk mengevaluasi kinerja siswa
def evaluate_performance(percentage):
    # Fungsi 'evaluasi_kinerja' menerima satu parameter yaitu 'persentase'
    if percentage >= 90:
        return "Excellent performance"
    # Jika persentase kinerja lebih besar atau sama dengan 90, maka tampilkan "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage>= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below Average performance"
    
# Menggunakan persentase siswa sebagai input
percentage = float(input("Enter the student's percentage: "))

# Mencetak kinerja nya
performance = evaluate_performance (percentage)
print("Student's Performance:", performance)
