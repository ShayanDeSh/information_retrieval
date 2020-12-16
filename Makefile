export PYTHONPATH := $(shell pwd)
export PATH := $(shell pwd)/venv/bin:$(PATH)
export VIRTUAL_ENV := $(shell pwd)/venv

.PHONY: test

test:
	pytest -rP

