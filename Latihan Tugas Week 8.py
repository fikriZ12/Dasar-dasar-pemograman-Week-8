def profile(nama, alamat, gender, umur, hobby):
    print("Nama Saya Adalah Fikri Ramadan")
    print("Alamat saya di JL.Rtm Gg H.lias no 7 RT 004 RW 011 DEPOK")
    print("Gender saya adalah Laki Laki")
    print("Umur Saya saat ini 19 Tahun")
    print("Hobby Saya Berenang")
profile("fikri","RTM","Laki laki","Berenang","19 Tahun")

#no 2

def tentukan_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
# Contoh penggunaan:
nilai = 70
print(tentukan_kelulusan(nilai))

#no 3
def cetak_bilangan_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
        print(nilai)

# Contoh penggunaan:
batas_tertinggi = 100
cetak_bilangan_ganjil(batas_tertinggi)