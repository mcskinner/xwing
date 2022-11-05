all: install test

install:
	pip install -e src

test:
	pytest -v tests/
