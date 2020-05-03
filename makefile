SHELL 	:= /bin/bash
VENV 		:= .env/bin
PYTHONPATH=$(shell pwd)

.EXPORT_ALL_VARIABLES:
.PHONY: all

install:
	( \
		python3 -m venv .env; \
		source .env/bin/activate; \
		pip install -r requirements.txt; \
		mkdir -p output; \
	)

test:
	$(VENV)/python -m unittest discover -vfb