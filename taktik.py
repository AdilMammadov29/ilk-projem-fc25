import random

# FC 25 Takımlar ve Taktikler
takim = "Liverpool"
taktikler = ["4-3-3 Ofansif", "4-4-2 Klasik", "5-2-3 Kontra Atak", "3-5-2 Kanat Odaklı"]

print(f"--- {takim} Taktik Analizi ---")
secilen_taktik = random.choice(taktikler)

print(f"Bugünkü maç için önerilen taktik: {secilen_taktik}")