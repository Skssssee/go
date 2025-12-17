FROM python:3.8-slim-bookworm

ENV PIP_NO_CACHE_DIR=1

# Install git (now works)
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip & setuptools
RUN pip3 install --upgrade pip setuptools

# Copy application code
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Run your module
CMD ["python3", "-m", "TEAMZYRO"]
