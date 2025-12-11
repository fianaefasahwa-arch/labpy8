def kalkulator_aman():
    try:
        angka1 = float(input("Masukkan angka pertama: "))

        angka2 = float(input("Masukkan angka kedua: "))

    except ValueError:
        print("Error: Input harus berupa angka!")
        return

    operator = input("Masukkan operator (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    try:
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            hasil = angka1 / angka2  # Berpotensi ZeroDivisionError

        print("Hasil:", hasil)

    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")

kalkulator_aman()
