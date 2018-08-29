DIRS             ?= $(shell find * -maxdepth 1 -type f -name 'Dockerfile*' | xargs -n1 dirname | sort | uniq)
BRANCH_NAME      ?= $(shell git rev-parse --abbrev-ref HEAD)
GIT_URL          ?= $(shell git remote get-url origin)
GIT_COMMIT       ?= $(shell git rev-parse HEAD)
GIT_COMMIT_SHORT ?= $(shell git rev-parse --short HEAD)
DOCKER_REPO      ?=	stan1y

build: $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO); \
		for dir in $^; do echo --- Building $$dir --- && make -C $$dir $@; done

test: build $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO); \
		for dir in $^; do echo --- Testing $$dir --- && make -C $$dir $@; done

publish: test $(DIRS)
	@export GIT_BRANCH=$(BRANCH_NAME) \
			GIT_URL=$(GIT_URL) \
			GIT_COMMIT=$(GIT_COMMIT) \
			GIT_COMMIT_SHORT=$(GIT_COMMIT_SHORT) \
			DOCKER_REPO=$(DOCKER_REPO); \
		for dir in $^; do echo --- Publishing $$dir --- && make -C $$dir $@; done

.PHONY: build test publish
.DEFAULT_GOAL: publish