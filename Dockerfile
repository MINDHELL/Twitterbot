FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies: ffmpeg, curl, and certificates
RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure certificates are up-to-date
RUN update-ca-certificates

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run bot
CMD ["python", "bot.py"]
