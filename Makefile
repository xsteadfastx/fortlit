.PHONY: all clean clean_temp_files clean_dirs test init

init:
	pipenv install --dev --python 3.6.6

test:
	pipenv run tox -r

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
