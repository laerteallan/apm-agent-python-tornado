clean:
	@echo "Execute cleaning ..."
	rm -f *.pyc
	rm -f coverage.xml

pep8:
	@find . -type f -not -path "*./.venv/*" -name "*.py"|xargs flake8 --max-line-length=130 --ignore=E402 --max-complexity=6


tests: clean pep8
	py.test tests

tests-unit: clean pep8
	py.test --cov=src tests/

tests-with-coverage: clean pep8
	py.test --cov=src --cov-report=xml tests

sonar: tests-with-coverage
	sonar-scanner
