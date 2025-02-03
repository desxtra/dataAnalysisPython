import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

# Mengonversi kolom dteday ke tipe datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Menambahkan kolom hari dalam seminggu
day_data['weekday'] = day_data['dteday'].dt.day_name()

# Judul aplikasi
st.title("Aplikasi Analisis Data Bike Share")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini adalah proyek analisis data menggunakan Streamlit yang memungkinkan pengguna untuk mengeksplorasi dataset Bike Share. 
Pengguna dapat memfilter data berdasarkan tanggal dan melihat jumlah peminjaman sepeda dalam rentang waktu yang dipilih.
""")

# Filter berdasarkan tanggal
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Tanggal Mulai", value=day_data['dteday'].min())
end_date = st.sidebar.date_input("Tanggal Akhir", value=day_data['dteday'].max())

# Filter data berdasarkan rentang tanggal
filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) & 
                          (day_data['dteday'] <= pd.to_datetime(end_date))]

# Menampilkan data yang difilter
st.subheader("Data Peminjaman Sepeda")
st.dataframe(filtered_data)

# Visualisasi jumlah peminjaman berdasarkan tanggal
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Tanggal')
plt.figure(figsize=(12, 6))
sns.lineplot(data=filtered_data, x='dteday', y='cnt', marker='o', color='blue', linewidth=2)
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Tanggal', fontsize=16)
plt.xlabel('Tanggal', fontsize=14)
plt.ylabel('Jumlah Peminjaman', fontsize=14)
plt.xticks(rotation=45)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
st.pyplot(plt)

# Visualisasi jumlah peminjaman berdasarkan jam
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Jam')
plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_data, x='hr', y='cnt', marker='o', color='blue', linewidth=2)
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Jam dalam Sehari', fontsize=16)
plt.xlabel('Jam', fontsize=14)
plt.ylabel('Jumlah Peminjaman', fontsize=14)
plt.xticks(range(0, 24))  # Menampilkan jam dari 0 hingga 23
plt.grid(color='gray', linestyle='--', linewidth=0.5)
st.pyplot(plt)

# Visualisasi jumlah peminjaman berdasarkan hari dalam seminggu
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
weekly_rentals = day_data.groupby('weekday')['cnt'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Debugging: Tampilkan hasil pengelompokan
st.write("Jumlah peminjaman berdasarkan hari dalam seminggu:", weekly_rentals)

plt.figure(figsize=(12, 6))
ax = sns.barplot(y=weekly_rentals.index, x=weekly_rentals.values, palette='pastel')
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu', fontsize=16)
plt.xlabel('Jumlah Peminjaman', fontsize=14)
plt.ylabel('Hari', fontsize=14)
plt.grid(axis='x')

# Menambahkan label pada setiap batang
for p in ax.patches:
    ax.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2), 
                ha='left', va='center', fontsize=10 , color='black', 
                xytext=(5, 0), textcoords='offset points')  # Menambahkan offset

plt.xlim(0, max(weekly_rentals.values) + 1000)  # Memberikan sedikit ruang di sebelah kanan
st.pyplot(plt)

# Visualisasi jumlah peminjaman berdasarkan musim
st.subheader('Jumlah Peminjaman Sepeda Berdasarkan Musim')
seasonal_rentals = day_data.groupby('season')['cnt'].sum()
plt.figure(figsize=(8, 5))
sns.barplot(x=seasonal_rentals.index, y=seasonal_rentals.values, palette='pastel')
plt.title('Jumlah Peminjaman Sepeda Berdasarkan Musim', fontsize=16)
plt.xlabel('Musim', fontsize=14)
plt.ylabel('Jumlah Peminjaman', fontsize=14)
plt.xticks(ticks=[0, 1, 2, 3], labels=['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])
plt.grid(axis='y')
st.pyplot(plt)

# Menambahkan penjelasan tentang hasil analisis
st.subheader("Analisis Hasil")
st.markdown("""
Dari visualisasi yang ditampilkan, dapat dilihat pola peminjaman sepeda berdasarkan hari dalam seminggu, jam, dan musim. 
Ini dapat membantu dalam memahami kapan waktu puncak peminjaman terjadi dan merencanakan strategi untuk meningkatkan layanan.
""")

# Menyediakan opsi untuk mengunduh data yang difilter
st.sidebar.header("Unduh Data")
if st.sidebar.button("Unduh Data yang Difilter"):
    filtered_data.to_csv('filtered_bike_share_data.csv', index=False)
    st.sidebar.success("Data berhasil diunduh!")