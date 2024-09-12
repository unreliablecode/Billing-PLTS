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

# Menentukan Harga Per KWh nya

Rumus Harga 
```
Biaya (IDR)=Energi (kWh)×Harga per kWh (IDR)
```
Contoh:  
Jika penggunaan selama 2 jam adalah 0.24KWh maka :
`Biaya (IDR)= 0.24×1300 = RP 312`
Dan jika penggunaan selama 100 jam adalah 24KWh maka:
`Biaya (IDR)= 24×1300 = RP 31200`
``
