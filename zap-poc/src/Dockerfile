# syntax=docker/dockerfile:1
# --- Simple Flask API for ZAP demo ---
FROM python:3.11-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app.py .

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]

