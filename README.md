# Django Mini Projects

A collection of small, independent Django projects built for learning and practice.  
Each project is self-contained and demonstrates a specific Django concept such as CRUD operations, authentication, and templating.

---

## 📌 Projects Included

### ✅ 1. **To-Do App**
📁 Path: `todo/`

- Create, update, and delete tasks
- Mark tasks as complete
- Focus on CRUD operations
- No authentication — open access

---

### ✅ 2. **Expense Tracker**
📁 Path: `expense_tracker/`

- Add, update, and delete expenses
- Track spending by category
- Includes **user authentication** (login, logout, register)
- Data is scoped to the logged-in user

---

## 🚀 Getting Started

Each project is standalone. Follow these steps **inside each project folder** (`todo/`, `expense_tracker/`).

### 1. Navigate to the project folder

```bash
cd todo        # or cd expense_tracker
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r ../requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🧠 Learning Goals

* Understand Django project setup and app structure
* Practice CRUD and form handling
* Build user authentication systems (in Expense Tracker)
* Learn modular, reusable Django patterns
* Get comfortable with running and managing multiple Django projects

---

## 🙌 Contributions

Pull requests are welcome!
Feel free to:

* Add new mini projects
* Improve existing functionality
* Suggest UI/UX or code enhancements

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Created by [@karmakr1920](https://github.com/karmakr1920)
Built with 💻 + ☕ + Django

```

---

Let me know if you want help:
- Generating `requirements.txt`
- Adding screenshots
- Creating a project index homepage (to link to each app)

Happy coding!
```
