PROJECT_NAME= mlops_assignment
DOCKER_IMAGE_NAME=$(PROJECT_NAME)_image
install:
	pip install -r requirements.txt

build:
	docker build -t $(DOCKER_IMAGE_NAME) .
test:
	python -m unittest test.py 