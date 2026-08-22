<h1 align="center">🔥 egaaX NglSpam 🔥</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&duration=3000&pause=500&color=00FF00&center=true&vCenter=true&random=false&width=600&height=80&lines=NGL+Spam+%2B+Music+Player;Multi+Fungsi+Tools;By+Alegra+Egaa" alt="Typing SVG">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0-blue?style=for-the-badge&logo=github">
  <img src="https://img.shields.io/badge/Python-3.x-green?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Platform-Termux-orange?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Music-Player-FF69B4?style=for-the-badge&logo=spotify">
  <img src="https://img.shields.io/badge/Size-55KB-red?style=for-the-badge">
</p>

---

## 📌 **Tentang**

**egaaX NglSpam** adalah tools multi-fungsi yang dirancang untuk Termux, menggabungkan dua fitur utama dalam satu script:

| Fitur | Keterangan |
|-------|------------|
| 🔥 **NGL Spammer** | Mengirim pesan secara massal ke akun NGL. |
| 🎵 **Music Player** | Mencari, mengunduh, dan memutar lagu secara offline. |
| 📜 **History Music** | Menyimpan riwayat unduhan lagu secara otomatis. |
| 🎨 **Animasi Keren** | Dilengkapi dengan spinner, progress bar, dan warna dinamis. |
| 💾 **Offline Play** | Memutar lagu yang sudah diunduh tanpa koneksi internet. |

> ⚠️ **Disclaimer:** Tools ini dibuat untuk tujuan **edukasi dan iseng-iseng**. Harap gunakan dengan bijak dan tanggung jawab sendiri.

---

## 📦 **Persyaratan**

Pastikan Termux kamu sudah terinstall paket-paket berikut:

| Package | Fungsi |
|---------|--------|
| `python` | Bahasa pemrograman utama. |
| `git` | Untuk meng-clone repository. |
| `mpv` | Pemutar musik. |
| `yt-dlp` | Untuk mengunduh musik dari YouTube. |
| `requests` | Library untuk HTTP requests. |
| `colorama` | Library untuk pewarnaan teks di terminal. |

---

## 🚀 **Cara Install (Step by Step)**

Ikuti langkah-langkah berikut untuk menginstall tools ini di Termux:

### Langkah 1: Setup Storage
```bash
termux-setup-storage
```

Langkah 2: Update & Upgrade Paket

```bash
pkg update -y
pkg upgrade -y
```

Langkah 3: Install Paket yang Dibutuhkan

```bash
pkg install python git mpv yt-dlp -y
```

Langkah 4: Install Modul Python

```bash
pip install requests colorama
```

Langkah 5: Clone Repository

```bash
git clone https://github.com/putraalegra6-collab/SpamNGL.git
```

Langkah 6: Masuk ke Folder

```bash
cd SpamNGL
```

Langkah 7: Jalankan Tools

```bash
python SpamNGL.py
```

---

⚡ Cara Update

Jika ada pembaruan dari repository, jalankan perintah berikut:

```bash
cd ~/SpamNGL
git pull
python SpamNGL.py
```

---

📋 Cara Penggunaan

🔥 Mode Spam NGL

1. Pada menu utama, pilih angka [1].
2. Masukkan username atau link NGL target (contoh: username atau https://ngl.link/username).
3. Masukkan pesan yang ingin dikirim.
4. Tentukan jumlah spam (1-1000).
5. Atur jeda pengiriman (delay) antara 0.1 - 3 detik.
6. Konfirmasi dengan mengetik y dan tunggu proses hingga selesai.

🎵 Mode Music Player

1. Pada menu utama, pilih angka [2].
2. Pilih opsi yang tersedia:
   · [1] Cari & Download Lagu
   · [2] Lihat History Download
   · [3] Hapus Semua Lagu
3. Jika memilih [1]:
   · Masukkan judul lagu yang ingin dicari.
   · Pilih nomor lagu dari daftar hasil pencarian.
   · Tunggu proses unduhan selesai.
   · Pilih y untuk memutar lagu secara langsung.

---

📸 Tampilan Menu

Saat pertama kali dijalankan, kamu akan melihat tampilan seperti ini:

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                      ║
║     ███████╗ ██████╗  █████╗  █████╗ ██╗  ██╗          ║
║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗╚██╗██╔╝          ║
║     █████╗  ██║  ███╗███████║███████║ ╚███╔╝           ║
║     ██╔══╝  ██║   ██║██╔══██║██╔══██║ ██╔██╗           ║
║     ███████╗╚██████╔╝██║  ██║██║  ██║██╔╝ ██╗          ║
║     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝          ║
║                                                                      ║
║         💫 egaaX NglSpam V3.0 💫                    ║
║           Script By : Alegra Egaa                            ║
║         ⚠️  Gunakan Dengan Bijak! ⚠️                       ║
╚══════════════════════════════════════════════════════════════════╝

======================================================================

📌 Pilih Menu:
  [1] 🔥 NGL Spam
  [2] 🎵 Music Player
  [0] Exit
======================================================================
```

---

🛠️ Troubleshooting

Jika mengalami masalah, berikut beberapa solusi umum:

Masalah Solusi
command not found Install paket yang diperlukan: pkg install [nama_paket] -y
ModuleNotFoundError Install modul Python: pip install [nama_modul]
Permission denied Jalankan termux-setup-storage untuk memberi izin akses storage.
No such file or directory Pastikan kamu berada di folder yang benar: cd SpamNGL
Already exists Folder sudah ada, langsung masuk: cd SpamNGL lalu jalankan python SpamNGL.py

---

📁 Struktur Folder

```
SpamNGL/
├── SpamNGL.py            # Script utama
├── README.md             # Dokumentasi
└── music_downloads/      # Folder untuk menyimpan lagu (auto dibuat)
    └── history.json      # Riwayat unduhan (auto dibuat)
```

---

💬 Kontak Developer

<p align="center">
  <a href="https://github.com/putraalegra6-collab">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://www.tiktok.com/@egaa________">
    <img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white">
  </a>
  <a href="https://wa.me/62881026046579">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
  </a>
</p>

---

📝 Lisensi

```
Copyright © 2024 Alegra Egaa
Script ini dibuat untuk tujuan edukasi dan iseng-iseng.
Gunakan dengan tanggung jawab sendiri!
```

---

<div align="center">
  <b>❤️ Made with Love by Alegra Egaa ❤️</b>
  <br>
  <b>⭐ Jangan lupa kasih bintang kalo suka! ⭐</b>
</div>


---
