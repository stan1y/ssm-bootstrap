DOCKER_REPO	?=	stan1y
BASE_IMAGES	:=	node \
				ruby \
				python

build-image:
	@echo ---- Building $(IMAGE) ----
	docker build \
		--build-arg BASE=$(IMAGE):alpine \
		--tag $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-alpine-$(GIT_COMMIT_SHORT) \
		-f Dockerfile \
		../..

test-image:
	@echo ---- Testing $(IMAGE) ----
	@echo "No tests for $@"

publish-image:
	@echo ---- Publishing $(IMAGE) ----
	docker tag \
		$(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-alpine-$(GIT_COMMIT_SHORT) \
		$(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-alpine-latest
	docker push $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-alpine-$(GIT_COMMIT_SHORT)
	docker push $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-alpine-latest

build:
	@for image in $(BASE_IMAGES); do make build-image IMAGE=$$image; done

test:
	@for image in $(BASE_IMAGES); do make test-image IMAGE=$$image; done

publish: build test
	@for image in $(BASE_IMAGES); do make publish-image IMAGE=$$image; done

.PHONY := build test publish
.DEFAULT_GOAL := publish