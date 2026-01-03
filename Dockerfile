FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV APP_NAME="Mock AI Service"
ENV PORT=8000

# server luôn chạy, ko override nhầm
ENTRYPOINT ["python", "-m", "uvicorn", "app:app"]

# Option, override được
CMD ["--host", "0.0.0.0", "--port", "8000"]

# ✅ HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"