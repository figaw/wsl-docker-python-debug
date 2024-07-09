FROM registry.jysk.com/dockerhub/library/python:3.12

RUN mkdir /app

COPY . /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
