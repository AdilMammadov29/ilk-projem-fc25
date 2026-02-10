import random

# --- VERİ KISMI (MANCHESTER UNITED) ---
takim_adi = "Manchester United"

# Man Utd Taktikleri (Genelde 4-2-3-1 veya Kontra oynarlar)
taktikler = ["4-2-3-1 Dengeli", "4-3-3 Defansif", "5-2-1-2 Kontra Atak", "4-1-4-1 Baskılı"]

# Oyuncu Kadrosu (Güncel Yıldızlar)
kadro = [
    "Lammens", "Lisandro Martinez", "Harry Maguire", "Diogo Dalot", "Luke Shaw",
    "Casemiro", "Kobbie Mainoo", "Bruno Fernandes",
    "Matheus Cunha", "Benjamin Sesko", "Brian Mbeumo", "Amad Diallo", "Patrick Dorgu"
]

# --- ZEKİ SEÇİM KISMI ---
secilen_taktik = random.choice(taktikler)
kaptan = "Bruno Fernandes"  # Kaptan
kilit_oyuncu = random.choice(kadro) # Maçın kaderini değiştirecek kişi

# --- EKRANA YAZDIRMA ---
print(f"🔴 {takim_adi} Maç Analizi 🔴")
print("-" * 35)
print(f"📋 Önerilen Taktik: {secilen_taktik}")
print(f"©️ Takım Kaptanı:   {kaptan}")
print(f"🔥 Maçın Yıldızı:   {kilit_oyuncu}")
print("-" * 35)
print("Glory Glory Man United! 😈")
#Guncelleme