FROM python:3.12

RUN mkdir /app

COPY server/. /app
COPY global-version-file-example /mnt/version

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
