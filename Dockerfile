FROM python:3

WORKDIR /flask-app

COPY requirements.txt requirements.txt
COPY Icav.py .
COPY books-2.csv .

RUN pip install -r requirements.txt

CMD [ "python", "Icav.py" ]