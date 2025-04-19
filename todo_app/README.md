# ✅ Django To-Do App

A clean and minimal **To-Do List** web app built using **Django** and **Bootstrap 5**.  
Supports task creation, inline editing using the same form, deletion, and toast notifications.

---

## 📁 Folder Structure

```
tasks/
├── templates/
│   └── task_list.html
├── models.py
├── views.py
├── urls.py

core/
├── __init__.py
├── settings.py
├── urls.py
├── wsgi.py
├── asgi.py

db.sqlite3
manage.py
requirements.txt
README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo_app.git
cd todo_app
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000] in your browser.

---

## ✨ Features

- ✅ Add tasks
- 📝 Edit tasks inline using the same form
- 🗑 Delete tasks
- 🔄 Mark tasks as completed or pending
- 🔔 Bootstrap toast notifications
- 🎨 Responsive UI (Bootstrap 5)

---

## 📦 Requirements

From `requirements.txt`:

```
Django==5.2
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📜 License

Open-source under the **MIT License**.

---

## 🙌 Credits

Created as part of **Python Mini Projects** to practice Django fundamentals with frontend.