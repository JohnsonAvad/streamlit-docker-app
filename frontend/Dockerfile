FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

COPY . .

EXPOSE 8501

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8501", "server.address=0.0.0.0"]