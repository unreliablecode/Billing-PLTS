# Billing-PLTS
Sistem Billing Pembangkit Listrik Tenaga Surya

Sistem ini menggunakan sensor tegangan dan sensor arus untuk menghitung daya listrik dalam satuan Watt, kemudian mengkonversinya menjadi KWh (Kilo Watt Hour). Sensor tegangan dan arus dipasang pada output listrik menuju rumah untuk mendapatkan pembacaan yang akurat.

### Rumus Daya (Watt)
```
P (Watt) = V (Volt) × I (Ampere)
```
Contoh:  
Jika tegangan (V) adalah 12V dan arus (I) sebesar 10A:  
`P = 12V × 10A = 120 Watt`

### Rumus Konversi Watt ke KiloWatt
```
P (kW) = P (Watt) ÷ 1000
```
Contoh:  
Dari contoh di atas, 120 Watt dibagi 1000:  
`P (kW) = 120 ÷ 1000 = 0.12 kW`

### Rumus Energi (KWh)
```
E (KWh) = P (kW) × Time (jam)
```
Contoh:  
Jika daya yang dihasilkan adalah 0.12 kW dan digunakan selama 2 jam:  
`E = 0.12 kW × 2 jam = 0.24 KWh`

Maka, konsumsi energi selama 2 jam adalah 0.24 KWh untuk tegangan 12V dengan arus 10A.

## Menentukan Harga Per KWh

### Rumus Harga 
```
Biaya (IDR) = Energi (kWh) × Harga per kWh (IDR)
```
Contoh:  
Jika penggunaan selama 2 jam adalah 0.24 KWh dan harga per kWh adalah 1300 IDR:  
`Biaya = 0.24 × 1300 = Rp 312`  
Jika penggunaan selama 100 jam adalah 24 KWh:  
`Biaya = 24 × 1300 = Rp 31,200`

## Menentukan Daya dari Sumber (Baterai Aki)
Jika menggunakan inverter dari 12V ke 220V, kita bisa menggunakan rumus berikut untuk menghitung daya yang dihasilkan:

```
P (Watt) = V (Volt) × Kapasitas Aki (Ah)
```
Contoh:  
Jika tegangan aki adalah 12V dan kapasitasnya 20Ah:  
`P = 12V × 20Ah = 240 Watt`  
Maka, kapasitas daya sumber adalah 240 Watt. Namun, efisiensi inverter perlu diperhitungkan.

### Rumus Mendapatkan Daya dari Baterai Aki dengan Efisiensi Inverter
```
P_eff (Watt) = P (Watt) × Efisiensi (%)
```
Contoh:  
Jika daya dari aki adalah 240 Watt dan efisiensi inverter adalah 85%:  
`P_eff = 240W × 0.85 = 204 Watt`  
Jadi, daya efektif yang bisa digunakan dari inverter adalah 204 Watt.
