def hitung_daya(v, i):
    # Menghitung Daya dalam Watt
    return v * i

def konversi_ke_kW(daya_watt):
    # Mengonversi Watt ke KiloWatt
    return daya_watt / 1000

def hitung_energi_kwH(daya_kW, waktu_jam):
    # Menghitung Energi dalam KWh
    return daya_kW * waktu_jam

def hitung_biaya(energi_kwH, harga_per_kwH):
    # Menghitung Biaya dalam IDR
    return energi_kwH * harga_per_kwH

def daya_baterai(v, kapasitas_ah):
    # Menghitung Daya dari Baterai (Watt)
    return v * kapasitas_ah

def daya_baterai_efisien(daya_baterai, efisiensi):
    # Menghitung Daya Efektif dengan Efisiensi Inverter (%)
    return daya_baterai * (efisiensi / 100)

# Input dari pengguna
v = float(input("Masukkan Tegangan (V): "))
i = float(input("Masukkan Arus (A): "))
waktu_jam = float(input("Masukkan Waktu Penggunaan (jam): "))
harga_per_kwH = float(input("Masukkan Harga per KWh (IDR): "))

# Perhitungan Daya dan Energi
daya_watt = hitung_daya(v, i)
daya_kW = konversi_ke_kW(daya_watt)
energi_kwH = hitung_energi_kwH(daya_kW, waktu_jam)
biaya = hitung_biaya(energi_kwH, harga_per_kwH)

print(f"\n--- Hasil Perhitungan ---")
print(f"Daya: {daya_watt} Watt ({daya_kW} kW)")
print(f"Energi: {energi_kwH} KWh")
print(f"Biaya: Rp {biaya:,}")

# Perhitungan Daya dari Baterai
v_baterai = float(input("\nMasukkan Tegangan Baterai (V): "))
kapasitas_ah = float(input("Masukkan Kapasitas Baterai (Ah): "))
efisiensi = float(input("Masukkan Efisiensi Inverter (%): "))

daya_bat = daya_baterai(v_baterai, kapasitas_ah)
daya_efektif = daya_baterai_efisien(daya_bat, efisiensi)

print(f"\nDaya Baterai: {daya_bat} Watt")
print(f"Daya Efektif dengan Efisiensi {efisiensi}%: {daya_efektif} Watt")
