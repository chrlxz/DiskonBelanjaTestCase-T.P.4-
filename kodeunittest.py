def hitung_diskon(total, member):
    """
    Fungsi menghitung total bayar setelah diskon.
    Mengembalikan tuple (ERRCODE, total_bayar)
    """
    if total == 0:
        ERRCODE = 1
        return ERRCODE, 0  # Error: total belanja 0

    ERRCODE = 0

    if member:
        total_bayar = total * 0.9       # Diskon 10%
    elif total >= 200000:
        total_bayar = total * 0.95      # Diskon 5%
    elif total < 50000:
        total_bayar = total              # Tidak ada diskon
    else:
        total_bayar = total              # Kondisi default

    return ERRCODE, total_bayar


# Contoh pemanggilan fungsi seperti di C++
err, hasil = hitung_diskon(150000, True)
print(hasil)  # Output: 135000
