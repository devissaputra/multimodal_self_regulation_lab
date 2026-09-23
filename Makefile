install:
	pip install -e .[dev]

test:
	pytest -q

demo:
	python examples/demo.py

check:
	python -m compileall -q src && pytest -q
