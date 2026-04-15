import random

# =========================
# FUNGSI NILAI NAMA
# =========================
def nilai_nama(nama):
    total = 0
    for huruf in nama.lower():
        if huruf.isalpha():
            total += ord(huruf) - 96
    return total

# =========================
# FUNGSI ZODIAK
# =========================
def zodiak(tanggal, bulan):
    if (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        return "Aries"
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        return "Taurus"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        return "Gemini"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        return "Cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        return "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        return "Virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        return "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        return "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        return "Sagittarius"
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        return "Capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        return "Aquarius"
    else:
        return "Pisces"

# =========================
# HITUNG KECOCOKAN
# =========================
def hitung_jodoh(nama1, nama2):
    nilai1 = nilai_nama(nama1)
    nilai2 = nilai_nama(nama2)
    selisih = abs(nilai1 - nilai2)
    persen = 100 - (selisih % 50)
    return persen

# =========================
# REKOMENDASI NAMA 100%
# =========================
def cari_jodoh_100(nama1):
    target = nilai_nama(nama1)
    nama2 = nama1
    while True:
        nilai2 = nilai_nama(nama2)
        if abs(target - nilai2) % 50 == 0:
            return nama2
        nama2 += "a"  # tambah huruf biar cocok

# =========================
# PROGRAM UTAMA
# =========================
while True:
    print("\n === APLIKASI CEK JODOH LENGKAP ABAL ABAL===")

    nama1 = input("Nama kamu: ")
    tgl1 = int(input("Tanggal lahir kamu: "))
    bln1 = int(input("Bulan lahir kamu (1-12): "))

    nama2 = input("\nNama pasangan: ")
    tgl2 = int(input("Tanggal lahir pasangan: "))
    bln2 = int(input("Bulan lahir pasangan (1-12): "))

    persen = hitung_jodoh(nama1, nama2)
    zod1 = zodiak(tgl1, bln1)
    zod2 = zodiak(tgl2, bln2)

    print("\n ===== HASIL ===== ")
    print(f"{nama1} ({zod1}) ❤️  {nama2} ({zod2})")
    print(f"Kecocokan: {persen}%")

    # Jika hasil rendah
    if persen < 50:
        rekomendasi = cari_jodoh_100(nama1)
        print("😅 Wah, kurang cocok...")
        print(f"💡 Saran nama pasangan yang cocok 100%: {rekomendasi}")
    elif persen > 85:
        print("Kalian ditakdirkan bersama 💍")
    elif persen > 70:
        print("Cinta kalian kuat 😍")
    else:
        print("Masih perlu usaha 🙂")

    # Quote
    quotes = [
        "Cinta sejati datang pada waktu yang tepat ❤️",
        "Jodoh tidak akan tertukar 💕",
        "Cinta butuh usaha dan kesabaran 💪",
        "Yang terbaik sedang menuju kamu ✨"
    ]
    print("Quote:", random.choice(quotes))

    lagi = input("\nCek lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

print("\nTerima kasih sudah menggunakan aplikasi cinta 💖")
