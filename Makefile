check-linting:
		flake8 scheduler/ tests/
		black --check scheduler/ tests/
		isort --check --profile black scheduler/ tests

fix-linting:
		flake8 scheduler/ tests/
		black scheduler/ tests/
		isort --profile black scheduler/ tests
