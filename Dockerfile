FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY yolo_tanima.py .
COPY packages.txt .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health').read()"

# Run Streamlit app
CMD ["streamlit", "run", "yolo_tanima.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
