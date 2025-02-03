# Aplikasi Analisis Data Bike Share

Aplikasi ini adalah proyek analisis data menggunakan Streamlit yang memungkinkan pengguna untuk mengeksplorasi dataset Bike Share. Pengguna dapat memfilter data berdasarkan tanggal dan melihat jumlah peminjaman sepeda dalam rentang waktu yang dipilih.

## Fitur
- **Filter Berdasarkan Tanggal**: Pengguna dapat memilih rentang tanggal untuk melihat data peminjaman sepeda dalam periode tertentu.
- **Visualisasi**: Menampilkan grafik jumlah peminjaman sepeda berdasarkan tanggal yang telah difilter.

## Dataset
Aplikasi ini menggunakan dua dataset:
- `day.csv`: Berisi informasi peminjaman sepeda berdasarkan hari.
- `hour.csv`: Berisi informasi peminjaman sepeda berdasarkan jam.

## Prerequisites

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal Python. Anda dapat menginstal semua paket yang diperlukan dengan menjalankan:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Aplikasi
1. **Clone Repository**: Clone repository ini ke mesin lokal Anda.
   ```bash
   git clone <URL_REPOSITORY>
   cd <NAMA_FOLDER>
   streamlit run dashboard.py
   ```