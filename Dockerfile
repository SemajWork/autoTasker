FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

RUN playwright install chromium
RUN playwright install-deps chromium

COPY backend/ .

EXPOSE 5000

CMD ["python", "app.py"]
