FROM python:3.11

RUN mkdir app

COPY . /app

RUN pip install -r /app/requirements.txt

CMD python /app/run.py

EXPOSE 5000