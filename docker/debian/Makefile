ifeq ($(DOCKER_REPO),)
$(error DOCKER_REPO must be specified)
endif

ifeq ($(IMAGE),)
$(error IMAGE must be specified)
endif

build:
	docker build \
		--build-arg BASE=$(IMAGE):slim \
		--tag $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-slim-$(GIT_COMMIT_SHORT) \
		-f Dockerfile \
		../..

test: build
	@echo "No tests for $(IMAGE)"

publish: test
	docker tag \
		$(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-slim-$(GIT_COMMIT_SHORT) \
		$(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-slim-latest
	docker push $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-slim-$(GIT_COMMIT_SHORT)
	docker push $(DOCKER_REPO)/ssm-bootstrap:$(IMAGE)-slim-latest


.PHONY := build test publish
.DEFAULT_GOAL := test