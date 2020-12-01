FROM python:3-alpine
WORKDIR /app

COPY run.py /app
ENTRYPOINT ["python3", "/app/run.py"]