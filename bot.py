from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet
from minecraft.utility import attribute_alias
import time
import random
import os
from threading import Thread

# Ayarlar
HOST = os.getenv("MINECRAFT_HOST", "play.aternos.me")
PORT = int(os.getenv("MINECRAFT_PORT", 25565))
USERNAME = os.getenv("MINECRAFT_USERNAME", "pisi_bot")
PASSWORD = os.getenv("MINECRAFT_PASSWORD", "")

print(f"🤖 Bot başlatılıyor...")
print(f"📍 Sunucu: {HOST}:{PORT}")
print(f"👤 Kullanıcı: {USERNAME}")

try:
    # Bağlantı oluştur
    connection = Connection(HOST, PORT, username=USERNAME, password=PASSWORD if PASSWORD else None)
    
    print("🔗 Bağlanıyor...")
    connection.connect()
    
    print("✅ Sunucuya bağlandı!")
    
    def keep_alive():
        print("🔄 AFK modu başladı...")
        counter = 0
        
        while connection.networking_thread and connection.networking_thread.is_alive():
            try:
                counter += 1
                time.sleep(random.randint(20, 60))
                
                if counter % 5 == 0:
                    print(f"✅ Bot aktif... ({counter*30} saniye)")
                    
            except Exception as e:
                print(f"❌ Hata: {e}")
                time.sleep(10)
    
    # AFK döngüsü başlat
    keep_alive_thread = Thread(target=keep_alive, daemon=True)
    keep_alive_thread.start()
    
    # Bağlantıyı açık tut
    while connection.networking_thread.is_alive():
        time.sleep(1)
    
    print("⛔ Bağlantı kapandı")

except Exception as e:
    print(f"❌ Bağlantı hatası: {e}")
    import traceback
    traceback.print_exc()
