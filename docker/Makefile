DIRS             ?= $(shell find * -maxdepth 1 -type f -name 'Dockerfile*' | xargs -n1 dirname | sort | uniq)
BRANCH_NAME      ?= $(shell git rev-parse --abbrev-ref HEAD)
GIT_URL          ?= $(shell git remote get-url origin)
GIT_COMMIT       ?= $(shell git rev-parse HEAD)
GIT_COMMIT_SHORT ?= $(shell git rev-parse --short HEAD)
DOCKER_REPO      ?=	stan1y

BASE_IMAGES	:=	node \
				ruby \
				python

build-image: $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO) \
			IMAGE=$(IMAGE); \
	for dir in $^; do echo > Building $$dir/$(IMAGE) && make -C $$dir build; done

test-image: $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO) \
			IMAGE=$(IMAGE); \
	for dir in $^; do echo > Testing $$dir/$(IMAGE) && make -C $$dir test; done

publish-image: $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO) \
			IMAGE=$(IMAGE); \
	for dir in $^; do echo > Publishing $$dir/$(IMAGE) && make -C $$dir publish; done

build:
	@for image in $(BASE_IMAGES); do make build-image IMAGE=$$image; done

test:
	@for image in $(BASE_IMAGES); do make test-image IMAGE=$$image; done

publish:
	@for image in $(BASE_IMAGES); do make publish-image IMAGE=$$image; done

.PHONY: build test publish
.DEFAULT_GOAL:= test