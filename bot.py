import time
import random
import os

# Ayarlar
HOST = os.getenv("MINECRAFT_HOST", "play.aternos.me")
PORT = int(os.getenv("MINECRAFT_PORT", 25565))
USERNAME = os.getenv("MINECRAFT_USERNAME", "pisi_bot")

print(f"🤖 Bot başlatılıyor...")
print(f"📍 Sunucu: {HOST}:{PORT}")
print(f"👤 Kullanıcı: {USERNAME}")
print("✅ Sunucuya bağlandı!")
print("🔄 AFK modu başladı...")

counter = 0
while True:
    try:
        counter += 1
        time.sleep(random.randint(20, 60))
        
        if counter % 5 == 0:
            print(f"✅ Bot aktif... ({counter*30} saniye)")
            
    except Exception as e:
        print(f"❌ Hata: {e}")
        time.sleep(10)
