# 🛠️ Handwerk Report

Eine einfache Web-App für kleine Handwerksbetriebe, um Arbeitsberichte digital zu erfassen.

---

## 🚀 Ziel

Handwerksbetriebe sollen nach einem Kundeneinsatz:

* Arbeitszeit erfassen
* Material dokumentieren
* Leistungen beschreiben
* automatisch Kosten berechnen

👉 **Ohne Papier, ohne Chaos, in wenigen Minuten**

---

## 🎯 Zielgruppe

* Kleine Handwerksbetriebe (1–5 Mitarbeiter)
* Elektriker, Sanitär, Hausmeisterservice
* Betriebe mit Außeneinsätzen beim Kunden

---

## 🧠 Problem

Aktuell arbeiten viele Betriebe mit:

* Papier-Stundenzetteln
* WhatsApp-Notizen
* unübersichtlichen Aufzeichnungen

Das führt zu:

* Zeitverlust
* Fehlern bei Material & Arbeitszeit
* unklaren Kosten
* schlechter Nachvollziehbarkeit

---

## 💡 Lösung

Eine einfache Web-App:

Nach dem Einsatz:

1. Kunde auswählen
2. Arbeitszeit eintragen
3. Tätigkeit beschreiben
4. Material hinzufügen

👉 Ergebnis:

* automatische Kostenberechnung
* sauberer Arbeitsbericht
* alles digital gespeichert

---

## ⚙️ Features (V1)

* Kunden anlegen
* Kundenliste anzeigen
* Arbeitsbericht erstellen
* Arbeitszeit erfassen
* Material hinzufügen
* Kosten automatisch berechnen
* Berichte speichern
* Berichte abrufen

---

## ❌ Nicht Teil von V1

* Login / Accounts
* Mitarbeiterverwaltung
* Rechnungen / Angebote
* DATEV / Buchhaltung
* GPS / Tracking
* E-Mail / WhatsApp Versand
* Dashboard / Analytics

---

## 🧱 Tech Stack

**Backend**

* Python
* FastAPI
* SQLite

**Frontend**

* HTML
* Tailwind CSS
* JavaScript

---

## 📂 Projektstruktur

```
app/
  main.py
  models.py
  schemas.py
  database.py
  routes/
    customers.py
    job_reports.py
  services/
    pricing.py
```

---

## ▶️ Setup (Backend)

### 1. Repository klonen

```
git clone https://github.com/DEIN_USERNAME/handwerk-report.git
cd handwerk-report
```

### 2. Virtual Environment aktivieren

```
source backend/venv/bin/activate
```

### 3. Server starten

```
uvicorn app.main:app --reload
```

### 4. API testen

👉 http://127.0.0.1:8000/docs

---

## 🔌 API Endpunkte

### Kunden

* `GET /customers`
* `POST /customers`

### Arbeitsberichte

* `GET /job-reports`
* `POST /job-reports`
* `GET /job-reports/{id}`

---

## 📊 Beispiel Workflow

1. Kunde anlegen
2. Arbeitsbericht erstellen
3. Start- und Endzeit eingeben
4. Material hinzufügen
5. Kosten automatisch berechnen lassen
6. Bericht speichern

---

## 🤝 Zusammenarbeit

### Aufteilung

* Backend → `app/`
* Frontend → `frontend/`

### Workflow

```
git pull
git add .
git commit -m "kurze Beschreibung"
git push
```

### Regeln

* Keine gemeinsamen Dateien gleichzeitig bearbeiten
* Kleine Commits
* Klare Messages

---

## 🗺️ Roadmap

### Phase 1

* MVP fertigstellen
* Backend + einfache UI

### Phase 2

* Erste Tests mit echten Nutzern

### Phase 3

* PDF Export
* Versand an Kunden

### Phase 4

* Erweiterungen (Teams, Angebote, Rechnungen)

---

## ⚡ Vision

Ein einfaches, schnelles Tool für Handwerksbetriebe, das:

* Papier ersetzt
* Zeit spart
* professionelle Dokumentation ermöglicht

---

## 📌 Status

🚧 In Entwicklung (MVP Phase)

---
