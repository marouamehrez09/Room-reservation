FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.org/simple


ENV FLASK_APP=app.py

CMD ["python", "app.py"]