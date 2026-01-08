.PHONY: style check_code_quality

export PYTHONPATH = src
check_dirs := src/sandbox

style:
	pre-commit run --all-files

check_code_quality:
	pre-commit run --all-files

publish:
	python3 -m build
	twine upload -r testpypi dist/* -u ${PYPI_USERNAME} -p ${PYPI_TEST_PASSWORD} --verbose
	twine check dist/*
	twine upload dist/* -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD} --verbose
