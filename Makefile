all: install test

install:
	pip install -e src

test:
	pytest -v tests/

black:
	black -l 86 $$(find * -name '*.py')
