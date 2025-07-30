# Memory-optimized build for small droplets
FROM python:3.11-slim

WORKDIR /app

# Install only essential build dependencies with memory optimization
RUN apt-get update && apt-get install -y \
    gcc \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Configure pip for memory efficiency
RUN pip config set global.timeout 600 && \
    pip config set global.retries 5

# Copy requirements and install dependencies with memory optimization
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 