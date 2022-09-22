FROM tiangolo/uwsgi-nginx-flask:latest

WORKDIR /app

COPY . .
RUN pip3 install SQLAlchemy Flask-SQLAlchemy

ENTRYPOINT ["flask", "--app", "index.py", "run"]