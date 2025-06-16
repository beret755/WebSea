{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to .venv (Python 3.12.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4c268d2-f5b4-4dca-adf3-2e561065579e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "from tkinterhtml import HtmlFrame\n",
    "import requests\n",
    "\n",
    "class SimpleWebBrowser(tk.Tk):\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "        self.title(\"Prosta przeglądarka\")\n",
    "        self.geometry(\"800x600\")\n",
    "\n",
    "        self.url_entry = ttk.Entry(self)\n",
    "        self.url_entry.pack(fill=tk.X, padx=5, pady=5)\n",
    "        self.url_entry.bind(\"<Return>\", self.load_page)\n",
    "\n",
    "        self.go_button = ttk.Button(self, text=\"Idź\", command=self.load_page)\n",
    "        self.go_button.pack(padx=5, pady=5)\n",
    "\n",
    "        self.html_frame = HtmlFrame(self, horizontal_scrollbar=\"auto\")\n",
    "        self.html_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)\n",
    "\n",
    "    def load_page(self, event=None):\n",
    "        url = self.url_entry.get()\n",
    "        if not url.startswith(\"http\"):\n",
    "            url = \"http://\" + url\n",
    "        try:\n",
    "            response = requests.get(url)\n",
    "            response.raise_for_status()\n",
    "            self.html_frame.set_content(response.text)\n",
    "        except Exception as e:\n",
    "            self.html_frame.set_content(f\"<h1>Błąd ładowania strony</h1><p>{e}</p>\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = SimpleWebBrowser()\n",
    "    app.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c79e6637-c3f6-4a3c-bfed-82d3947bd42a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "QSocketNotifier: Can only be used with threads started with QThread\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "setUrl(self, url: QUrl): argument 1 has unexpected type 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 27\u001b[39m, in \u001b[36mBrowser.load_url\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m url.startswith(\u001b[33m\"\u001b[39m\u001b[33mhttp\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m     26\u001b[39m     url = \u001b[33m\"\u001b[39m\u001b[33mhttp://\u001b[39m\u001b[33m\"\u001b[39m + url\n\u001b[32m---> \u001b[39m\u001b[32m27\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mbrowser\u001b[49m\u001b[43m.\u001b[49m\u001b[43msetUrl\u001b[49m\u001b[43m(\u001b[49m\u001b[43murl\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mTypeError\u001b[39m: setUrl(self, url: QUrl): argument 1 has unexpected type 'str'"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "0",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/beret/Dokumenty/websea/.venv/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3680: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget\n",
    "from PyQt5.QtWebEngineWidgets import QWebEngineView\n",
    "import sys\n",
    "\n",
    "class Browser(QMainWindow):\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "        self.setWindowTitle(\"Przeglądarka Saturn\")\n",
    "        self.setGeometry(100, 100, 1200, 800)\n",
    "\n",
    "        self.browser = QWebEngineView()\n",
    "        self.url_bar = QLineEdit()\n",
    "        self.url_bar.returnPressed.connect(self.load_url)\n",
    "\n",
    "        layout = QVBoxLayout()\n",
    "        layout.addWidget(self.url_bar)\n",
    "        layout.addWidget(self.browser)\n",
    "\n",
    "        container = QWidget()\n",
    "        container.setLayout(layout)\n",
    "        self.setCentralWidget(container)\n",
    "\n",
    "    def load_url(self):\n",
    "        url = self.url_bar.text()\n",
    "        if not url.startswith(\"http\"):\n",
    "            url = \"http://\" + url\n",
    "        self.browser.setUrl(url)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = QApplication(sys.argv)\n",
    "    window = Browser()\n",
    "    window.show()\n",
    "    sys.exit(app.exec_())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6e4ac69-44db-4b08-986d-270c6b32f440",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mThe Kernel crashed while executing code in the current cell or a previous cell. \n",
      "\u001b[1;31mPlease review the code in the cell(s) to identify a possible cause of the failure. \n",
      "\u001b[1;31mClick <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget\n",
    "from PyQt5.QtWebEngineWidgets import QWebEngineView\n",
    "import sys\n",
    "\n",
    "class Browser(QMainWindow):\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "        self.setWindowTitle(\"Przeglądarka Saturn\")\n",
    "        self.setGeometry(100, 100, 1200, 800)\n",
    "\n",
    "        self.browser = QWebEngineView()\n",
    "        self.url_bar = QLineEdit()\n",
    "        self.url_bar.returnPressed.connect(self.load_url)\n",
    "\n",
    "        layout = QVBoxLayout()\n",
    "        layout.addWidget(self.url_bar)\n",
    "        layout.addWidget(self.browser)\n",
    "\n",
    "        container = QWidget()\n",
    "        container.setLayout(layout)\n",
    "        self.setCentralWidget(container)\n",
    "\n",
    "        # Ładuj google.com na start\n",
    "        self.browser.setUrl(\"https://www.google.com\")\n",
    "        self.url_bar.setText(\"https://www.google.com\")\n",
    "\n",
    "    def load_url(self):\n",
    "        url = self.url_bar.text()\n",
    "        if not url.startswith(\"http\"):\n",
    "            url = \"http://\" + url\n",
    "        self.browser.setUrl(url)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = QApplication(sys.argv)\n",
    "    window = Browser()\n",
    "    window.show()\n",
    "    sys.exit(app.exec_())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
