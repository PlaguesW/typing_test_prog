# Typing Trainer - Backend

This is the backend API for the Typing Trainer project — an online typing speed training application inspired by MonkeyType. It supports multilingual typing (Russian, English) and programming languages (e.g., Python, JavaScript).

---

## 🚀 Features

- Retrieve random text snippets by language
- Submit typing session results
- Store user performance data (WPM, CPM, accuracy, etc.)
- Built with FastAPI and PostgreSQL

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Env Config**: python-dotenv

---

## 📦 Installation

1. **Clone the repository**
```bash
git https://github.com/PlaguesW/typing_test_prog.git
cd typing_test_prog
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip3 install -r requirements.txt
```

4. **Configure environment**
- Create .env file:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/typingdb
```

5. **Run server**
```bash
uvicorn app.main:app --reload
```