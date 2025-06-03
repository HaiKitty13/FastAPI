FROM python:3.10

WORKDIR /app

COPY requirement.txt .
COPY main.py .
COPY model.pkl .

RUN pip install --no-cache-dir -r requirement.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
