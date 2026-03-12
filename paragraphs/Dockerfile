FROM python:3.12-slim 

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8090 

CMD ["python", "-u", "src/main.py"]