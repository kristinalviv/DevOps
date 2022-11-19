FROM python:3.9-slim

WORKDIR /app

RUN pip install dash

COPY . .

EXPOSE 4050

CMD ["python", "demo_app1.py"]