FROM python:3.10.18-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["fastapi", "run", "src/main.py", "--port",  "8000"]