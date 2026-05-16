import streamlit as st
import math

st.title("Kalkulator Luas Lingkaran")

# Input jari-jari
r = st.number_input("Masukkan jari-jari")

# Hitung luas
luas = math.pi * r * r

# Tampilkan hasil
st.write("Luas lingkaran adalah =", luas)
