import streamlit as st
import numpy as np
import pickle

# Load model yang sudah disimpan
model_path = 'model_uas.pkl'
model = pickle.load(open(model_path, 'rb'))

# Judul aplikasi
st.title("Prediksi Biaya Asuransi")
st.write("Aplikasi ini memprediksi biaya asuransi berdasarkan data input yang diberikan.")

# Form input
st.header("Input Data")
age = st.number_input("Umur", min_value=1, max_value=120, value=25, step=1)
sex = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input("Jumlah Anak", min_value=0, max_value=10, value=0, step=1)
smoker = st.selectbox("Perokok", ["Ya", "Tidak"])

# Encode input categorical
sex_encoded = 0 if sex == "Laki-laki" else 1
smoker_encoded = 1 if smoker == "Ya" else 0

# Buat input untuk model
input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded]])

# Prediksi
if st.button("Prediksi"):
    prediction = model.predict(input_data)
    st.success(f"Estimasi Biaya Asuransi: ${prediction[0]:,.2f}")

# Footer
st.write("---")
st.write("Dibuat oleh: Muhammad Dzaki Zahirsyah")
st.write("NIM: 2021230043")
