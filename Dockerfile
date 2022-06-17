FROM python:3.10
WORKDIR /code

ENV FLASK_RUN_HOST=0.0.0.0

RUN apt update -y && apt upgrade -y && apt install -y gcc musl-dev linux-headers-generic
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run"]
