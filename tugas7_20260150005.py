# Mengimpor fungsi dari modul_evaluasi
from modul_evaluasi import (
    hitung_persentase_presensi,
    hitung_nilai_akhir,
    cek_kelayakan_aslab
)


# Fungsi validasi input angka
def input_angka_valid(prompt, min_val, max_val):
    while True:
        try:
            angka = float(input(prompt))

            if angka < min_val or angka > max_val:
                print("Warning: Angka di luar batas!")
                print(f"Masukkan angka antara {min_val} sampai {max_val}.")

            else:
                return angka

        except ValueError:
            print("Error: Input harus berupa angka!")
            print("Silakan masukkan kembali.")


# Program utama
while True:
    print("\n===================================")
    print(" SISTEM EVALUASI KELAYAKAN ASLAB AI")
    print("===================================")
    print("1. Hitung Kelayakan")
    print("2. Keluar")

    try:
        pilihan = int(input("Pilih menu (1/2): "))

        if pilihan == 2:
            print("\nTerima kasih telah menggunakan program!")
            break

        elif pilihan == 1:
            print("\n--- INPUT DATA MAHASISWA ---")

            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")

            hadir = input_angka_valid(
                "Jumlah Kehadiran (0-14): ", 0, 14
            )

            tugas = input_angka_valid(
                "Nilai Tugas (0-100): ", 0, 100
            )

            ucp1 = input_angka_valid(
                "Nilai UCP 1 (0-100): ", 0, 100
            )

            ucp2 = input_angka_valid(
                "Nilai UCP 2 (0-100): ", 0, 100
            )

            # Menghitung hasil
            persentase = hitung_persentase_presensi(hadir)
            nilai_akhir = hitung_nilai_akhir(tugas, ucp1, ucp2)
            status = cek_kelayakan_aslab(
                persentase, nilai_akhir
            )

            # Menampilkan hasil
            print("\n===================================")
            print("       HASIL EVALUASI ASLAB")
            print("===================================")
            print(f"Nama                 : {nama}")
            print(f"NIM                  : {nim}")
            print(f"Jumlah Kehadiran     : {hadir:.0f}/14")
            print(f"Persentase Kehadiran : {persentase:.2f}%")
            print(f"Nilai Tugas          : {tugas:.2f}")
            print(f"Nilai UCP 1          : {ucp1:.2f}")
            print(f"Nilai UCP 2          : {ucp2:.2f}")
            print(f"Nilai Akhir          : {nilai_akhir:.2f}")
            print("-----------------------------------")
            print(f"STATUS               : {status}")
            print("===================================")

        else:
            print("Pilihan tidak tersedia! Pilih 1 atau 2.")

    except ValueError:
        print("Error: Menu harus diisi dengan angka!")