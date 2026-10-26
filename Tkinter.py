import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "nilai_siswa.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi INTEGER NOT NULL,
            fisika INTEGER NOT NULL,
            inggris INTEGER NOT NULL,
            prediksi_fakultas TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def simpan_ke_db(nama, biologi, fisika, inggris, prediksi):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    """,
        (nama, biologi, fisika, inggris, prediksi),
    )
    conn.commit()
    conn.close()


def Submit():
    nama = entry_nama.get().strip()
    val_bio = entry_biologi.get().strip()
    val_fis = entry_fisika.get().strip()
    val_ing = entry_inggris.get().strip()

    if not nama or not val_bio or not val_fis or not val_ing:
        messagebox.showwarning(
            "Peringatan", "Semua data nilai dan nama siswa harus diisi!"
        )
        return

    if (
        not val_bio.isdigit()
        or not val_fis.isdigit()
        or not val_ing.isdigit()
    ):
        messagebox.showerror(
            "Gagal", "Nilai mata pelajaran harus berupa angka bulat!"
        )
        return

    bio = int(val_bio)
    fis = int(val_fis)
    ing = int(val_ing)

    if bio > fis and bio > ing:
        prediksi = "Kedokteran"
    elif fis > bio and fis > ing:
        prediksi = "Teknik"
    elif ing > bio and ing > fis:
        prediksi = "Bahasa"
    else:
        prediksi = "Tidak Dapat Diprediksi (Nilai Tertinggi Sama)"

    label_hasil.config(text=f"Hasil Prediksi: {prediksi}")

    simpan_ke_db(nama, bio, fis, ing, prediksi)
    messagebox.showinfo(
        "Sukses", "Data siswa dan hasil prediksi berhasil disimpan ke database!"
    )

    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

    init_db()

root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")
root.geometry("420x430")