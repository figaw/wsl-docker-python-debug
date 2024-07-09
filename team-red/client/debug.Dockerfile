FROM registry.jysk.com/dockerhub/library/python:3.12

RUN mkdir /app

# in the debug.Dockerfile, we don't copy in the app,
# but use it as a volume-mount, so we can hot-reload files;
#   i.e. the app picks up changes, without having to rebuild the container.
# COPY . /app
COPY client/requirements.txt /app
COPY global-version-file-example /mnt/version

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
