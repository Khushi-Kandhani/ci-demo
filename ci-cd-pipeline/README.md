 # CI/CD Pipeline Demo 🚀
 
A simple FastAPI application with a fully automated CI/CD pipeline using GitHub Actions.

## 📁 Project Structure

ci-demo/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions workflow
├── src/
│   ├── __init__.py
│   └── main.py           # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_main.py      # Pytest test cases
├── conftest.py
├── requirements.txt
└── README.md


## 🛠️ Tech Stack

- **Python 3.11**
- **FastAPI** - Web framework
- **Pytest** - Testing
- **Flake8** - Linting
- **GitHub Actions** - CI/CD

## 🚀 API Endpoints

| Method | Endpoint  | Description          |
|--------|-----------|----------------------|
| GET    | /         | Home route           |
| GET    | /status   | Health check route   |

## ⚙️ CI Pipeline Steps

1. ✅ Checkout code
2. ✅ Set up Python 3.11
3. ✅ Install dependencies
4. ✅ Run Flake8 linter
5. ✅ Run Pytest tests

## 🔧 Run Locally

**Clone the repo:**
```bash
git clone https://github.com/Khushi-Kandhani/ci-demo.git
cd ci-demo
```

**Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the app:**
```bash
uvicorn src.main:app --reload
```

**Run tests:**
```bash
pytest -v
```

## 👩‍💻 Author

**Khushi Kandhani**  
[GitHub](https://github.com/Khushi-Kandhani)
