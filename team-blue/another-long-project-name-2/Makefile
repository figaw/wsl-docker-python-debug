# Name of the Docker image
IMAGE_NAME = my-python-app
# Name of the Docker container
CONTAINER_NAME = my-python-app-container

# Default target
.PHONY: all
all: build run

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
.PHONY: run
run: stop
	docker run -d --name $(CONTAINER_NAME) -p 8080:8080 $(IMAGE_NAME)

# debug the Docker container
.PHONY: debug
debug: stop
	docker run -d --name $(CONTAINER_NAME) \
		-p 8080:8080 \
		-p 5678:5678 \
		$(IMAGE_NAME) \
		-m debugpy --listen 0.0.0.0:5678 --wait-for-client app.py

# Stop the Docker container
.PHONY: stop
stop:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

# Clean up the Docker image and container
.PHONY: clean
clean: stop
	-docker rmi $(IMAGE_NAME)

# Show logs from the Docker container
.PHONY: logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Enter the Docker container shell
.PHONY: shell
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash
