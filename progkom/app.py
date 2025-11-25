import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Virtual Lab Lingkaran Interaktif (1 Layar)",
    layout="wide"
)

st.title("🧪 Virtual Lab Matematika: Rumus Lingkaran")
st.markdown("Ubah Jari-Jari di kolom kiri untuk melihat perubahan Keliling dan Luas secara real-time.")

# Konstanta Pi
pi = np.pi

# --- Pembagian Kolom untuk 1 Layar ---
# Kolom pertama untuk Input dan pengaturan
# Kolom kedua untuk Visualisasi dan Hasil
col_input, col_output = st.columns([1, 2]) # Ratio 1:2 agar kolom output lebih besar

# --- Komponen Input Interaktif (Sekarang di Kolom Kiri) ---
with col_input:
    st.header("📐 Pengaturan Lingkaran")
    
    # Slider untuk Jari-Jari (r)
    r = st.slider(
        "Pilih Jari-Jari (**r**) dalam satuan cm:",
        min_value=1.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

    # Pilihan untuk menampilkan rumus
    tampilkan_rumus = st.checkbox("**Tampilkan Rumus** yang Digunakan", True)
    
    st.markdown("---")

    # --- Perhitungan ---
    d = 2 * r          # Diameter
    K = 2 * pi * r     # Keliling
    L = pi * (r ** 2)  # Luas

    # Tampilan Hasil Perhitungan
    st.subheader("✨ Hasil Perhitungan")
    st.metric(label="Jari-Jari ($r$)", value=f"{r:.2f} cm")
    st.metric(label="Diameter ($d$ = 2r)", value=f"{d:.2f} cm")
    st.metric(label="Keliling ($K$)", value=f"{K:.2f} cm")
    st.metric(label="Luas ($L$)", value=f"{L:.2f} cm²")

    # Penjelasan Rumus (jika diaktifkan)
    if tampilkan_rumus:
        st.subheader("💡 Rumus Matematika")
        st.latex(r"d = 2 \times r")
        st.latex(r"K = 2 \times \pi \times r")
        st.latex(r"L = \pi \times r^2")

# --- Komponen Output & Visualisasi (Sekarang di Kolom Kanan) ---
with col_output:
    st.header("🖼️ Visualisasi Lingkaran")
    
    # Membuat plot lingkaran
    fig, ax = plt.subplots(figsize=(8, 8)) # Ukuran figure diperbesar
    
    # Menggambar Lingkaran 

[Image of an interactive diagram showing a circle with its radius and diameter labeled, and sliders to change the radius]

    circle = plt.Circle((0, 0), r, color='skyblue', fill=True, alpha=0.5)
    ax.add_artist(circle)
    
    # Menggambar Jari-Jari (r)
    ax.plot([0, r], [0, 0], 'r--', label='Jari-Jari (r)')
    ax.text(r/2, 0.5, f'$r = {r}$', color='red')
    
    # Pengaturan sumbu agar terlihat seperti lingkaran sempurna
    # Batas sumbu disesuaikan agar selalu terlihat baik (misalnya 1 unit lebih besar dari r maksimal)
    ax_limit = 11 
    ax.set_xlim(-ax_limit, ax_limit)
    ax.set_ylim(-ax_limit, ax_limit)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"Lingkaran dengan r = {r} cm", fontsize=16)
    ax.set_xlabel("Sumbu X")
    ax.set_ylabel("Sumbu Y")
    
    st.pyplot(fig)

st.markdown("""
---
## 📝 Eksplorasi Siswa

* **Amati** bagaimana Keliling dan Luas berubah ketika Anda menggerakkan slider Jari-Jari.
* **Perhatikan** bahwa Luas meningkat jauh lebih cepat daripada Keliling ketika Jari-Jari diperbesar, karena Luas berbanding lurus dengan $r^2$.
""")
