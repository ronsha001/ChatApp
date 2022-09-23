FROM python:3.10.4

# RUN pip3 install mysql-connector-python

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x entry-point.sh

ENTRYPOINT ["./entry-point.sh"]