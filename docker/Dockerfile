FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV APP_VERSION=local

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]