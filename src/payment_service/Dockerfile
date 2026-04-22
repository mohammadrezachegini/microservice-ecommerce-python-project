FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m -u 1001 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn payment_service.wsgi:application --bind 0.0.0.0:${PORT:-8004} --workers 2"]