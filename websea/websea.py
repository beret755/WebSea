#!/usr/bin/env python3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QVBoxLayout,
    QWidget, QPushButton, QHBoxLayout, QSystemTrayIcon,
    QMenu, QAction, QTabWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QFont
import sys

try:
    from gi.repository import Notify
    Notify.init("WebSea")
    def show_notification(title, message):
        n = Notify.Notification.new(title, message)
        n.show()
except ImportError:
    def show_notification(title, message):
        pass

BUTTON_STYLE = """
QPushButton {
    background-color: #2d89ef;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 6px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #1b5fbd;
}
"""

URL_BAR_STYLE = """
QLineEdit {
    border: 2px solid #2d89ef;
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 14px;
}
QLineEdit:focus {
    border-color: #1b5fbd;
    background-color: #e6f0fb;
}
"""

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.browser = QWebEngineView()
        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet(URL_BAR_STYLE)
        self.url_bar.returnPressed.connect(self.load_url)

        self.back_button = QPushButton("←")
        self.back_button.setStyleSheet(BUTTON_STYLE)
        self.back_button.clicked.connect(self.browser.back)

        self.refresh_button = QPushButton("⟳")
        self.refresh_button.setStyleSheet(BUTTON_STYLE)
        self.refresh_button.clicked.connect(self.browser.reload)

        self.clear_cookies_button = QPushButton("Usuń cookies")
        self.clear_cookies_button.setStyleSheet(BUTTON_STYLE)
        self.clear_cookies_button.clicked.connect(self.clear_cookies)

        nav_bar = QHBoxLayout()
        nav_bar.setSpacing(8)
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.refresh_button)
        nav_bar.addWidget(self.clear_cookies_button)
        nav_bar.addWidget(self.url_bar)

        layout = QVBoxLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        layout.addLayout(nav_bar)
        layout.addWidget(self.browser)

        self.setLayout(layout)

        self.browser.setUrl(QUrl("https://www.google.com"))
        self.url_bar.setText("https://www.google.com")

        self.set_dark_mode(False)

    def load_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def clear_cookies(self):
        profile = self.browser.page().profile()
        profile.cookieStore().deleteAllCookies()
        show_notification("WebSea", "Cookies usunięte, kurwa!")

    def set_dark_mode(self, enabled):
        if enabled:
            self.browser.page().setBackgroundColor(Qt.black)
            self.url_bar.setStyleSheet(URL_BAR_STYLE + "QLineEdit { background-color: #222; color: white; border-color: #555; }")
        else:
            self.browser.page().setBackgroundColor(Qt.white)
            self.url_bar.setStyleSheet(URL_BAR_STYLE)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebSea")
        self.setGeometry(100, 100, 1200, 800)

        icon_path = "/home/beret/Dokumenty/websea/websea.png"
        self.setWindowIcon(QIcon(icon_path))

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        menu = self.menuBar()
        tab_menu = menu.addMenu("Karta")
        new_tab_action = QAction("Nowa karta", self)
        new_tab_action.triggered.connect(self.add_new_tab)
        tab_menu.addAction(new_tab_action)

        settings_menu = menu.addMenu("Ustawienia")
        self.dark_mode_action = QAction("Tryb ciemny", self, checkable=True)
        self.dark_mode_action.triggered.connect(self.toggle_dark_mode)
        settings_menu.addAction(self.dark_mode_action)

        self.add_new_tab()

        self.tray_icon = QSystemTrayIcon(QIcon(icon_path), self)
        tray_menu = QMenu()
        exit_action = QAction("Wyjdź", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        show_notification("WebSea", "Przeglądarka uruchomiona!")

    def add_new_tab(self):
        new_tab = BrowserTab(self)
        index = self.tabs.addTab(new_tab, "Nowa karta")
        self.tabs.setCurrentIndex(index)
        new_tab.browser.titleChanged.connect(lambda title: self.tabs.setTabText(index, title))
        new_tab.set_dark_mode(self.dark_mode_action.isChecked())

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

    def toggle_dark_mode(self):
        enabled = self.dark_mode_action.isChecked()
        for i in range(self.tabs.count()):
            tab = self.tabs.widget(i)
            tab.set_dark_mode(enabled)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())

