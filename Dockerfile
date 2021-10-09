FROM python:3.7-slim-buster

ADD . /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]