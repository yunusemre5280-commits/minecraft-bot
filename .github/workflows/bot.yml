name: Minecraft Bot

on:
  schedule:
    - cron: '0 */6 * * *'  # Her 6 saatte bir çalıştır
  workflow_dispatch:  # Manual olarak da çalıştırabilirsiniz

jobs:
  run-bot:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Python Kur
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Kütüphaneleri Kur
      run: pip install -r requirements.txt
    
    - name: Bot'u Çalıştır
      env:
        MINECRAFT_HOST: ${{ secrets.MINECRAFT_HOST }}
        MINECRAFT_PORT: ${{ secrets.MINECRAFT_PORT }}
        MINECRAFT_USERNAME: ${{ secrets.MINECRAFT_USERNAME }}
        MINECRAFT_PASSWORD: ${{ secrets.MINECRAFT_PASSWORD }}
      run: python bot.py
