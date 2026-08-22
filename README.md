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

## 📌 Tentang

**egaaX NglSpam** adalah tools multi-fungsi untuk Termux yang menggabungkan:

| Fitur | Keterangan |
|-------|------------|
| 🔥 **NGL Spammer** | Kirim pesan spam massal ke akun NGL |
| 🎵 **Music Player** | Cari, download, & putar lagu offline |
| 📜 **History Music** | Riwayat download tersimpan otomatis |
| 🎨 **Animasi Keren** | Spinner, progress bar, warna dinamis |
| 💾 **Offline Play** | Putar lagu tanpa koneksi internet |

> ⚠️ **Disclaimer:** Tools ini untuk **edukasi & iseng-iseng**. Gunakan dengan bijak!

---

## 📦 Persyaratan

| Package | Fungsi |
|---------|--------|
| `python` | Bahasa pemrograman |
| `git` | Clone repository |
| `mpv` | Pemutar musik |
| `yt-dlp` | Download musik dari YouTube |
| `requests` | Library HTTP requests |
| `colorama` | Pewarnaan terminal |

---

## 🚀 Cara Install (Step by Step)

### STEP 1 - Setup Storage
```bash
termux-setup-storage
```

STEP 2 - Update & Upgrade

```bash
pkg update -y
pkg upgrade -y
```

STEP 3 - Install Package

```bash
pkg install python git mpv yt-dlp -y
```

STEP 4 - Install Modul Python

```bash
pip install requests colorama
```

STEP 5 - Clone Repository

```bash
git clone https://github.com/putraalegra6-collab/SpamNGL.git
```

STEP 6 - Masuk Folder

```bash
cd SpamNGL
```

STEP 7 - Jalankan Tools

```bash
python SpamNGL.py
```

---

⚡ Cara Run (Setelah Install)

Cukup 2 langkah:

```bash
cd SpamNGL
python SpamNGL.py
```

Atau langsung satu baris:

```bash
cd SpamNGL && python SpamNGL.py
```

---

🔄 Cara Update (Jika Ada Versi Baru)

```bash
cd SpamNGL
git pull
python SpamNGL.py
```

---

💀 Reset Total (Install Ulang)

```bash
rm -rf SpamNGL
git clone https://github.com/putraalegra6-collab/SpamNGL.git
cd SpamNGL
python SpamNGL.py
```

Atau satu baris:

```bash
rm -rf SpamNGL && git clone https://github.com/putraalegra6-collab/SpamNGL.git && cd SpamNGL && python SpamNGL.py
```

---

📋 Cara Penggunaan

🔥 Mode Spam NGL

Langkah Aksi
1 Pilih menu [1]
2 Masukkan username/link NGL
3 Masukkan pesan spam
4 Masukkan jumlah spam (1-1000)
5 Masukkan delay (0.1-3 detik)
6 Konfirmasi y dan tunggu

🎵 Mode Music Player

Langkah Aksi
1 Pilih menu [2]
2 Pilih opsi: [1] Cari Lagu, [2] History, [3] Hapus
3 Jika pilih [1], masukkan judul lagu
4 Pilih nomor lagu dari daftar
5 Tunggu download selesai
6 Pilih y untuk putar sekarang

---

📸 Tampilan Menu

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

Masalah Solusi
command not found pkg install [nama] -y
ModuleNotFoundError pip install [nama]
Permission denied termux-setup-storage
No such file or directory Pastikan di folder SpamNGL
Not a directory rm -rf SpamNGL lalu clone ulang
Already exists Folder sudah ada, langsung cd SpamNGL

---

📁 Struktur Folder

```
SpamNGL/
├── SpamNGL.py            # Script utama
├── README.md             # Dokumentasi
└── music_downloads/      # Folder lagu (auto dibuat)
    └── history.json      # Riwayat download (auto dibuat)
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
Script ini untuk tujuan edukasi dan iseng-iseng.
Gunakan dengan tanggung jawab sendiri!
```

---

<div align="center">
  <b>❤️ Made with Love by Alegra Egaa ❤️</b>
  <br>
  <b>⭐ Jangan lupa kasih bintang kalo suka! ⭐</b>
</div>


---
