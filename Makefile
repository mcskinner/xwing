all: install test

install:
	pip install -e .

test:
	pytest -v tests/
