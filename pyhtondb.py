import tkinter as tk
import sqlite3


# Menghubungkan ke database SQLite
conn = sqlite3.connect('prodi_ti.db')
cursor = conn.cursor()
# Membuat tabel prodi jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS prodi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matematika REAL,
    inggris REAL,
    geografi REAL,
    prediksi TEXT
)
''')

# Menutup koneksi sementara
conn.commit()

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Aplikasi Prodi Pilihan")
jendela.configure(bg="#87CEFA")

# Variabel untuk menyimpan nilai input
matematika = tk.DoubleVar()
inggris = tk.DoubleVar()
geografi = tk.DoubleVar()

# Fungsi prediksi
def prediksi():
    # Cek apakah ada nilai yang kurang dari 75
    if geografi.get() < 75.0 or inggris.get() < 75.0 or matematika.get() < 75.0:
        a = 'Tidak Lulus Seleksi'
    else:
        if matematika.get() > 99 and inggris.get() > 99:
            a = 'Kedokteran'
        elif geografi.get() > 90 and matematika.get() > 88:
            a = 'Teknik'
        elif inggris.get() > 82 and geografi.get() > 80:
            a = 'Pertanian'
        else:
            a = 'Ilmu padi'

    
    # Menyimpan data ke database
    cursor.execute('''
    INSERT INTO prodi (matematika, inggris, geografi, prediksi)
    VALUES (?, ?, ?, ?)
    ''', (matematika.get(), inggris.get(), geografi.get(), a))
    conn.commit()

 
    # Mengupdate teks pada hasil_label dengan hasil prediksi
    hasil_label.config(text=f"Hasil Prediksi: {a}")

# Label dan entry untuk nilai Geografi
geografi_label = tk.Label(jendela, text="Nilai Geografi", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#FF0000")
geografi_label.place(relx=0.5, rely=0.15, anchor="center")

geografi_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFFFFF", textvariable=geografi)
geografi_entry.place(relx=0.5, rely=0.22, anchor="center")

# Label dan entry untuk nilai Matematika
matematika_label = tk.Label(jendela, text="Nilai Matematika", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#FF0000")
matematika_label.place(relx=0.5, rely=0.28, anchor="center")

matematika_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFFFFF", textvariable=matematika)
matematika_entry.place(relx=0.5, rely=0.35, anchor="center")

# Label dan entry untuk nilai Bahasa Inggris
bahasa_inggris_label = tk.Label(jendela, text="Nilai Bahasa Inggris", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#FF0000")
bahasa_inggris_label.place(relx=0.5, rely=0.41, anchor="center")

bahasa_inggris_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFFFFF", textvariable=inggris)
bahasa_inggris_entry.place(relx=0.5, rely=0.48, anchor="center")

# Tombol prediksi
prediksi_button = tk.Button(jendela, text="Prediksi", command=prediksi, font=("Arial", 12, "bold"), bg="#FFA07A", fg="#000000")
prediksi_button.place(relx=0.5, rely=0.55, anchor="center")

# Label hasil prediksi
hasil_label = tk.Label(jendela, font=("Arial", 12), fg="#FFFFFF", bg="#123456")
hasil_label.place(relx=0.5, rely=0.65, anchor="center")

# Menjalankan aplikasi
jendela.mainloop()


