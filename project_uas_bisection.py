import streamlit as st
st.title("Project UAS Matematika Komputasi Metode Bisection")
st.write("Halo, ini aplikasi pertama saya di Streamlit.")

# Import Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input Data dari Pengguna
fungsi = st.text_input(
    "Masukkan fungsi yang ingin dicari akarnya",
    "x**3 - 4*x - 9"
)

batas_bawah = st.number_input(
    "Masukkan batas bawah interval",
    value=2.0
)

batas_atas = st.number_input(
    "Masukkan batas atas interval",
    value=3.0
)

toleransi = st.number_input(
    "Masukkan tingkat ketelitian",
    value=0.0001,
    format="%.4f"
)

# Membuat Fungsi Matematika
def hitung_fungsi(x):
    return eval(fungsi)

# Memeriksa Syarat Metode Bisection
if hitung_fungsi(batas_bawah) * hitung_fungsi(batas_atas) > 0:
    print("Interval yang dimasukkan tidak memenuhi syarat Metode Bisection")
else:
    st.success("Interval memenuhi syarat")

# Perhitungan Metode Bisection

data_iterasi = []

jumlah_iterasi = 0

while abs(batas_atas - batas_bawah) > toleransi:

    titik_tengah = (batas_bawah + batas_atas) / 2

    data_iterasi.append([
        jumlah_iterasi + 1,
        batas_bawah,
        batas_atas,
        titik_tengah
    ])

    if hitung_fungsi(batas_bawah) * hitung_fungsi(titik_tengah) < 0:
        batas_atas = titik_tengah
    else:
        batas_bawah = titik_tengah

    jumlah_iterasi += 1

akar = (batas_bawah + batas_atas) / 2

st.write("Akar persamaan =", akar)
st.write("Jumlah iterasi =", jumlah_iterasi)

# Menampilkan Tabel Iterasi

tabel_iterasi = pd.DataFrame(
    data_iterasi,
    columns=[
        "Iterasi",
        "Batas Bawah",
        "Batas Atas",
        "Titik Tengah"
    ]
)

st.dataframe(tabel_iterasi)


# Menampilkan Grafik Fungsi

x = np.linspace(batas_bawah - 2, batas_atas + 2, 400)
y = [hitung_fungsi(nilai_x) for nilai_x in x]

plt.figure(figsize=(8,5))
plt.plot(x, y)
plt.axhline(y=0)

plt.title("Grafik Fungsi")
plt.xlabel("Nilai x")
plt.ylabel("Nilai f(x)")
plt.grid()
st.pyplot(plt)
