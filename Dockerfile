FROM python:3.11.3-alpine

RUN pip install --upgrade pip

WORKDIR /python-server

ADD . /python-server

RUN pip install -r requirements.txt

CMD ["python", "wsgi.py"]