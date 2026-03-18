Login & Register Web-App






🔹 Beschreibung

Moderne Webanwendung für Benutzer-Login und Registrierung mit Flask, SQLite und bcrypt.

Die App bietet ein ansprechendes Frontend mit animierten Formularen, Floating Labels, neonfarbenem Design und ein sicheres Backend.

Benutzer können sich registrieren und einloggen

Passwörter werden sicher gehasht

AJAX-basierte Interaktion ohne Neuladen

Responsive Design für Desktop und Mobile

🌟 Features

Animiertes Login- und Registrierungsformular

Floating Labels für alle Eingabefelder

AJAX-Kommunikation mit dem Flask-Backend

Passwort-Hashing mit bcrypt

Speicherung von Benutzername, Passwort und E-Mail in SQLite

Anzeige von Erfolg- oder Fehlermeldungen direkt im Formular

🗂 Projektstruktur
/dein-projekt            # optional Name
├─ app.py                # Flask Backend
├─ users.db              # SQLite Datenbank (wird automatisch erstellt)
├─ templates/
│   └─ index.html        # Frontend HTML
└─ static/
    ├─ style.css         # CSS für Design & Animation
    └─ script.js         # JS für AJAX & Formular-Animation
📸 Screenshots

Ich hab mein Screenschots bei dem Projeckt hinzugefüngt

Login:
Erste Screenshot


Register:
Zweite Screenshot


⚡ Installation & Start

Projektordner öffnen

(Optional) Virtuelle Umgebung erstellen:

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Abhängigkeiten installieren:

pip install flask bcrypt

Flask-Server starten:

python app.py

Im Browser öffnen:
http://127.0.0.1:5000
