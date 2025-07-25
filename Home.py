# -*- coding: utf-8 -*-
"""Upload_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r3qjHD_LBnnTJmbPzXYb_tEM8L9rrFeO
"""

import streamlit as st
import pandas as pd

st.title("📥 Upload Dataset Mahasiswa")

# Upload file 1
uploaded_file_1 = st.file_uploader("Unggah Data Survey", type=["csv", "xlsx"])
if uploaded_file_1:
    st.session_state['df'] = pd.read_csv(uploaded_file_1) if uploaded_file_1.name.endswith(".csv") else pd.read_excel(uploaded_file_1)
    st.success("✅ File Data Survey berhasil diunggah")

# Upload file 2
uploaded_file_2 = st.file_uploader("Unggah Data IPK", type=["csv", "xlsx"])
if uploaded_file_2:
    st.session_state['df2'] = pd.read_csv(uploaded_file_2) if uploaded_file_2.name.endswith(".csv") else pd.read_excel(uploaded_file_2)
    st.success("✅ File Data IPK berhasil diunggah")

# Tombol lanjut jika keduanya sudah diunggah
if 'df' in st.session_state and 'df2' in st.session_state:
    st.page_link("pages/1_analisis_lingkungan_akademik.py", label="👉 Lanjut ke Analisis", icon="📊")
else:
    st.info("Harap unggah kedua file terlebih dahulu untuk melanjutkan.")

