# ============================================
# Program: Sistem Diskon Belanja Online (Interaktif)
# Bahasa: Python
# ============================================

def hitung_total_bayar(total_belanja, status_member):
    """
    Fungsi untuk menghitung total bayar dan kategori diskon.
    Mengembalikan tuple: (errcode, kategori, diskon, total_bayar)
    """
    # 1️⃣ Kondisi error jika total belanja = 0
    if total_belanja == 0:
        return (1, "ERROR: Belanja tidak boleh 0!", 0, 0)

    # 2️⃣ Jika pelanggan member → diskon 10%
    if status_member:
        diskon = 0.10 * total_belanja
        kategori = "Member - Diskon 10%"

    # 3️⃣ Jika bukan member → diskon 5% jika total ≥ 200.000
    elif total_belanja >= 200000:
        diskon = 0.05 * total_belanja
        kategori = "Non-member - Diskon 5%"

    # 4️⃣ Jika total < 50.000 → tidak ada diskon
    elif total_belanja < 50000:
        diskon = 0
        kategori = "Non-member - Tidak ada diskon (belanja < 50.000)"

    # 5️⃣ Kondisi default (non-member, total antara 50.000–200.000)
    else:
        diskon = 0
        kategori = "Non-member - Tidak dapat diskon"

    total_bayar = total_belanja - diskon
    return (0, kategori, diskon, total_bayar)


# ============================================
# Bagian Input dari Pengguna
# ============================================

print("=== Sistem Diskon Belanja Online ===")

# Input total belanja
try:
    total_belanja = int(input("Masukkan total belanja (Rp): "))
except ValueError:
    print("Input tidak valid! Harus berupa angka.")
    exit()

# Input status member
status_input = input("Apakah Anda member? (ya/tidak): ").strip().lower()
if status_input not in ["ya", "tidak"]:
    print("Input status member tidak valid!")
    exit()

status_member = True if status_input == "ya" else False

# ============================================
# Proses dan Output
# ============================================

err, kategori, diskon, total_bayar = hitung_total_bayar(total_belanja, status_member)

print("\n=== HASIL TRANSAKSI ===")
print(f"Total Belanja : Rp{total_belanja:,}")
print(f"Status Member : {'Member' if status_member else 'Non-member'}")
print(f"Kategori      : {kategori}")
print(f"Diskon        : Rp{diskon:,.0f}")
print(f"Total Bayar   : Rp{total_bayar:,.0f}")
print(f"ERRCODE       : {err}")
print("==============================")
