# Implementasi Komunikasi MQTT Menggunakan Python dan Mosquitto Broker pada Sistem Air Quality Monitoring
## Tugas Mata Kuliah Cyber Physical System

### Dosen Pengampu
- Sabriansyah Rizqika Akbar, S.T., M.Eng., Ph.D.

### Disusun Oleh
- M Dzakir Thuha Al Ghaffar (245150307111004)

---

## Deskripsi Sistem
Proyek ini merupakan simulasi Air Quality Monitoring berbasis Cyber Physical System (CPS) dan Internet of Things (IoT). Sistem ini memanfaatkan protokol MQTT (Message Queuing Telemetry Transport) yang menggunakan pola komunikasi publish-subscribe untuk mendistribusikan data kualitas udara secara real-time. 

Data yang disimulasikan meliputi tiga parameter utama lingkungan:
* Kadar CO2 (dalam satuan ppm) yang dipakai di S1, S2, S3, S4 dan S5
* Suhu/Temperature (dalam satuan °C) yang dipakai di S3, S4, S5
* Kelembaban/Humidity (dalam satuan %) yang dipakai di S3, S4, S5

Simulasi ini dibagi ke dalam 5 skenario pengujian untuk menganalisis perilaku distribusi pesan berdasarkan tingkat keandalan (QoS), variasi topik, dan efisiensi menggunakan wildcard topic

---

## Prasyarat & Persiapan Lingkungan
Sebelum menjalankan simulasi, pastikan lingkungan telah dikonfigurasi dengan spesifikasi berikut
* Bahasa Pemrograman: Python 3.13.7
* MQTT Broker: Eclipse Mosquitto Broker v2.1.2
* Library Python: paho-mqtt v1.6.1

### Instalasi Library
Instal library MQTT client untuk Python melalui perintah berikut di terminal
```bash
pip install paho-mqtt

```

---

## Konfigurasi Mosquitto Broker

Broker dijalankan pada lingkungan lokal (localhost) dengan konfigurasi otentikasi anonim diaktifkan untuk kebutuhan praktikum biasa

### Spesifikasi Koneksi

* Broker Host: localhost
* Broker Port: 1883
* Keep Alive: 60 detik

### File Konfigurasi (`mosquitto.conf`)

Pastikan file konfigurasi Mosquitto mencakup baris berikut agar menerima koneksi lokal tanpa hambatan

```ini
listener 1883
allow_anonymous true

```

---

## Cara Menjalankan Program

### Langkah 1, Aktifkan Mosquitto Broker

Buka Powershell/Terminal utama, arahkan ke direktori instalasi Mosquitto, lalu jalankan broker dengan mode verbose (-v) agar log terlihat

```bash
& "C:\Program Files\mosquitto\mosquitto.exe" -c "C:\Program Files\mosquitto\mosquitto.conf" -v

```

### Langkah 2, jalankan skenario pengujian

Untuk setiap skenario, wajib membuka dua terminal terpisah (Terminal Subscriber terlebih dahulu, kemudian Terminal Publisher).

#### Skenario 1, Komunikasi Dasar (Satu Topik)

Menguji pengiriman dasar data CO2 pada satu topik tunggal (airquality/room1/co2).

```bash
# Terminal 1 (Subscriber)
cd skenario1
python subscribers1.py

# Terminal 2 (Publisher)
cd skenario1
python publishers1.py

```

#### Skenario 2m Pengujian Quality of Service (QoS 0, 1, 2)

Menguji perbedaan keandalan pengiriman pesan menggunakan mekanisme acknowledgement level 0, 1, dan 2 secara bergantian.

```bash
# Terminal 1 (Subscriber)
cd skenario2
python subscribers2.py

# Terminal 2 (Publisher)
cd skenario2
python publishers2.py

```

#### Skenario 3, Penggunaan Beberapa Topik

Mengirimkan data CO2, Suhu, dan Kelembaban secara terpisah pada jalurnya masing masing untuk struktur monitoring yang rapi

```bash
# Terminal 1 (Subscriber)
cd skenario3
python subscribers3.py

# Terminal 2 (Publisher)
cd skenario3
python publishers3.py

```

#### Skenario 4, Penggunaan Wildcard Tunggal +

Publisher mengirim data dari room1 dan room2. Subscriber menggunakan topik airquality/room1/+ sehingga hanya menyaring dan menerima data dari Room 1.

```bash
# Terminal 1 (Subscriber)
cd skenario4
python subscribers4.py

# Terminal 2 (Publisher)
cd skenario4
python publishers4.py

```

#### Skenario 5, Penggunaan Wildcard Multi-level #

Publisher mengirim data dari kedua ruangan. Subscriber menggunakan topik airquality/# untuk memantau seluruh hirarki data kualitas udara secara terpusat.

```bash
# Terminal 1 (Subscriber)
cd skenario5
python subscribers5.py

# Terminal 2 (Publisher)
cd skenario5
python publishers5.py

```

---

## Struktur Proyek

```
dzakir_mqtt_airquality/
│
├── skenario1/
│   ├── publishers1.py
│   └── subscribers1.py
│
├── skenario2/
│   ├── publishers2.py
│   └── subscribers2.py
│
├── skenario3/
│   ├── publishers3.py
│   └── subscribers3.py
│
├── skenario4/
│   ├── publishers4.py
│   └── subscribers4.py
│
├── skenario5/
│   ├── publishers5.py
│   └── subscribers5.py
│
├── screenshot/
│   ├── Output_Skenario1.png
│   ├── Output_Skenario2.png
│   ├── Output_Skenario3.png
│   ├── Output_Skenario4.png
│   └── Output_Skenario5.png
│
└── README.md
