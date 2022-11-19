FROM python:3.9-slim

WORKDIR /app

RUN pip install dash

COPY . .

EXPOSE 5050

CMD ["python", "demo_app2.py"]