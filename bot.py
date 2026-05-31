from mineflayer import Bot
import time
import random
import os

# Ortam değişkenlerinden oku
HOST = os.getenv("MINECRAFT_HOST", "play.aternos.me")
PORT = int(os.getenv("MINECRAFT_PORT", 25565))
USERNAME = os.getenv("MINECRAFT_USERNAME")
PASSWORD = os.getenv("MINECRAFT_PASSWORD", "")

if not USERNAME:
    print("❌ MINECRAFT_USERNAME ortam değişkenini ayarlayın!")
    exit(1)

print(f"🤖 Bot başlatılıyor... {HOST}:{PORT}")
print(f"👤 Kullanıcı: {USERNAME}")

options = {
    "host": HOST,
    "port": PORT,
    "username": USERNAME,
}

# Eğer şifre varsa, ekle
if PASSWORD:
    options["password"] = PASSWORD

try:
    bot = Bot(options)
    
    @bot.on_login
    def on_login():
        print("✅ Sunucuya bağlandı!")
    
    @bot.on_spawn
    def on_spawn():
        print("🎮 Oyunda spawn oldu!")
    
    def keep_alive():
        print("🔄 AFK modu başladı...")
        counter = 0
        while True:
            try:
                counter += 1
                
                # İleri git
                if random.choice([True, False]):
                    bot.setControlState('forward', True)
                    time.sleep(random.randint(3, 8))
                    bot.setControlState('forward', False)
                
                # Sıçra
                if random.choice([True, False]):
                    bot.setControlState('jump', True)
                    time.sleep(0.3)
                    bot.setControlState('jump', False)
                
                # Sola git
                if random.choice([True, False]):
                    bot.setControlState('left', True)
                    time.sleep(random.randint(2, 5))
                    bot.setControlState('left', False)
                
                time.sleep(random.randint(15, 45))
                
                if counter % 10 == 0:
                    print(f"✅ Bot aktif... ({counter} işlem)")
                
            except Exception as e:
                print(f"❌ Hata: {e}")
                time.sleep(10)
    
    bot.start()
    keep_alive()

except Exception as e:
    print(f"❌ Bağlantı hatası: {e}")
