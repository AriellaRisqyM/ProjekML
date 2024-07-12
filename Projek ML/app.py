import streamlit as st
import pandas as pd
from projek_ml import run_projek

# Judul aplikasi
st.title('Aplikasi Pemrosesan Data')

# Fungsi untuk membaca file Excel/CSV
@st.cache
def load_data(file):
    if file.type == 'text/csv':
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)

# Upload file
uploaded_file = st.file_uploader("Unggah file Excel/CSV", type=["csv", "xlsx"])

if uploaded_file:
    data = load_data(uploaded_file)
    st.write("Data yang diunggah:")
    st.write(data.head())

    # Jalankan program
    result = run_projek(data)
    
    # Tampilkan hasil
    st.write("Hasil pemrosesan:")
    st.write(result)

