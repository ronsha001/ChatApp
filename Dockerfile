FROM python:3.10.4

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["index.py"]