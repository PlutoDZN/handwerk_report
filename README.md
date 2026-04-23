# 🛠️ Handwerk Report

Eine einfache Web-App für kleine Handwerksbetriebe, um Arbeitsberichte digital zu erfassen.

---

## 🚀 Idee

Nach einem Kundeneinsatz können Handwerker:

* Arbeitszeit eintragen
* Material erfassen
* Leistungen dokumentieren
* Kosten automatisch berechnen

👉 Ohne Papier, ohne Chaos

---

## 🎯 Zielgruppe

* Kleine Handwerksbetriebe (1–5 Mitarbeiter)
* Elektriker, Sanitär, Hausmeisterservice
* Außeneinsätze beim Kunden

---

## 🧱 Tech Stack

Backend:

* FastAPI
* SQLite
* SQLAlchemy

Frontend:

* HTML
* CSS (Tailwind geplant)
* JavaScript

---

## ⚙️ Setup (Backend)

### 1. Repo klonen

```bash
git clone https://github.com/DEIN_USERNAME/handwerk-report.git
cd handwerk-report/backend
```

---

### 2. Virtual Environment erstellen

```bash
python3 -m venv venv
```

---

### 3. Aktivieren

```bash
source venv/bin/activate
```

---

### 4. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

### 5. Server starten

```bash
uvicorn app.main:app --reload
```

---

### 6. API öffnen

👉 http://127.0.0.1:8000/docs

---

## 🔌 API

### Kunden

* GET /customers
* POST /customers

### Berichte

* GET /job-reports
* POST /job-reports
* GET /job-reports/{id}

---

## 🤝 Zusammenarbeit

Aufteilung:

* Backend → `app/`
* Frontend → `frontend/`

Workflow:

```bash
git pull
git add .
git commit -m "Änderung"
git push
```

---

## 📂 Struktur

```text
app/
  main.py
  models.py
  schemas.py
  database.py
  routes/
  services/
```

---

## 📌 Status

🚧 MVP in Entwicklung

---
