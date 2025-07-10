# WebSea 🐚
Lekka przeglądarka internetowa napisana w Pythonie z użyciem PyQt5 i QtWebEngine.
To run websea you can use 
python3 websea.py 

or

 pyinstaller --noconfirm --windowed --hidden-import=PyQt5.sip --hidden-import=PyQt5.QtWebEngineWidgets websea.py

REMEBER you nedd to be in websea folder

## Funkcje
- Wiele kart (jak w Firefox/Chrome)
- Pasek adresu + przyciski nawigacji
- Ikona w system trayu + powiadomienia
- Lekki interfejs bez śmieci
- W pełni otwartoźródłowa 🔓
- Przeglądarka najlepiej działa z GNOME 46.0

## Wymagania
- Python 3.x
- PyQt5
- python3-pyqt5.qtwebengine
- libnotify (dla powiadomień na Linuxie)

## Uruchomienie
```bash
python3 websea.py
