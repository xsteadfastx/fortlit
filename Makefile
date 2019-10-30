.PHONY: all clean clean_temp_files clean_dirs test init shiv

init:
	poetry install -v

test:
	poetry run tox

clean_temp_files:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*.egg-info' -type d -exec rm -rf {} \;

clean_dirs:
	rm -rf .tox
	rm -rf build/
	rm -rf dist/
	rm -rf .mypy_cache
	rm -rf .pytest_cache

clean: clean_temp_files clean_dirs

shiv:
	mkdir -p dist/
	poetry run tox -e shiv-py36
	poetry run tox -e shiv-py37
