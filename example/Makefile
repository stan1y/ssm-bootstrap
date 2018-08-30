BRANCH_NAME      ?= $(shell git rev-parse --abbrev-ref HEAD)
GIT_URL          ?= $(shell git remote get-url origin)
GIT_COMMIT       ?= $(shell git rev-parse HEAD)
GIT_COMMIT_SHORT ?= $(shell git rev-parse --short HEAD)

ifeq ($(DOCKER_USERNAME),)
$(error DOCKER_USERNAME must be specified)
endif

build:
	docker build \
		--tag $(DOCKER_USERNAME)/ssm-bootstrap:example-$(GIT_COMMIT_SHORT) \
		-f Dockerfile .

publish: build
	docker tag \
		$(DOCKER_USERNAME)/ssm-bootstrap:example-$(GIT_COMMIT_SHORT) \
		$(DOCKER_USERNAME)/ssm-bootstrap:example-latest
	docker push $(DOCKER_USERNAME)/ssm-bootstrap:example-$(GIT_COMMIT_SHORT)
	docker push $(DOCKER_USERNAME)/ssm-bootstrap:example-latest


.PHONY := build publish
.DEFAULT_GOAL := build
