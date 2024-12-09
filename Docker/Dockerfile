# Використовуємо офіційний образ Python
FROM python:3.10-slim

# Встановлюємо необхідні пакети
RUN pip install --no-cache-dir paho-mqtt influxdb-client

# Створюємо директорію для вашого коду та копіюємо всі файли
WORKDIR /app
COPY . /app

# Встановлюємо сертифікат
COPY emqxsl-ca.txt.crt /usr/local/share/ca-certificates/emqxsl-ca.crt
RUN update-ca-certificates

# Вказуємо команду для запуску Python скрипту
CMD ["python", "subscriber.py"]
