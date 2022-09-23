FROM python:3.10.4

# RUN pip3 install mysql-connector-python

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["index.py"]