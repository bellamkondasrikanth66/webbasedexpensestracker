# 💰 Web-Based Expenses Tracker

A web application built with **Python and Django** to help users track, manage, and analyze their personal expenses in an easy and organized way.

---

## 🚀 Features

* Add, edit, and delete expenses
* Categorize expenses (food, travel, shopping, etc.)
* View expense history
* Dashboard to analyze spending patterns
* User authentication system
* Responsive UI with Tailwind CSS

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Tailwind CSS, JavaScript
* **Database:** SQLite (default Django database, can be changed)

---

## 📸 Screenshots

*(Add screenshots here once available)*

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/bellamkondasrikanth66/webbasedexpensestracker.git
cd webbasedexpensestracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

* **Windows**

```bash
venv\\Scripts\\activate
```

* **Mac/Linux**

```bash
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

### 5. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```
webbasedexpensestracker/
│── expenses/           # Main app
│── templates/          # HTML templates
│── static/             # CSS, JS, images
│── db.sqlite3          # Database
│── manage.py
│── README.md
```

---

## ▶️ Usage

1. Register/Login to your account
2. Add your expenses with category and amount
3. View and analyze your spending
4. Manage expenses anytime from dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Srikanth Bellamkonda**
GitHub: [https://github.com/bellamkondasrikanth66](https://github.com/bellamkondasrikanth66)

---

## ⭐ Support

If you like this project, please give it a star ⭐ on GitHub!
