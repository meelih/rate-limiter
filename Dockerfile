FROM python:3.10-slim

WORKDIR /app
COPY app.py /app
RUN pip install fastapi uvicorn redis

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
