#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║                    egaaX NglSpam V3.0                          ║
║                   Script By : Alegra Egaa                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

import requests
import random
import time
import json
import os
import sys
import re
import subprocess
from datetime import datetime
from colorama import init, Fore, Style, Back

# INIT COLORAMA
init(autoreset=True)

# ============================================
# KONFIGURASI
# ============================================

VERSION = "3.0"
AUTHOR = "Alegra Egaa"
MUSIC_DIR = os.path.join(os.getcwd(), "music_downloads")
HISTORY_FILE = os.path.join(MUSIC_DIR, "history.json")

# KONFIGURASI CHAT
TELEGRAM_TOKEN = "8818093055:AAH-lPbkSWASN2KyB2a2fUkffiiaKnSLagE"
ADMIN_CHAT_ID = "6943146350"
GROUP_CHAT_ID = "-1004355627344"

# BUAT FOLDER
if not os.path.exists(MUSIC_DIR):
    os.makedirs(MUSIC_DIR)

# ============================================
# BANNER
# ============================================

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║                                                                      ║
{Fore.CYAN}║     {Fore.YELLOW}███████╗ ██████╗  █████╗  █████╗ ██╗  ██╗          {Fore.CYAN}║
{Fore.CYAN}║     {Fore.YELLOW}██╔════╝██╔════╝ ██╔══██╗██╔══██╗╚██╗██╔╝          {Fore.CYAN}║
{Fore.CYAN}║     {Fore.YELLOW}█████╗  ██║  ███╗███████║███████║ ╚███╔╝           {Fore.CYAN}║
{Fore.CYAN}║     {Fore.YELLOW}██╔══╝  ██║   ██║██╔══██║██╔══██║ ██╔██╗           {Fore.CYAN}║
{Fore.CYAN}║     {Fore.YELLOW}███████╗╚██████╔╝██║  ██║██║  ██║██╔╝ ██╗          {Fore.CYAN}║
{Fore.CYAN}║     {Fore.YELLOW}╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝          {Fore.CYAN}║
{Fore.CYAN}║                                                                      ║
{Fore.CYAN}║         {Fore.MAGENTA}💫 egaaX NglSpam V{VERSION} 💫                    {Fore.CYAN}║
{Fore.CYAN}║           {Fore.GREEN}Script By : {AUTHOR}                            {Fore.CYAN}║
{Fore.CYAN}║         {Fore.RED}⚠️  Gunakan Dengan Bijak! ⚠️                       {Fore.CYAN}║
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝
{Fore.RESET}
    """)

def music_banner():
    print(f"""
{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════╗
{Fore.MAGENTA}║                   🎵 MUSIC PLAYER 🎵                            ║
{Fore.MAGENTA}║                                                                      ║
{Fore.MAGENTA}║         {Fore.CYAN}💿 Download & Play Offline 💿                     {Fore.MAGENTA}║
{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════╝
{Fore.RESET}
    """)

# ============================================
# UTILITY FUNCTIONS
# ============================================

def loading(text="Memuat"):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for i in range(20):
        sys.stdout.write(f"\r{Fore.YELLOW}[{chars[i % len(chars)]}] {Fore.CYAN}{text}... {Fore.GREEN}{i*5}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\r{Fore.GREEN}[✓] {text} Selesai!     ")

def progress(current, total, success=0, fail=0):
    bar_length = 30
    progress_val = current / total
    filled = int(bar_length * progress_val)
    bar = "█" * filled + "░" * (bar_length - filled)
    color = Fore.GREEN if progress_val > 0.7 else Fore.YELLOW if progress_val > 0.3 else Fore.RED
    sys.stdout.write(f"\r{color}[{bar}] {Fore.CYAN}{progress_val*100:.1f}% {Fore.GREEN}✅{success} {Fore.RED}❌{fail}")
    sys.stdout.flush()

def press_enter():
    input(f"\n{Fore.YELLOW}[+] Tekan Enter untuk lanjut...")

def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ============================================
# NGL SPAM FUNCTIONS
# ============================================

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36",
]

def get_username(input_text):
    input_text = input_text.strip()
    patterns = [
        r'https?://(?:www\.)?ngl\.link/([a-zA-Z0-9_]+)',
        r'ngl\.link/([a-zA-Z0-9_]+)',
        r'@?([a-zA-Z0-9_]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, input_text)
        if match:
            return match.group(1)
    return None

def send_spam(username, message):
    try:
        url = "https://ngl.link/api/submit"
        payload = {
            "username": username,
            "question": message,
            "deviceId": f"android-{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))}"
        }
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Content-Type": "application/json",
            "Referer": "https://ngl.link/"
        }
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return True, "✅ BERHASIL"
        elif response.status_code == 429:
            return False, "⏳ RATE LIMIT"
        elif response.status_code == 404:
            return False, "❌ USERNAME SALAH"
        else:
            return False, f"❌ ERROR {response.status_code}"
    except:
        return False, "❌ GAGAL"

def ngl_spam():
    clear()
    banner()
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.MAGENTA}║                    🔥 NGL SPAMMER 🔥                            ║")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════╝")
    print()
    
    while True:
        user_input = input(f"{Fore.CYAN}[+] Masukkan Username/Link NGL: {Fore.WHITE}").strip()
        if not user_input:
            print(f"{Fore.RED}[!] Tidak boleh kosong!")
            continue
        username = get_username(user_input)
        if username:
            print(f"{Fore.GREEN}[✓] Username: @{username}")
            break
        print(f"{Fore.RED}[!] Format salah! Contoh: username atau https://ngl.link/username")
    
    while True:
        message = input(f"{Fore.CYAN}[+] Pesan Spam: {Fore.WHITE}").strip()
        if message:
            break
        print(f"{Fore.RED}[!] Pesan tidak boleh kosong!")
    
    while True:
        try:
            count = int(input(f"{Fore.CYAN}[+] Jumlah Spam (1-1000): {Fore.WHITE}").strip())
            if 1 <= count <= 1000:
                break
            print(f"{Fore.RED}[!] Minimal 1, maksimal 1000!")
        except:
            print(f"{Fore.RED}[!] Harus angka!")
    
    while True:
        try:
            delay = float(input(f"{Fore.CYAN}[+] Delay (0.1-3 detik): {Fore.WHITE}").strip())
            if 0.1 <= delay <= 3:
                break
            print(f"{Fore.RED}[!] Minimal 0.1, maksimal 3!")
        except:
            print(f"{Fore.RED}[!] Harus angka!")
    
    print(f"\n{Fore.RED}[!] PERINGATAN: Ini untuk iseng-iseng!")
    confirm = input(f"{Fore.YELLOW}[?] Lanjut? (y/n): {Fore.WHITE}").lower()
    if confirm != 'y':
        print(f"{Fore.YELLOW}[!] Dibatalkan!")
        press_enter()
        return
    
    loading("Mempersiapkan Spam")
    
    print(f"\n{Fore.GREEN}[+] Target: @{username}")
    print(f"{Fore.GREEN}[+] Jumlah: {count}")
    print(f"{Fore.GREEN}[+] Delay: {delay}s")
    print(f"{Fore.MAGENTA}{'='*70}\n")
    
    success = 0
    fail = 0
    
    for i in range(1, count + 1):
        try:
            status, msg = send_spam(username, message)
            if status:
                success += 1
                print(f"{Fore.GREEN}[{i}/{count}] ✅ {msg}")
            else:
                fail += 1
                print(f"{Fore.RED}[{i}/{count}] {msg}")
            
            progress(i, count, success, fail)
            print()
            
            if i < count:
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Dihentikan oleh user!")
            break
        except Exception as e:
            fail += 1
            print(f"{Fore.RED}[{i}/{count}] ❌ {str(e)[:30]}")
    
    print(f"\n{Fore.MAGENTA}{'='*70}")
    print(f"{Fore.GREEN}✅ Berhasil: {success}")
    print(f"{Fore.RED}❌ Gagal: {fail}")
    print(f"{Fore.YELLOW}📦 Total: {success + fail}")
    print(f"{Fore.MAGENTA}{'='*70}")
    
    if success > 0:
        print(f"{Fore.GREEN}\n🔥 Spam Berhasil!")
    else:
        print(f"{Fore.RED}\n💀 Gagal Semua!")
    
    press_enter()

# ============================================
# MUSIC FUNCTIONS
# ============================================

def check_ytdlp():
    try:
        subprocess.run("yt-dlp --version", shell=True, capture_output=True, timeout=5)
        return True
    except:
        return False

def check_mpv():
    try:
        subprocess.run("mpv --version", shell=True, capture_output=True, timeout=5)
        return True
    except:
        return False

def search_music(query):
    results = []
    
    try:
        url = f"https://api.deezer.com/search/track?q={query}&limit=10"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for track in data.get("data", []):
                duration = track.get("duration", 0)
                results.append({
                    "title": track.get("title", "Unknown"),
                    "artist": track.get("artist", {}).get("name", "Unknown"),
                    "duration": f"{duration//60}:{duration%60:02d}",
                    "url": track.get("link", "")
                })
            if results:
                return results
    except:
        pass
    
    try:
        url = f"https://itunes.apple.com/search?term={query}&media=music&limit=10"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for track in data.get("results", []):
                if track.get("wrapperType") == "track":
                    duration = track.get("trackTimeMillis", 0) // 1000
                    results.append({
                        "title": track.get("trackName", "Unknown"),
                        "artist": track.get("artistName", "Unknown"),
                        "duration": f"{duration//60}:{duration%60:02d}",
                        "url": track.get("trackViewUrl", "")
                    })
            if results:
                return results
    except:
        pass
    
    return results

def download_music(query):
    if not check_ytdlp():
        print(f"{Fore.RED}[!] yt-dlp tidak terinstall!")
        install = input(f"{Fore.YELLOW}[?] Install sekarang? (y/n): {Fore.WHITE}").lower()
        if install == 'y':
            os.system("pkg install yt-dlp -y")
            if not check_ytdlp():
                return {"success": False, "error": "Gagal install yt-dlp"}
        else:
            return {"success": False, "error": "yt-dlp diperlukan!"}
    
    try:
        print(f"{Fore.YELLOW}[+] Mencari di YouTube...")
        cmd = f"yt-dlp --no-playlist --default-search ytsearch1: '{query} audio' --print title --print id --print duration"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            return {"success": False, "error": "Gagal mencari"}
        
        lines = result.stdout.strip().split('\n')
        if len(lines) < 3:
            return {"success": False, "error": "Tidak ditemukan"}
        
        title = lines[0].strip()
        video_id = lines[1].strip()
        duration = lines[2].strip()
        
        print(f"{Fore.GREEN}[+] Ditemukan: {title}")
        print(f"{Fore.CYAN}[+] Durasi: {duration} detik")
        print(f"{Fore.YELLOW}[+] Mendownload... (butuh waktu)")
        
        output = f"{MUSIC_DIR}/%(title)s.%(ext)s"
        cmd = f"yt-dlp -x --audio-format mp3 --audio-quality 0 -o '{output}' --no-playlist 'https://youtube.com/watch?v={video_id}'"
        subprocess.run(cmd, shell=True, check=True, timeout=300)
        
        files = os.listdir(MUSIC_DIR)
        mp3s = [f for f in files if f.endswith('.mp3')]
        if mp3s:
            latest = max(mp3s, key=lambda f: os.path.getctime(os.path.join(MUSIC_DIR, f)))
            return {
                "success": True,
                "title": title,
                "artist": "Unknown Artist",
                "duration": f"{duration} detik",
                "filepath": os.path.join(MUSIC_DIR, latest),
                "filename": latest
            }
        
        return {"success": False, "error": "File tidak ditemukan"}
        
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def play_music(filepath):
    if not check_mpv():
        print(f"{Fore.RED}[!] mpv tidak terinstall!")
        install = input(f"{Fore.YELLOW}[?] Install sekarang? (y/n): {Fore.WHITE}").lower()
        if install == 'y':
            os.system("pkg install mpv -y")
            if not check_mpv():
                print(f"{Fore.RED}[!] Gagal install mpv")
                return False
    
    try:
        os.system(f"mpv --no-video '{filepath}'")
        return True
    except:
        return False

def save_history(song):
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
            for h in history:
                if h.get("title") == song.get("title") and h.get("artist") == song.get("artist"):
                    return
        except:
            pass
    
    song["downloaded_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(song)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def music_player():
    while True:
        clear()
        music_banner()
        print(f"{Fore.YELLOW}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║                                                                      ║")
        print(f"{Fore.YELLOW}║  {Fore.GREEN}[1] {Fore.CYAN}🔍 Cari & Download Lagu                         {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║  {Fore.GREEN}[2] {Fore.MAGENTA}📜 History Download                                {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║  {Fore.GREEN}[3] {Fore.RED}🗑️  Hapus Semua                                {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║  {Fore.GREEN}[0] {Fore.RED}🔙 Kembali                                       {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║                                                                      ║")
        print(f"{Fore.YELLOW}╚══════════════════════════════════════════════════════════════════╝")
        print()
        
        try:
            choice = int(input(f"{Fore.GREEN}[+] Pilih: {Fore.YELLOW}"))
        except:
            print(f"{Fore.RED}[!] Harus angka!")
            time.sleep(1)
            continue
        
        if choice == 0:
            break
        
        elif choice == 1:
            query = input(f"{Fore.CYAN}[+] Cari Lagu: {Fore.WHITE}").strip()
            if not query:
                continue
            
            print(f"{Fore.YELLOW}[+] Mencari...")
            results = search_music(query)
            
            if not results:
                print(f"{Fore.RED}[!] Tidak ditemukan di API, cari di YouTube...")
                download_result = download_music(query)
                if download_result.get("success"):
                    print(f"{Fore.GREEN}\n✅ Download Selesai!")
                    print(f"{Fore.CYAN}📁 {download_result.get('filepath')}")
                    print(f"{Fore.CYAN}🎵 {download_result.get('title')}")
                    print(f"{Fore.CYAN}👤 {download_result.get('artist')}")
                    print(f"{Fore.CYAN}⏱️ {download_result.get('duration')}")
                    
                    save_history(download_result)
                    
                    play = input(f"{Fore.YELLOW}[?] Putar sekarang? (y/n): {Fore.WHITE}").lower()
                    if play == 'y':
                        print(f"{Fore.CYAN}\n🎵 Memutar...")
                        play_music(download_result.get('filepath'))
                        print(f"{Fore.GREEN}\n✅ Selesai!")
                else:
                    print(f"{Fore.RED}[!] Gagal: {download_result.get('error')}")
                press_enter()
                continue
            
            print(f"\n{Fore.CYAN}{'='*70}")
            print(f"{Fore.GREEN}📋 HASIL PENCARIAN:")
            print(f"{Fore.CYAN}{'='*70}")
            for i, song in enumerate(results[:10], 1):
                print(f"{Fore.YELLOW}[{i}] {Fore.WHITE}{song.get('title')[:40]} {Fore.CYAN}- {Fore.MAGENTA}{song.get('artist')} {Fore.GREEN}({song.get('duration')})")
            print(f"{Fore.CYAN}{'='*70}")
            print(f"{Fore.YELLOW}[0] Kembali")
            
            try:
                choice2 = int(input(f"{Fore.GREEN}\n[+] Pilih: {Fore.YELLOW}"))
                if choice2 == 0:
                    continue
                if 1 <= choice2 <= len(results[:10]):
                    selected = results[choice2 - 1]
                    print(f"{Fore.YELLOW}\n[+] Downloading: {selected.get('title')}")
                    
                    download_result = download_music(f"{selected.get('artist')} {selected.get('title')}")
                    
                    if download_result.get("success"):
                        print(f"{Fore.GREEN}\n✅ Download Selesai!")
                        print(f"{Fore.CYAN}📁 {download_result.get('filepath')}")
                        print(f"{Fore.CYAN}🎵 {download_result.get('title')}")
                        print(f"{Fore.CYAN}👤 {download_result.get('artist')}")
                        print(f"{Fore.CYAN}⏱️ {download_result.get('duration')}")
                        
                        save_history(download_result)
                        
                        play = input(f"{Fore.YELLOW}[?] Putar sekarang? (y/n): {Fore.WHITE}").lower()
                        if play == 'y':
                            print(f"{Fore.CYAN}\n🎵 Memutar...")
                            play_music(download_result.get('filepath'))
                            print(f"{Fore.GREEN}\n✅ Selesai!")
                    else:
                        print(f"{Fore.RED}[!] Gagal: {download_result.get('error')}")
            except:
                pass
            press_enter()
        
        elif choice == 2:
            history = load_history()
            if not history:
                print(f"{Fore.YELLOW}\n[!] Belum ada history")
                press_enter()
                continue
            
            print(f"\n{Fore.CYAN}{'='*70}")
            print(f"{Fore.MAGENTA}📜 HISTORY DOWNLOAD:")
            print(f"{Fore.CYAN}{'='*70}")
            for i, song in enumerate(history, 1):
                print(f"{Fore.YELLOW}[{i}] {Fore.WHITE}{song.get('title')[:35]} {Fore.CYAN}- {Fore.MAGENTA}{song.get('artist')} {Fore.GREEN}({song.get('duration')})")
            print(f"{Fore.CYAN}{'='*70}")
            print(f"{Fore.YELLOW}[0] Kembali")
            
            try:
                choice3 = int(input(f"{Fore.GREEN}\n[+] Pilih: {Fore.YELLOW}"))
                if choice3 == 0:
                    continue
                if 1 <= choice3 <= len(history):
                    selected = history[choice3 - 1]
                    filepath = selected.get("filepath")
                    if os.path.exists(filepath):
                        print(f"{Fore.CYAN}\n🎵 Memutar...")
                        play_music(filepath)
                        print(f"{Fore.GREEN}\n✅ Selesai!")
                    else:
                        print(f"{Fore.RED}[!] File tidak ditemukan!")
                        history.pop(choice3 - 1)
                        with open(HISTORY_FILE, 'w') as f:
                            json.dump(history, f, indent=2)
            except:
                pass
            press_enter()
        
        elif choice == 3:
            confirm = input(f"{Fore.RED}[!] Hapus semua? (y/n): {Fore.WHITE}").lower()
            if confirm == 'y':
                for f in os.listdir(MUSIC_DIR):
                    if f.endswith('.mp3'):
                        os.remove(os.path.join(MUSIC_DIR, f))
                if os.path.exists(HISTORY_FILE):
                    os.remove(HISTORY_FILE)
                print(f"{Fore.GREEN}[✓] Semua dihapus!")
            press_enter()

# ============================================
# FUNGSI CHAT
# ============================================

def kirim_ke_admin(pesan, user):
    """Kirim pesan ke admin via Telegram"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        text = f"📩 **Pesan dari User**\n\n👤 Nama: {user}\n💬 Pesan: {pesan}\n\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        data = {
            "chat_id": ADMIN_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }
        resp = requests.post(url, data=data, timeout=10)
        return resp.status_code == 200
    except:
        return False

def kirim_ke_global(pesan, user):
    """Kirim pesan ke chat global via Telegram"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        text = f"👤 **{user}**\n💬 {pesan}"
        data = {
            "chat_id": GROUP_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }
        resp = requests.post(url, data=data, timeout=10)
        return resp.status_code == 200
    except:
        return False

def ambil_pesan_global():
    """Ambil 5 pesan terakhir dari chat global"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            messages = []
            for msg in data.get('result', [])[-5:]:
                chat_id = msg.get('message', {}).get('chat', {}).get('id')
                if str(chat_id) == GROUP_CHAT_ID:
                    text = msg.get('message', {}).get('text', '')
                    user = msg.get('message', {}).get('from', {}).get('first_name', 'Unknown')
                    if text:
                        messages.append(f"👤 {user}: {text}")
            if messages:
                return "\n".join(messages[::-1])
            return "Belum ada pesan di chat global"
    except:
        return "Gagal mengambil pesan"

def ambil_balasan_admin():
    """Ambil balasan dari admin"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            messages = []
            for msg in data.get('result', [])[-5:]:
                chat_id = msg.get('message', {}).get('chat', {}).get('id')
                if str(chat_id) == ADMIN_CHAT_ID:
                    text = msg.get('message', {}).get('text', '')
                    if text and not text.startswith('/'):
                        messages.append(f"👨‍💻 Developer: {text}")
            if messages:
                return "\n".join(messages[::-1])
            return "Belum ada balasan dari Developer"
    except:
        return "Gagal mengambil pesan"

def chat_admin():
    """Menu chat admin"""
    clear()
    music_banner()
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.MAGENTA}║                   💬 CHAT ADMIN 💬                            ║")
    print(f"{Fore.MAGENTA}║                                                                      ║")
    print(f"{Fore.MAGENTA}║         {Fore.CYAN}Hubungi Developer Langsung via Telegram              {Fore.MAGENTA}║")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════╝")
    print()
    
    print(f"{Fore.YELLOW}[!] Pesan akan langsung dikirim ke Developer")
    print(f"{Fore.GREEN}[✓] Developer akan bales via Telegram")
    print(f"{Fore.CYAN}[✓] Cek balasan di menu 'Cek Balasan'\n")
    
    user = input(f"{Fore.CYAN}[+] Nama Kamu: {Fore.WHITE}").strip() or "User"
    pesan = input(f"{Fore.CYAN}[+] Pesan: {Fore.WHITE}").strip()
    
    if not pesan:
        print(f"{Fore.RED}[!] Pesan tidak boleh kosong!")
        press_enter()
        return
    
    print(f"\n{Fore.YELLOW}[+] Mengirim pesan ke Developer...")
    if kirim_ke_admin(pesan, user):
        print(f"{Fore.GREEN}[✓] Pesan terkirim!")
        print(f"{Fore.CYAN}[✓] Developer akan bales segera")
    else:
        print(f"{Fore.RED}[!] Gagal mengirim! Cek koneksi internet")
    
    press_enter()

def chat_global():
    """Menu chat global"""
    while True:
        clear()
        music_banner()
        print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.MAGENTA}║                   🌐 CHAT GLOBAL 🌐                            ║")
        print(f"{Fore.MAGENTA}║                                                                      ║")
        print(f"{Fore.MAGENTA}║         {Fore.CYAN}Komunitas Pengguna SpamNGL                         {Fore.MAGENTA}║")
        print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════╝")
        print()
        
        print(f"{Fore.YELLOW}📜 Pesan Terbaru:\n")
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.WHITE}{ambil_pesan_global()}")
        print(f"{Fore.CYAN}{'='*50}\n")
        
        print(f"{Fore.GREEN}[1] Kirim Pesan")
        print(f"{Fore.MAGENTA}[2] Refresh Pesan")
        print(f"{Fore.RED}[0] Kembali")
        print()
        
        try:
            choice = int(input(f"{Fore.GREEN}[+] Pilih: {Fore.YELLOW}"))
        except:
            print(f"{Fore.RED}[!] Harus angka!")
            time.sleep(1)
            continue
        
        if choice == 0:
            break
        elif choice == 1:
            user = input(f"{Fore.CYAN}[+] Nama Kamu: {Fore.WHITE}").strip() or "User"
            pesan = input(f"{Fore.CYAN}[+] Pesan: {Fore.WHITE}").strip()
            if not pesan:
                print(f"{Fore.RED}[!] Pesan tidak boleh kosong!")
                time.sleep(1)
                continue
            
            print(f"{Fore.YELLOW}[+] Mengirim ke chat global...")
            if kirim_ke_global(pesan, user):
                print(f"{Fore.GREEN}[✓] Pesan terkirim!")
            else:
                print(f"{Fore.RED}[!] Gagal mengirim!")
            time.sleep(1)
        elif choice == 2:
            continue

def cek_balasan():
    """Cek balasan dari admin"""
    clear()
    music_banner()
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.MAGENTA}║                   📩 CEK BALASAN 📩                            ║")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════════════════════════════════════╝")
    print()
    
    print(f"{Fore.YELLOW}[+] Cek pesan dari Developer...\n")
    
    balasan = ambil_balasan_admin()
    print(f"{Fore.CYAN}{'='*50}")
    print(f"{Fore.WHITE}{balasan}")
    print(f"{Fore.CYAN}{'='*50}")
    
    press_enter()

# ============================================
# MAIN MENU
# ============================================

def main():
    while True:
        clear()
        banner()
        print(f"{Fore.MAGENTA}{'='*70}")
        print(f"{Fore.CYAN}\n📌 Pilih Menu:")
        print(f"{Fore.GREEN}  [1] 🔥 NGL Spam")
        print(f"{Fore.MAGENTA}  [2] 🎵 Music Player")
        print(f"{Fore.YELLOW}  [3] 💬 Chat Admin (Hubungi Developer)")
        print(f"{Fore.CYAN}  [4] 🌐 Chat Global (Komunitas)")
        print(f"{Fore.GREEN}  [5] 📩 Cek Balasan Admin")
        print(f"{Fore.RED}  [0] Exit")
        print(f"{Fore.MAGENTA}{'='*70}")
        print()
        
        try:
            choice = int(input(f"{Fore.GREEN}[+] Pilih: {Fore.YELLOW}"))
        except:
            print(f"{Fore.RED}[!] Harus angka!")
            time.sleep(1)
            continue
        
        if choice == 0:
            print(f"{Fore.RED}\n[!] Keluar...")
            print(f"{Fore.CYAN}\nScript By : {AUTHOR}")
            sys.exit()
        elif choice == 1:
            ngl_spam()
        elif choice == 2:
            music_player()
        elif choice == 3:
            chat_admin()
        elif choice == 4:
            chat_global()
        elif choice == 5:
            cek_balasan()
        else:
            print(f"{Fore.RED}[!] Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Keluar...")
        print(f"{Fore.CYAN}\nScript By : {AUTHOR}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}")
        print(f"{Fore.CYAN}\nScript By : {AUTHOR}")
