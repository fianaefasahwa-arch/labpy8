nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_valid = 0

for n in nilai:
    try:
        # Coba ubah ke angka
        angka = float(n)
        total += angka
        jumlah_valid += 1

    except ValueError:
        # Jika bukan angka, skip tanpa hentikan program
        print(f"Data tidak valid dilewati: {n}")
        continue

if jumlah_valid > 0:
    rata_rata = total / jumlah_valid
    print("Rata-rata nilai valid:", rata_rata)
else:
    print("Tidak ada data valid.")
