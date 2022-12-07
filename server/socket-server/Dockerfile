FROM python:3.9

WORKDIR /app
COPY . /app/

RUN pip install jpysocket;

CMD ["python" "server.py"]
EXPOSE 8080