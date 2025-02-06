FROM python:3.10.0-slim

COPY . /app

WORKDIR /app

RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \ 
    /opt/venv/bin/pip install -r requirements.txt

EXPOSE 8080

CMD ["/opt/venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]