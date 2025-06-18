#!/usr/bin/env python3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout,
    QWidget, QPushButton, QHBoxLayout, QSystemTrayIcon,
    QMenu, QAction, QTabWidget, QDialog, QLabel
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon
import sys
import shutil
import os
import platform
from PyQt5.QtWidgets import QMessageBox

# Sprawdzenie systemu operacyjnego
if platform.system() == "Windows":
    QMessageBox.critical(None, "Nieobsługiwany system",
                         "🚫 Ta przeglądarka działa tylko na systemach Linux.\n"
                         "Zainstaluj Linuxa i przestań używać badziewia.")
    sys.exit(1)
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"
os.environ["QT_QUICK_BACKEND"] = "software"

try:
    from gi.repository import Notify
    Notify.init("WebSea")
    def show_notification(title, message):
        n = Notify.Notification.new(title, message)
        n.show()
except ImportError:
    def show_notification(title, message):
        pass

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ustawienia WebSea")
        self.setFixedSize(300, 150)

        self.clear_cookies_button = QPushButton("🪑 Wyczyść cookies", self)
        self.clear_cookies_button.clicked.connect(self.clear_cookies)
        self.clear_cookies_button.move(80, 40)

        self.status_label = QLabel("", self)
        self.status_label.move(80, 80)

    def clear_cookies(self):
        try:
            shutil.rmtree("cookies")
            os.makedirs("cookies", exist_ok=True)
            self.status_label.setText("✅ Cookies usunięte")
        except Exception as e:
            self.status_label.setText("❌ Błąd przy czyszczeniu")

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.browser = QWebEngineView()
        self.browser.settings().setAttribute(self.browser.settings().FullScreenSupportEnabled, True)
        # self.browser.fullScreenRequested.connect(lambda request: request.accept())  # PyQt5 nie wspiera tego

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)

        self.back_button = QPushButton("←")
        self.back_button.clicked.connect(self.browser.back)

        self.refresh_button = QPushButton("⟳")
        self.refresh_button.clicked.connect(self.browser.reload)

        self.fullscreen_button = QPushButton("⛶")
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)

        nav_bar = QHBoxLayout()
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.refresh_button)
        nav_bar.addWidget(self.fullscreen_button)
        nav_bar.addWidget(self.url_bar)

        layout = QVBoxLayout()
        layout.addLayout(nav_bar)
        layout.addWidget(self.browser)

        self.setLayout(layout)

        self.browser.setUrl(QUrl("https://github.com/beret755"))
        self.url_bar.setText("https://github.com/beret755")

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def toggle_fullscreen(self):
        if self.window().isFullScreen():
            self.window().showNormal()
        else:
            self.window().showFullScreen()

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebSea aplha 0.50")
        self.setGeometry(100, 100, 1200, 800)

        icon_path = "add_your_icon_path_here.png"  # Replace with your icon path
        self.setWindowIcon(QIcon(icon_path))

        # === Zakładki === 
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        # === Menu ===
        menu = self.menuBar()
        tab_menu = menu.addMenu("Karta")
        new_tab_action = QAction("Nowa karta", self)
        new_tab_action.triggered.connect(self.add_new_tab)
        tab_menu.addAction(new_tab_action)

        settings_menu = menu.addMenu("Ustawienia")
        open_settings_action = QAction("Ustawienia...", self)
        open_settings_action.triggered.connect(self.open_settings)
        settings_menu.addAction(open_settings_action)

        self.add_new_tab()

        # === Tray ===
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        tray_menu = QMenu()

        settings_action = QAction("Ustawienia", self)
        settings_action.triggered.connect(self.open_settings)
        tray_menu.addAction(settings_action)

        exit_action = QAction("Wyjdź", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        show_notification("WebSea", "this is aplha version of WebSea browser")

    def add_new_tab(self):
        new_tab = BrowserTab(self)
        index = self.tabs.addTab(new_tab, "Nowa karta")
        self.tabs.setCurrentIndex(index)
        new_tab.browser.titleChanged.connect(lambda title: self.tabs.setTabText(index, title))

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

    def open_settings(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
