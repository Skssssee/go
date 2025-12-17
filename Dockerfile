FROM python:3.10-slim-bookworm

ENV PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY requirements.txt .
RUN pip install -U pip setuptools && pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "TEAMZYRO"]
