# --- Komponen Output & Visualisasi (Sekarang di Kolom Kanan) ---
with col_output:
    st.header("🖼️ Visualisasi Lingkaran")
    
    # Membuat plot lingkaran
    fig, ax = plt.subplots(figsize=(8, 8)) # Ukuran figure diperbesar
    
    # Menggambar Lingkaran
    circle = plt.Circle((0, 0), r, color='skyblue', fill=True, alpha=0.5)
    ax.add_artist(circle)
    
    # Menggambar Jari-Jari (r)
    ax.plot([0, r], [0, 0], 'r--', label='Jari-Jari (r)')
    ax.text(r/2, 0.5, f'$r = {r}$', color='red')
    
    # Pengaturan sumbu agar terlihat seperti lingkaran sempurna
# ... kode selanjutnya
