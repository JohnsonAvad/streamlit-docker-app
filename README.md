# 💰 Loan Calculator Application

A full-stack **loan calculator** built with a **FastAPI backend** and **Streamlit frontend**, fully containerized using **Docker** for easy deployment.

---

## ✨ Features

- 🔢 **Loan Calculation**: Compute total repayment and monthly installment
- 📝 **History Tracking**: Store all loan records in a CSV file
- 📥 **Downloadable Records**: Employees or applicants can download their loan history
- 🖥️ **Responsive UI**: Clean and simple Streamlit interface
- 🐳 **Dockerized**: Run everything easily using Docker Compose

---

## 🧱 Tech Stack

| Layer      | Tech        |
|------------|-------------|
| Backend    | FastAPI (Python) |
| Frontend   | Streamlit (Python) |
| Storage    | CSV via Python’s `csv` module |
| DevOps     | Docker, Docker Compose |

---

## 📁 Project Structure

```
loan-calculator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI routes
│   │   └── database.py      # CSV data handling
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py               # Streamlit UI
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🚀 Installation

### What you need before starting

- **Docker**: A tool that lets you run apps in containers, so you don't have to worry about setup.
- **Docker Compose**: Helps you start multiple containers (backend and frontend) with one command.

### How to install and run the app

1. **Clone the project** to your computer:

   ```bash
   git clone https://github.com/yourusername/loan-calculator.git
   cd loan-calculator
   ```

2. **Run the entire app** (backend + frontend) with Docker Compose:

   ```bash
   docker compose up --build
   ```

   This command will:
   - Build the backend and frontend containers
   - Start both services internally:
     - Backend API (accessible to the frontend)
     - Frontend UI at [http://localhost:8501](http://localhost:8501)

3. Open your browser and go to the frontend URL above to use the loan calculator.

---

## 🌐 API Endpoints (FastAPI)

The backend provides two main actions:

| Endpoint       | Method | What it does                                         |
|----------------|--------|-----------------------------------------------------|
| `/calculate/`  | POST   | Send loan details (amount, interest, term) and get calculated total and monthly payments |
| `/records/`    | GET    | Fetch all previous loan records saved in the system |

### Simple Explanation

- **POST `/calculate/`**: You send your loan info, and it gives you back how much you will pay monthly and in total.
- **GET `/records/`**: You get a list of all past loans recorded in the system.

---

## 📤 Why Use CSV?

We use **CSV (Comma-Separated Values)** to store data because:

- ✅ It's **lightweight** and perfect for small apps
- ✅ Easy to **read, edit, and download**
- ✅ No need to install or configure a full database
- ✅ Ideal for quick prototyping and testing

In the future, we plan to replace it with more powerful tools like **Pandas** for better data handling.

---

## ⚙️ Docker Compose Details

Here’s how the app is defined in Docker Compose:

```yaml
services:
  backend:
    build: ./backend
    environment:
      - PYTHONUNBUFFERED=1

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_API_URL=http://backend:8000
    depends_on:
      - backend
```

- The **frontend** uses the backend internally via the `http://backend:8000` URL.
- No need to expose the backend's port since only the frontend interacts with it.

---

## 🖥️ Development (Without Docker)

If you want to run backend and frontend separately on your machine:

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## ⚙️ Environment Variables

To allow the frontend to connect to the backend, we use environment variables.

Example `.env` file:

```env
STREAMLIT_API_URL=http://localhost:8000
```

---

## 🔮 Future Plans

We plan to improve this project by:

- Using **Pandas** for better data management instead of raw CSV files
- Adding user authentication and security
- Adding email notifications when loans are approved
- Writing tests to make the app more reliable

---

Feel free to open issues or pull requests!

---

*Happy loan calculating!* 💸
